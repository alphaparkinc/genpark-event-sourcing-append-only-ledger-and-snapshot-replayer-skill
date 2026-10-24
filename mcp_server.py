"""MCP server for Event Sourcing Ledger Engine."""
import sys
import json
from client import EventSourcingLedgerEngine

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [{
                "name": "replay_event_sourcing_stream",
                "description": "Replays an immutable sequence of events over an initial snapshot",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "initial_snapshot": {"type": "object"},
                        "events": {"type": "array"}
                    },
                    "required": ["initial_snapshot", "events"]
                }
            }]
        }
    elif method == "tools/call":
        params = req.get("params", {})
        if params.get("name") == "replay_event_sourcing_stream":
            args = params.get("arguments", {})
            res = EventSourcingLedgerEngine.replay_events(
                args.get("initial_snapshot", {}),
                args.get("events", [])
            )
            return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
    return {"error": "Method not found"}

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(handle_request(json.loads(line))))
            sys.stdout.flush()

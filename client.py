"""Event Sourcing Append-Only Ledger & Snapshot Replayer.
100% Python Standard Library.
"""

class EventSourcingLedgerEngine:
    """Manages immutable append-only event streams and rehydrates state from snapshots."""

    @staticmethod
    def replay_events(initial_snapshot: dict, events: list) -> dict:
        state = dict(initial_snapshot)
        applied_count = 0

        for evt in sorted(events, key=lambda x: int(x.get("version", 0))):
            evt_type = evt.get("event_type")
            payload = evt.get("payload", {})
            if evt_type == "ITEM_ADDED":
                state.setdefault("items", []).append(payload.get("item"))
            elif evt_type == "STATUS_UPDATED":
                state["status"] = payload.get("status")
            elif evt_type == "BALANCE_ADJUSTED":
                state["balance"] = state.get("balance", 0.0) + float(payload.get("amount", 0.0))
            applied_count += 1

        return {
            "rehydrated_state": state,
            "events_applied": applied_count,
            "final_version": events[-1].get("version", 0) if events else 0
        }

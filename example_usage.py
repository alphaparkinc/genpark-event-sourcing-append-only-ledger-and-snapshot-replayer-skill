"""Example usage for Event Sourcing Ledger Engine."""
from client import EventSourcingLedgerEngine

if __name__ == "__main__":
    res = EventSourcingLedgerEngine.replay_events(
        {"balance": 100.0, "status": "ACTIVE"},
        [
            {"version": 1, "event_type": "BALANCE_ADJUSTED", "payload": {"amount": 50.0}},
            {"version": 2, "event_type": "STATUS_UPDATED", "payload": {"status": "VIP"}}
        ]
    )
    print("Final State:", res["rehydrated_state"])

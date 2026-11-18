"""In-memory demo store with reset support and idempotent follow-up creation."""

from __future__ import annotations

from copy import deepcopy
from threading import RLock

from .data import CUSTOMERS, TICKETS


class DemoStore:
    def __init__(self) -> None:
        self._lock = RLock()
        self.reset()

    def reset(self) -> None:
        with self._lock:
            self.customers = deepcopy(CUSTOMERS)
            self.tickets = deepcopy(TICKETS)
            self.followups: dict[str, dict[str, object]] = {}
            self._idempotency: dict[str, str] = {}

    def list_customers(self, priority: str | None = None) -> list[dict[str, object]]:
        with self._lock:
            rows = self.customers
            if priority:
                rows = [row for row in rows if row["priority"] == priority]
            return deepcopy(rows)

    def get_customer(self, customer_id: str) -> dict[str, object] | None:
        with self._lock:
            row = next((x for x in self.customers if x["id"] == customer_id), None)
            return deepcopy(row) if row else None

    def create_followup(
        self, customer_id: str, title: str, idempotency_key: str
    ) -> tuple[dict[str, object], bool]:
        with self._lock:
            if customer_id not in {x["id"] for x in self.customers}:
                raise KeyError(customer_id)
            existing_id = self._idempotency.get(idempotency_key)
            if existing_id:
                return deepcopy(self.followups[existing_id]), False
            followup_id = f"FUP-{len(self.followups) + 1:05d}"
            item: dict[str, object] = {
                "id": followup_id,
                "customer_id": customer_id,
                "title": title,
                "status": "open",
            }
            self.followups[followup_id] = item
            self._idempotency[idempotency_key] = followup_id
            return deepcopy(item), True

    def list_tickets(self) -> list[dict[str, object]]:
        with self._lock:
            return deepcopy(self.tickets)

    def list_followups(self) -> list[dict[str, object]]:
        with self._lock:
            return deepcopy(list(self.followups.values()))


store = DemoStore()

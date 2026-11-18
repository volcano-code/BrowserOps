"""Deterministic CRM and ticket fixtures for reproducible browser tasks."""

from __future__ import annotations

from datetime import date, timedelta

CUSTOMERS: list[dict[str, object]] = [
    {
        "id": f"CUST-{i:04d}",
        "name": f"Customer {i:04d}",
        "email": f"customer{i:04d}@example.test",
        "priority": "high" if i % 5 == 0 else ("medium" if i % 2 == 0 else "low"),
        "status": "active" if i % 7 else "inactive",
        "owner": f"sales-{(i % 4) + 1}",
        "last_contact": (date(2026, 11, 18) - timedelta(days=(i * 3) % 75)).isoformat(),
    }
    for i in range(1, 101)
]

TICKETS: list[dict[str, object]] = [
    {
        "id": f"TKT-{i:04d}",
        "customer_id": f"CUST-{((i - 1) % 100) + 1:04d}",
        "title": f"Support request {i:04d}",
        "priority": "high" if i % 6 == 0 else "normal",
        "status": "open" if i % 3 else "closed",
    }
    for i in range(1, 61)
]

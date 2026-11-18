"""FastAPI application for the local BrowserOps demo SaaS."""

from __future__ import annotations

from typing import Annotated

from fastapi import FastAPI, Header, HTTPException, Query
from pydantic import BaseModel, Field

from .store import store

app = FastAPI(title="BrowserOps Demo SaaS", version="0.1.0")


class FollowupCreate(BaseModel):
    customer_id: str = Field(min_length=1)
    title: str = Field(min_length=3, max_length=160)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "browserops-demo-saas"}


@app.get("/crm/customers")
def customers(priority: Annotated[str | None, Query()] = None) -> dict[str, object]:
    if priority and priority not in {"low", "medium", "high"}:
        raise HTTPException(status_code=422, detail="invalid priority")
    rows = store.list_customers(priority)
    return {"items": rows, "count": len(rows)}


@app.get("/crm/customers/{customer_id}")
def customer(customer_id: str) -> dict[str, object]:
    row = store.get_customer(customer_id)
    if row is None:
        raise HTTPException(status_code=404, detail="customer not found")
    return row


@app.get("/tickets")
def tickets() -> dict[str, object]:
    rows = store.list_tickets()
    return {"items": rows, "count": len(rows)}


@app.get("/followups")
def followups() -> dict[str, object]:
    rows = store.list_followups()
    return {"items": rows, "count": len(rows)}


@app.post("/followups", status_code=201)
def create_followup(
    payload: FollowupCreate,
    idempotency_key: Annotated[str, Header(alias="Idempotency-Key", min_length=8)],
) -> dict[str, object]:
    try:
        item, created = store.create_followup(
            payload.customer_id, payload.title, idempotency_key
        )
    except KeyError as exc:
        raise HTTPException(status_code=404, detail="customer not found") from exc
    return {"item": item, "created": created}


@app.post("/__test__/reset")
def reset() -> dict[str, str]:
    """Reset fixtures. Bind this endpoint to localhost in non-test deployments."""
    store.reset()
    return {"status": "reset"}

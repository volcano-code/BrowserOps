"""Thin, explicitly non-sandboxed adapter for the upstream Browser Use baseline.

This adapter is for controlled local evaluation only. Browser Use 1.0 executes Python
inside a persistent REPL; a domain allowlist is not an operating-system sandbox.
Never pass untrusted tasks or host secrets to this adapter.
"""

from __future__ import annotations

from typing import Any

from .upstream import verify_upstream_version


def create_local_browser() -> Any:
    """Create a fresh local Chromium browser, never the default cloud browser."""
    verify_upstream_version()
    from browser_use import Browser

    return Browser("chromium")


def create_agent(task: str, llm: Any) -> Any:
    """Create a Browser Use baseline agent with an explicitly local browser."""
    if not task.strip():
        raise ValueError("task must not be empty")
    verify_upstream_version()
    from browser_use import Agent

    return Agent(task=task, llm=llm, browser=create_local_browser())

"""Upstream Browser Use provenance and compatibility checks."""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version

UPSTREAM_DISTRIBUTION = "browser-use"
UPSTREAM_VERSION = "1.0.4"
UPSTREAM_COMMIT = "480d0bd508ce10dcf27a4716f2f87355a08e8372"
UPSTREAM_REPOSITORY = "https://github.com/browser-use/browser-use"


def installed_upstream_version() -> str:
    """Return the installed Browser Use distribution version."""
    try:
        return version(UPSTREAM_DISTRIBUTION)
    except PackageNotFoundError as exc:
        raise RuntimeError(
            "Browser Use is not installed. Run 'uv sync --dev' from the repository root."
        ) from exc


def verify_upstream_version() -> str:
    """Fail closed unless the exact upstream baseline is installed."""
    installed = installed_upstream_version()
    if installed != UPSTREAM_VERSION:
        raise RuntimeError(
            f"Unsupported Browser Use version {installed!r}; "
            f"this baseline requires exactly {UPSTREAM_VERSION!r}."
        )
    return installed

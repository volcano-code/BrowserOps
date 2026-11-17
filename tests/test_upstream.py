from importlib.metadata import PackageNotFoundError
from unittest.mock import patch

import pytest

from browserops_core import upstream


def test_upstream_pin_is_explicit() -> None:
    assert upstream.UPSTREAM_VERSION == "1.0.4"
    assert upstream.UPSTREAM_COMMIT == "480d0bd508ce10dcf27a4716f2f87355a08e8372"


def test_verify_upstream_version_accepts_exact_pin() -> None:
    with patch.object(upstream, "installed_upstream_version", return_value="1.0.4"):
        assert upstream.verify_upstream_version() == "1.0.4"


def test_verify_upstream_version_rejects_drift() -> None:
    with patch.object(upstream, "installed_upstream_version", return_value="1.0.5"):
        with pytest.raises(RuntimeError, match="requires exactly"):
            upstream.verify_upstream_version()


def test_missing_distribution_has_actionable_error() -> None:
    with patch(
        "browserops_core.upstream.version",
        side_effect=PackageNotFoundError("browser-use"),
    ):
        with pytest.raises(RuntimeError, match="uv sync --dev"):
            upstream.installed_upstream_version()

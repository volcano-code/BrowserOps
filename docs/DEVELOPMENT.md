# Development guide

## Requirements

- Linux x86_64 recommended for the target development environment.
- Python 3.12 and uv.
- Google Chrome or Chromium for local browser smoke tests.
- Docker/Podman will be introduced for isolated execution in a later phase.

## Setup

```bash
git clone git@github.com:volcano-code/BrowserOps.git
cd BrowserOps
git switch browserops/phase0-1
uv sync --dev
uv run pytest -q
uv run ruff check .
uv run pyright
```

## Baseline test policy

Normal CI must not call a paid model API, create a cloud browser, or require a Browser Use
Cloud API key. The first tests only check the pinned distribution and provenance guard.

## Local Chromium smoke test

This optional smoke test creates a local Chromium instance explicitly. It does not use the
default Browser Use Cloud browser. It requires a valid model provider configuration and
may incur model charges.

```bash
export BROWSEROPS_MODEL_NAME='your-model-name'
export BROWSEROPS_MODEL_BASE_URL='https://your-compatible-endpoint/v1'
export BROWSEROPS_MODEL_API_KEY='your-key'
uv run python scripts/smoke_browser_use.py --url https://example.com
```

Only run this against a site you are authorized to access. Browser Use 1.0 executes Python
in a persistent REPL and is not a security sandbox. Do not use it for untrusted tasks or
with host credentials. The controlled executor and sandbox are not implemented yet.

See `.env.example` for the optional smoke-test configuration.

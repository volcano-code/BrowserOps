# BrowserOps

**A secure, reliable, and verifiable enterprise browser-agent platform.**

BrowserOps is a downstream integration project built around the pinned upstream
[Browser Use](https://github.com/browser-use/browser-use) engine. It adds a controlled
execution layer, policy enforcement, independent verification, durable task execution,
and a reproducible evaluation suite.

> **Current status:** Phase 0–1 foundation. No production execution, sandbox isolation,
> model-provider call, or benchmark result is claimed yet.

## Upstream baseline

- Upstream: https://github.com/browser-use/browser-use
- Version: `1.0.4`
- Commit: `480d0bd508ce10dcf27a4716f2f87355a08e8372`
- License: MIT (upstream license and attribution are retained in `THIRD_PARTY_NOTICES.md`)

BrowserOps does not vendor or silently rewrite the upstream source. It pins the upstream
package and builds its own adapters and controlled runtime around it.

## Development

The repository targets Python 3.12 and uses `uv`.

```bash
uv sync --dev
uv run pytest -q
uv run ruff check .
uv run pyright
```

See [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md) for Linux setup and the local Chromium smoke test.

## Safety boundary

The upstream Browser Use 1.0 agent runs Python in a persistent REPL. A domain allowlist is
not a sandbox. Do not run untrusted tasks or expose host credentials to that process.
The controlled Playwright executor and isolated sandbox are planned as separate components;
they are not implemented in this foundation commit.

## Roadmap

- Phase 0: repository, provenance, scope, development conventions.
- Phase 1: reproducible Python environment and upstream baseline.
- Phase 2+: Demo SaaS, durable runtime, controlled actions, policy engine, verifier, UI,
  OpsBench, security and reliability evaluation.

See [docs/ROADMAP.md](docs/ROADMAP.md).

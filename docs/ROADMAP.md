# BrowserOps roadmap

## Phase 0 — repository and provenance

- [x] Create downstream repository.
- [x] Pin Browser Use 1.0.4 and record upstream commit.
- [x] Preserve upstream MIT notice.
- [x] Define scope and safety boundary.
- [ ] Local clone and baseline environment verification.

## Phase 1 — reproducible baseline

- [x] Add Python 3.12 project configuration.
- [x] Add strict upstream version guard.
- [x] Add thin local Chromium baseline adapter.
- [x] Add no-provider unit tests and CI workflow.
- [ ] Run baseline tests on the user's Linux/RTX 5090 workstation.
- [ ] Run authorized local Chromium smoke test with a configured model.

## Phase 2 — Demo SaaS and OpsBench

- [ ] Build resettable CRM/ticketing demo application.
- [ ] Add deterministic seed data and task fixtures.
- [ ] Add independent task graders and held-out split.

## Phase 3 — backend and durable runtime

- [ ] FastAPI, PostgreSQL, migrations, worker leases and transactional outbox.
- [ ] Task/run/event/artifact/evidence data model.

## Phase 4 — controlled browser execution

- [ ] Structured action schema and validator.
- [ ] Playwright executor.
- [ ] Browser context isolation and artifact capture.

## Phase 5 — policy and sandbox

- [ ] Domain and network egress policy.
- [ ] Rootless sandbox manager and resource limits.
- [ ] Secret isolation and redaction.
- [ ] Approval policy for side effects.

## Phase 6 — verification and reliability

- [ ] Independent postcondition verifier.
- [ ] Operation ledger and idempotency.
- [ ] Checkpoint, cancellation and crash recovery.

## Phase 7 — frontend and observability

- [ ] Next.js workbench.
- [ ] Live run events, approval center and evidence viewer.
- [ ] OpenTelemetry traces and metrics.

## Phase 8 — evaluation and release

- [ ] Browser Use baseline comparison.
- [ ] OpsBench, security red-team and failure injection.
- [ ] Ablations, reproducible report and Docker deployment.

## Phase 9 — optional learning

- [ ] Trajectory collection and quality filtering.
- [ ] SFT/LoRA experiment.
- [ ] Agent Lightning integration only after reliable task grading exists.

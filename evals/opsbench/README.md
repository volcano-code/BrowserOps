# OpsBench v0

OpsBench is a deterministic task fixture and grading harness for BrowserOps. This first
increment defines the dataset contract and a small seed suite. It is not yet the planned
130-task benchmark and no agent success-rate claim is made.

## Task contract

Each task fixture contains:
- stable task ID and category;
- natural-language instruction;
- reset preconditions;
- expected postconditions;
- risk class;
- grader identifier.

## Current seed tasks

The JSON file contains read-only customer lookup and idempotent follow-up creation tasks.
The evaluation runner validates task structure and checks the demo SaaS state through its
read-only API. Browser automation integration is a later milestone.

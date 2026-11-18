"""Validate OpsBench task fixture structure without invoking an agent."""

from __future__ import annotations

import json
from pathlib import Path

REQUIRED = {"task_id", "category", "instruction", "risk", "expected", "grader"}
ALLOWED_RISKS = {"R0", "R1", "R2", "R3"}


def validate_tasks(path: Path) -> list[dict[str, object]]:
    tasks = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(tasks, list):
        raise ValueError("task fixture root must be a list")
    seen: set[str] = set()
    for index, task in enumerate(tasks):
        if not isinstance(task, dict):
            raise ValueError(f"task at index {index} must be an object")
        missing = REQUIRED - task.keys()
        if missing:
            raise ValueError(f"task at index {index} missing: {sorted(missing)}")
        task_id = task["task_id"]
        if not isinstance(task_id, str) or not task_id:
            raise ValueError(f"task at index {index} has invalid task_id")
        if task_id in seen:
            raise ValueError(f"duplicate task_id: {task_id}")
        seen.add(task_id)
        if task["risk"] not in ALLOWED_RISKS:
            raise ValueError(f"task {task_id} has invalid risk")
    return tasks


if __name__ == "__main__":
    fixture = Path(__file__).with_name("tasks.v0.json")
    print(f"validated {len(validate_tasks(fixture))} OpsBench task fixtures")

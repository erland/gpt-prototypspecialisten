#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
import sys
import yaml

REQUIRED_MODEL_IDS = {
    "resume-state",
    "validation-gate",
    "browser-fallback",
    "responsive-core",
    "model-idea-input",
    "model-screenshot-input",
    "model-url-input",
    "model-form-error",
    "model-runtime-parity",
}
REQUIRED_CATEGORIES = {
    "idea_input",
    "screenshot_input",
    "url_input",
    "responsive_translation",
    "forms_and_errors",
}


def load_yaml(path: Path) -> dict:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"Eval must be a mapping: {path}")
    if not data.get("id"):
        raise ValueError(f"Eval missing id: {path}")
    return data


def validate(root: Path) -> None:
    eval_root = root / "evals"
    files = sorted(eval_root.rglob("*.yaml"))
    if not files:
        raise ValueError("EVAL-COVERAGE-001: no eval scenarios found")

    seen_ids: set[str] = set()
    categories: set[str] = set()
    model_ids: set[str] = set()

    for path in files:
        data = load_yaml(path)
        eval_id = str(data["id"])
        if eval_id in seen_ids:
            raise ValueError(f"EVAL-COVERAGE-002: duplicate eval id: {eval_id}")
        seen_ids.add(eval_id)
        if data.get("category"):
            categories.add(str(data["category"]))
        if "model-compatibility" in path.parts:
            model_ids.add(eval_id)
            if not data.get("purpose") or not data.get("input") or not data.get("expected"):
                raise ValueError(f"EVAL-COVERAGE-003: incomplete model scenario: {path}")

    missing_model = sorted(REQUIRED_MODEL_IDS - model_ids)
    if missing_model:
        raise ValueError("EVAL-COVERAGE-004: missing model scenarios: " + ", ".join(missing_model))

    missing_categories = sorted(REQUIRED_CATEGORIES - categories)
    if missing_categories:
        raise ValueError("EVAL-COVERAGE-005: missing scenario categories: " + ", ".join(missing_categories))

    # Existing specialized suites are part of the contract as well.
    for suite in ("workflow", "preview", "codegen", "validation", "distribution"):
        suite_dir = eval_root / suite
        if not suite_dir.is_dir() or not any(suite_dir.glob("*.yaml")):
            raise ValueError(f"EVAL-COVERAGE-006: required suite missing or empty: {suite}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--project-root", default=".")
    args = ap.parse_args()
    try:
        validate(Path(args.project_root).resolve())
    except (OSError, ValueError, yaml.YAMLError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    print("Eval coverage OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

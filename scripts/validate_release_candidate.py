#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    import yaml
except Exception as exc:
    raise SystemExit("PyYAML is required") from exc


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--project-root", default=".")
    ap.add_argument("--version", required=True)
    args = ap.parse_args()

    root = Path(args.project_root).resolve()
    status = yaml.safe_load((root / "project-status.yaml").read_text(encoding="utf-8"))
    errors: list[str] = []

    if status.get("state", {}).get("blocking_issues"):
        errors.append("RC-001: blocking issues remain")
    if status.get("state", {}).get("warnings"):
        errors.append("RC-002: warnings remain")
    if status.get("validation", {}).get("last_result") != "pass":
        errors.append("RC-003: validation.last_result must be pass")
    if status.get("project_hygiene", {}).get("last_result") != "pass":
        errors.append("RC-004: project_hygiene.last_result must be pass")
    if status.get("progress", {}).get("last_completed_step") != status.get("plan", {}).get("total_steps"):
        errors.append("RC-005: all planned steps must be completed")
    next_step = status.get("next_step") or {}
    if next_step.get("recommended") != "stable_release":
        errors.append("RC-006: approved RC must recommend stable_release as next step")
    if "-rc." not in args.version:
        errors.append("RC-007: version must be an explicit release candidate version")

    manifest_path = root / "dist" / "DELIVERY-MANIFEST.json"
    if not manifest_path.is_file():
        errors.append("RC-008: delivery manifest missing")
    else:
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            if manifest.get("version") != args.version:
                errors.append("RC-009: delivery manifest version mismatch")
        except Exception as exc:
            errors.append(f"RC-010: invalid delivery manifest: {exc}")

    if errors:
        print("RC READINESS: FAIL")
        for item in errors:
            print(f"- {item}")
        return 1
    print("RC READINESS: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

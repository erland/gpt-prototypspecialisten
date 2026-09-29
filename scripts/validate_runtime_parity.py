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


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def canonical_projection(contract: dict) -> dict:
    return {
        "capabilities": contract.get("capabilities"),
        "artifacts": contract.get("artifacts"),
        "workspace_state": contract.get("workspace_state"),
        "tools": contract.get("tools"),
    }


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    cfg = yaml.safe_load((root / "gpt-project.yaml").read_text(encoding="utf-8"))

    active = []
    runtime_cfg = cfg.get("runtime", {})
    if runtime_cfg.get("chat_zip", {}).get("enabled"):
        active.append(("chat", root / "build/chat/assistant/runtime-contract.json", "chatgpt_chat"))
    if runtime_cfg.get("custom_gpt", {}).get("enabled"):
        path = runtime_cfg["custom_gpt"].get("builder", {}).get("runtime_contract", "builder/runtime-contract.json")
        active.append(("custom_gpt", root / "build/custom-gpt" / path, "chatgpt_custom"))
    if runtime_cfg.get("opencode", {}).get("enabled"):
        path = runtime_cfg["opencode"]["layout"]["runtime_contract"]
        active.append(("opencode", root / "build/opencode" / path, "opencode"))

    if len(active) < 2:
        return ["PARITY-001: at least two active runtimes are required for parity validation"]

    loaded: dict[str, dict] = {}
    for name, path, expected_runtime_id in active:
        if not path.is_file():
            fail(errors, f"PARITY-002: missing runtime contract for {name}: {path.relative_to(root)}")
            continue
        try:
            contract = load_json(path)
        except Exception as exc:
            fail(errors, f"PARITY-003: invalid runtime contract for {name}: {exc}")
            continue
        if contract.get("runtime_id") != expected_runtime_id:
            fail(errors, f"PARITY-004: runtime_id mismatch for {name}")
        loaded[name] = contract

    if errors:
        return errors

    baseline_name = active[0][0]
    baseline = canonical_projection(loaded[baseline_name])
    for name, _, _ in active[1:]:
        current = canonical_projection(loaded[name])
        if current != baseline:
            fail(errors, f"PARITY-005: canonical contract mismatch between {baseline_name} and {name}")

    # All runtime packages must be built from the same canonical instruction markers.
    canonical = (root / cfg["instructions"]["canonical"]).read_text(encoding="utf-8")
    markers = list(cfg.get("instructions", {}).get("core_contract", {}).get("required_markers", []) or [])
    for marker in markers:
        if marker not in canonical:
            fail(errors, f"PARITY-006: canonical instruction is missing required marker: {marker}")

    chat_instr = root / "build/chat/assistant/instructions.md"
    custom_instr = root / "build/custom-gpt/builder/instructions.md"
    opencode_instr = root / "build/opencode/AGENTS.md"
    for name, path in [("chat", chat_instr), ("custom_gpt", custom_instr), ("opencode", opencode_instr)]:
        if not path.is_file():
            fail(errors, f"PARITY-007: missing compiled instruction for {name}")
            continue
        text = path.read_text(encoding="utf-8")
        for marker in markers:
            if marker not in text:
                fail(errors, f"PARITY-008: {name} compiled instruction missing core marker: {marker}")

    return errors


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--project-root", default=".")
    args = ap.parse_args()
    errors = validate(Path(args.project_root).resolve())
    if errors:
        print("RUNTIME PARITY: FAIL")
        for item in errors:
            print(f"- {item}")
        return 1
    print("RUNTIME PARITY: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

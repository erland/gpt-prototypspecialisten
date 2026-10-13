#!/usr/bin/env python3
"""Validate all configured distributions against canonical behavior markers."""
from __future__ import annotations
import argparse
from pathlib import Path
import zipfile
import yaml

PATHS = {"chat": "assistant/instructions.md", "opencode": "AGENTS.md", "claude-project": "project/instructions.md"}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", default=".")
    args = parser.parse_args()
    root = Path(args.project_root)
    cfg = yaml.safe_load((root / "gpt-project.yaml").read_text(encoding="utf-8"))
    markers = cfg["instructions"]["core_contract"]["required_markers"]
    skills = [s["id"] for s in cfg["skills"]["definitions"]]
    errors = []
    from importlib.util import spec_from_file_location, module_from_spec
    source = root / "tooling/gpt-byggaren-1.6.21/scripts/lib/canonical_skill_sources.py"
    spec = spec_from_file_location("canonical_sources_parity", source)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    canonical = module.projected_instruction(root, cfg, cfg["skills"]["definitions"])
    for marker in markers:
        if marker not in canonical:
            errors.append(f"Canonical instruction missing: {marker}")
    dist = root / "dist"
    for runtime in ("chat", "plugin", "opencode", "claude-project", "claude-skills"):
        matches = list(dist.glob(f"prototypspecialisten-{runtime}-*.zip"))
        if len(matches) != 1:
            errors.append(f"{runtime}: expected one archive, found {len(matches)}")
            continue
        with zipfile.ZipFile(matches[0]) as z:
            files = z.namelist()
            if runtime in ("plugin", "claude-skills"):
                required = [f"skills/{skill}/SKILL.md" for skill in skills]
            else:
                required = [PATHS[runtime]]
            missing = [path for path in required if path not in files]
            errors.extend(f"{runtime}: missing {path}" for path in missing)
            content = "\n".join(z.read(path).decode("utf-8") for path in required if path in files)
            for marker in markers:
                if marker not in content:
                    errors.append(f"{runtime}: missing marker {marker}")
    print("RUNTIME PARITY:", "FAIL" if errors else "PASS")
    for error in errors:
        print("-", error)
    return int(bool(errors))

if __name__ == "__main__":
    raise SystemExit(main())

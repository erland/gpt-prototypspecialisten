#!/usr/bin/env python3
"""Verify all five generated runtime bundles preserve canonical behavioral markers."""
from __future__ import annotations
import argparse
from pathlib import Path
import zipfile
import yaml

PATHS = {
    "chat": "assistant/instructions.md",
    "plugin": "skills/prototypspecialisten/SKILL.md",
    "opencode": "AGENTS.md",
    "claude-project": "instructions.md",
    "claude-skills": "skills/prototypspecialisten/SKILL.md",
}

def main():
    p=argparse.ArgumentParser(); p.add_argument('--project-root',default='.')
    a=p.parse_args(); root=Path(a.project_root); cfg=yaml.safe_load((root/'gpt-project.yaml').read_text())
    markers=cfg['instructions']['core_contract']['required_markers']
    canonical=(root/cfg['instructions']['canonical']).read_text()
    errors=[f'Canonical instruction missing: {m}' for m in markers if m not in canonical]
    files=list((root/'dist').glob('prototypspecialisten-*.zip'))
    for runtime, path in PATHS.items():
        matches=[f for f in files if f.name.startswith('prototypspecialisten-'+runtime+'-')]
        if len(matches)!=1: errors.append(f'{runtime}: expected exactly one archive, found {len(matches)}');continue
        with zipfile.ZipFile(matches[0]) as z:
            if path not in z.namelist():
                candidates=[x for x in z.namelist() if x.endswith(path)]
                if not candidates:errors.append(f'{runtime}: missing {path}');continue
                path=candidates[0]
            content=z.read(path).decode()
            for marker in markers:
                if marker not in content:errors.append(f'{runtime}: missing marker {marker}')
    print('RUNTIME PARITY:', 'FAIL' if errors else 'PASS')
    for e in errors: print('-',e)
    return int(bool(errors))
if __name__=='__main__':raise SystemExit(main())

#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import yaml


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--project-root', default='.')
    ap.add_argument('--version', required=True)
    ap.add_argument('--mode', choices=['ci', 'release'], default='release')
    args = ap.parse_args()

    root = Path(args.project_root).resolve()
    cfg = yaml.safe_load((root / 'gpt-project.yaml').read_text(encoding='utf-8'))
    status = yaml.safe_load((root / 'project-status.yaml').read_text(encoding='utf-8'))
    errors: list[str] = []

    if status.get('state', {}).get('blocking_issues'):
        errors.append('RR-001: blocking issues remain')
    if status.get('state', {}).get('warnings'):
        errors.append('RR-002: project status contains warnings')
    if status.get('validation', {}).get('last_result') != 'pass':
        errors.append('RR-003: validation.last_result must be pass')
    if status.get('project_hygiene', {}).get('last_result') != 'pass':
        errors.append('RR-004: project_hygiene.last_result must be pass')

    if not cfg.get('ci', {}).get('enabled'):
        errors.append('RR-005: CI must be enabled')
    if not cfg.get('release', {}).get('github', {}).get('enabled'):
        errors.append('RR-006: GitHub release build must be enabled')

    for rel in [cfg.get('ci', {}).get('workflow'), cfg.get('release', {}).get('github', {}).get('workflow')]:
        if not rel or not (root / rel).is_file():
            errors.append(f'RR-007: configured workflow missing: {rel}')

    dist = root / 'dist'
    manifest_path = dist / 'DELIVERY-MANIFEST.json'
    sums_path = dist / 'SHA256SUMS.txt'
    if not manifest_path.is_file():
        errors.append('RR-008: DELIVERY-MANIFEST.json missing')
    if not sums_path.is_file():
        errors.append('RR-009: SHA256SUMS.txt missing')

    manifest = None
    if manifest_path.is_file():
        try:
            manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
        except Exception as exc:
            errors.append(f'RR-010: invalid delivery manifest: {exc}')
        else:
            if manifest.get('version') != args.version:
                errors.append('RR-011: delivery manifest version mismatch')

    expected_files = [f"{cfg['project']['id']}-project.zip"]
    for target in cfg.get('build_system', {}).get('targets', []):
        if target == 'project':
            continue
        rt = cfg.get('build_system', {}).get('runtime_targets', {}).get(target)
        if not rt:
            errors.append(f'RR-012: build target lacks runtime target config: {target}')
            continue
        runtime_cfg = cfg.get('runtime', {}).get(rt['runtime_key'], {})
        if runtime_cfg.get('enabled'):
            expected_files.append(rt['filename_pattern'].replace('<project-id>', cfg['project']['id']).replace('<version>', args.version))

    for name in expected_files:
        if not (dist / name).is_file():
            errors.append(f'RR-013: expected release artifact missing: {name}')

    if sums_path.is_file():
        parsed = {}
        for line in sums_path.read_text(encoding='utf-8').splitlines():
            if not line.strip():
                continue
            digest, name = line.split(None, 1)
            parsed[name.strip()] = digest
        for name in expected_files:
            p = dist / name
            if p.is_file() and parsed.get(name) != sha256(p):
                errors.append(f'RR-014: checksum mismatch or missing for {name}')

    if manifest is not None:
        manifest_files = {item.get('file') for item in manifest.get('artifacts', [])}
        for name in expected_files + ['SHA256SUMS.txt']:
            if name not in manifest_files:
                errors.append(f'RR-015: delivery manifest missing artifact: {name}')

    if args.mode == 'release' and args.version == '0.0.0-ci':
        errors.append('RR-016: release mode cannot use CI version')

    if errors:
        print('RELEASE READINESS: BLOCKED')
        for error in errors:
            print(f'- {error}')
        return 1

    print('RELEASE READINESS: READY')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

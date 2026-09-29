from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]


def load_cfg():
    return yaml.safe_load((ROOT / 'gpt-project.yaml').read_text(encoding='utf-8'))


def test_github_ci_and_release_are_enabled_and_present():
    cfg = load_cfg()
    assert cfg['ci']['enabled'] is True
    assert cfg['release']['github']['enabled'] is True
    assert (ROOT / cfg['ci']['workflow']).is_file()
    assert (ROOT / cfg['release']['github']['workflow']).is_file()


def test_all_enabled_runtimes_are_build_targets():
    cfg = load_cfg()
    selected = set(cfg['build_system']['targets'])
    targets = cfg['build_system']['runtime_targets']
    for target, meta in targets.items():
        runtime_cfg = cfg['runtime'][meta['runtime_key']]
        if runtime_cfg.get('enabled'):
            assert target in selected


def test_release_workflow_is_tag_driven_and_uploads_manifest():
    cfg = load_cfg()
    text = (ROOT / cfg['release']['github']['workflow']).read_text(encoding='utf-8')
    assert 'github.event.release.tag_name' in text
    assert 'gh release upload' in text
    assert 'dist/DELIVERY-MANIFEST.json' in text
    assert 'dist/SHA256SUMS.txt' in text


def test_ci_uses_non_release_version_and_all_configured_targets():
    cfg = load_cfg()
    text = (ROOT / cfg['ci']['workflow']).read_text(encoding='utf-8')
    assert '--version 0.0.0-ci' in text
    # No explicit --targets means build_distributions uses build_system.targets.
    assert 'build_distributions.py --project-root . --version 0.0.0-ci' in text
    assert '--targets' not in text


def test_approved_rc_recommends_stable_release():
    status = yaml.safe_load((ROOT / 'project-status.yaml').read_text(encoding='utf-8'))
    assert status['release']['status'] == 'release_candidate'
    assert status['next_step']['recommended'] == 'stable_release'

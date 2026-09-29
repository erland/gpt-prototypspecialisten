from pathlib import Path
import json
import yaml
from jsonschema import validate

ROOT = Path(__file__).resolve().parents[1]


def test_all_yaml_and_json_source_files_parse():
    excluded = {'build', 'dist'}
    for path in ROOT.rglob('*'):
        if not path.is_file() or any(part in excluded for part in path.relative_to(ROOT).parts):
            continue
        if path.suffix in {'.yaml', '.yml'}:
            yaml.safe_load(path.read_text(encoding='utf-8'))
        elif path.suffix == '.json':
            json.loads(path.read_text(encoding='utf-8'))


def test_project_status_matches_schema():
    schema = json.loads((ROOT / 'schemas/project-status.schema.json').read_text(encoding='utf-8'))
    data = yaml.safe_load((ROOT / 'project-status.yaml').read_text(encoding='utf-8'))
    validate(instance=data, schema=schema)

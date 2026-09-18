#!/usr/bin/env python3
"""Validate CodeFoundry's testable-unit package structure."""
from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parents[2]
errors=[]
for required in ['SKILL.md','MANIFEST.json','README.md','AGENTS','COUNCILS','DEPARTMENTS','SHARED','TESTING']:
    if not (ROOT/required).exists(): errors.append(f'missing {required}')
for base in ['AGENTS','COUNCILS']:
    for p in (ROOT/base).iterdir():
        if p.is_dir() and not (p/'UNIT.json').exists(): errors.append(f'{p.relative_to(ROOT)} missing UNIT.json')
for p in list((ROOT/'AGENTS').glob('*/UNIT.json'))+list((ROOT/'COUNCILS').glob('*/UNIT.json')):
    try: d=json.loads(p.read_text())
    except Exception as e: errors.append(f'{p}: invalid JSON: {e}'); continue
    if d.get('unit_type') not in {'agent','council'}: errors.append(f'{p}: invalid unit_type')
# Departments are independently-packaged sub-organizations, each with its
# own internal structure (Developer_Organization's UNIT.json-based
# capabilities; QA_Organization's own constitution/engine, not UNIT.json-
# based at all) — validated only for presence and a README, not forced
# into the AGENTS/COUNCILS unit schema.
for dept in ['Developer_Organization', 'QA_Organization']:
    d = ROOT/'DEPARTMENTS'/dept
    if not d.exists(): errors.append(f'missing DEPARTMENTS/{dept}')
    elif not (d/'README.md').exists(): errors.append(f'DEPARTMENTS/{dept} missing README.md')
for p in (ROOT/'DEPARTMENTS/Developer_Organization/CAPABILITIES').iterdir() if (ROOT/'DEPARTMENTS/Developer_Organization/CAPABILITIES').exists() else []:
    if p.is_dir() and not (p/'UNIT.json').exists(): errors.append(f'{p.relative_to(ROOT)} missing UNIT.json')
if not (ROOT/'COUNCILS/Pre-Planning/roles').exists(): errors.append('missing Pre-Planning roles')
if len(list((ROOT/'COUNCILS/Design-Council/roles').glob('*.md'))) != 7: errors.append('Design Council must contain 7 role files')
# Legacy operational paths must not survive in markdown except explicit source-gap/history language.
legacy=[]
for p in ROOT.rglob('*.md'):
    if 'DEPARTMENTS/QA_Organization' in str(p.relative_to(ROOT)): continue  # its own independent repo, not this package's operational paths
    t=p.read_text(encoding='utf-8')
    for token in ['`agents/','`workers/','`design-council/']:
        if token in t: legacy.append(str(p.relative_to(ROOT)))
if legacy: errors.append('legacy operational paths found: '+', '.join(sorted(set(legacy))))
if errors:
    print('FAIL'); [print(' -',e) for e in errors]; sys.exit(1)
print('PASS: CodeFoundry package structure and unit boundaries are valid.')

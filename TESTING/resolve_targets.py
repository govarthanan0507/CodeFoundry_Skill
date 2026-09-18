#!/usr/bin/env python3
"""Resolve one or more CodeFoundry test targets into a machine-readable plan.

This is intentionally model-provider agnostic. It establishes the test boundary;
a future runner can consume the emitted JSON and execute the actual benchmark.
"""
from pathlib import Path
import argparse, json, sys

ap=argparse.ArgumentParser(description='Resolve CodeFoundry test unit folders')
ap.add_argument('targets', nargs='+', help='One or more agent/council/worker directories')
ap.add_argument('--json', action='store_true', dest='as_json')
a=ap.parse_args()
root=Path(__file__).resolve().parents[1]
items=[]
for raw in a.targets:
    p=Path(raw).resolve()
    manifest=p/'UNIT.json'
    if not manifest.exists():
        print(f'ERROR: {p} has no UNIT.json', file=sys.stderr); sys.exit(2)
    d=json.loads(manifest.read_text(encoding='utf-8'))
    items.append({'path':str(p),'name':d.get('name'),'unit_type':d.get('unit_type'),'entrypoint':d.get('entrypoint'),'members':d.get('members',[]),'status':d.get('status','ready')})
plan={'schema_version':'1.0','targets':items,'comparison':len(items)>1,'evaluation_contract':str(root/'TESTING/AGENT_EVALUATION_CONTRACT.md')}
if a.as_json:
    print(json.dumps(plan,indent=2))
else:
    print(f"Targets: {len(items)} | matched comparison: {'YES' if len(items)>1 else 'NO'}")
    for i,x in enumerate(items,1):
        print(f"{i}. {x['name']} [{x['unit_type']}] — {x['path']}")
        if x['unit_type']=='council': print(f"   atomic council bundle; internal members: {len(x['members'])}")
        if x['status']!='ready': print(f"   STATUS: {x['status']}")

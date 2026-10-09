import json
from pathlib import Path
import xml_namespace_contract as m
p=json.loads(Path('contract.json').read_text());good=m.audit(Path('feed.xml').read_bytes(),p);bad=m.audit(Path('bad-feed.xml').read_bytes(),p)
assert not good['findings'] and bad['findings']
print(json.dumps({'good':good,'violation':bad},indent=2))

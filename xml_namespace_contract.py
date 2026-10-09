"""Prefix-invariant XML path cardinality and attribute contracts, without XSD."""
import argparse
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path


def name(value):
    if not isinstance(value, str) or not re.fullmatch(r'(?:\{[^{}]+\})?[A-Za-z_][A-Za-z0-9_.-]*', value):
        raise ValueError('names require Clark notation or plain ASCII local names')
    return value


def contract(p):
    if not isinstance(p, dict) or set(p) != {'namespaces', 'rules'}:
        raise ValueError('contract needs only namespaces and rules')
    if not isinstance(p['namespaces'], list) or not all(isinstance(x, str) for x in p['namespaces']):
        raise ValueError('namespaces must be URI strings; empty string allows unqualified names')
    if not isinstance(p['rules'], list) or not 1 <= len(p['rules']) <= 1000:
        raise ValueError('one to 1000 rules required')
    paths = set()
    for r in p['rules']:
        if not isinstance(r, dict) or set(r)-{'path','min','max','required_attributes','unique_attribute'} or not {'path','min','max'} <= set(r):
            raise ValueError('invalid rule fields')
        if not isinstance(r['path'], list) or not 1 <= len(r['path']) <= 64:
            raise ValueError('path must contain one to 64 expanded names')
        path = tuple(name(x) for x in r['path'])
        if path in paths:
            raise ValueError('duplicate rule path')
        paths.add(path)
        if any(type(r[k]) is not int or r[k] < 0 for k in ('min','max')) or r['min'] > r['max']:
            raise ValueError('invalid count range')
        attrs = r.get('required_attributes', [])
        if not isinstance(attrs, list):
            raise ValueError('required_attributes must be a list')
        for a in attrs:
            name(a)
        if 'unique_attribute' in r:
            name(r['unique_attribute'])
    return p


def audit(data, p):
    p = contract(p)
    if not isinstance(data, bytes) or len(data) > 2*1024*1024:
        raise ValueError('input must be UTF-8 bytes within 2 MiB')
    text = data.decode('utf-8-sig')
    if '\x00' in text or re.search(r'<!\s*(?:DOCTYPE|ENTITY)\b', text, re.I):
        raise ValueError('DTD, entities and NUL bytes are unsupported')
    decl = re.match(r'\s*<\?xml\b([^?]*)\?>', text)
    if decl:
        enc = re.search(r'encoding\s*=\s*[\'"]([^\'"]+)', decl[1], re.I)
        if enc and enc[1].lower() not in ('utf-8', 'utf8'):
            raise ValueError('only UTF-8 XML is supported')
    try:
        root = ET.fromstring(text)
    except ET.ParseError as e:
        raise ValueError('malformed XML') from e
    matches = {tuple(r['path']): [] for r in p['rules']}
    findings = []
    todo = [(root, ())]
    count = 0
    while todo:
        elem, parent = todo.pop()
        path = parent + (elem.tag,)
        count += 1
        if count > 50000 or len(path) > 64:
            raise ValueError('element count or depth exceeds supported limit')
        for expanded in [elem.tag, *elem.attrib]:
            ns = expanded[1:].split('}',1)[0] if expanded.startswith('{') else ''
            if ns not in p['namespaces']:
                findings.append(dict(code='namespace', path=list(path), name=expanded))
        if path in matches:
            matches[path].append(elem)
        todo.extend((c, path) for c in reversed(list(elem)))
    for r in p['rules']:
        elems = matches[tuple(r['path'])]
        if not r['min'] <= len(elems) <= r['max']:
            findings.append(dict(code='count', path=r['path'], actual=len(elems), min=r['min'], max=r['max']))
        seen = set()
        unique = r.get('unique_attribute')
        for i, elem in enumerate(elems, 1):
            for a in set(r.get('required_attributes', []) + ([unique] if unique else [])):
                if a not in elem.attrib or elem.attrib[a] == '':
                    findings.append(dict(code='missing_attribute', path=r['path'], occurrence=i, attribute=a))
            if unique and unique in elem.attrib:
                value = elem.attrib[unique]
                if value in seen:
                    findings.append(dict(code='duplicate_attribute', path=r['path'], occurrence=i, attribute=unique))
                seen.add(value)
    return dict(elements=count, findings=findings)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('xml')
    ap.add_argument('contract')
    args = ap.parse_args()
    try:
        result = audit(Path(args.xml).read_bytes(), json.loads(Path(args.contract).read_text()))
        print(json.dumps(result, sort_keys=True))
        return int(bool(result['findings']))
    except (ValueError, UnicodeError, OSError) as e:
        print(json.dumps({'error': str(e)}))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())

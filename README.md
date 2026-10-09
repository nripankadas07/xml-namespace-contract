# xml-namespace-contract

Prefix-invariant XML namespace, path cardinality and attribute-identity contracts.

## Who and why

Data integration reviewers with small XML feeds and simple business delivery invariants. A harmless prefix rename should pass while namespace-URI drift, missing paths or duplicate identifiers should fail with inspectable paths.

Match absolute expanded-name paths, whole-document count ranges, required attributes and unique attribute values; report namespace and cardinality drift.

## Quickstart

Python 3.10+ and pip. Git source installation, no external-registry publication:

```sh
git clone https://github.com/nripankadas07/xml-namespace-contract.git
cd xml-namespace-contract
python -m venv .venv
# Unix: source .venv/bin/activate; Windows: .venv\Scripts\activate
python -m pip install .
xml-namespace-contract feed.xml contract.json
python demo.py
python verify.py
```

CLI JSON on stdout. Exit **0** passes/claims, **1** policy findings or authentication/replay rejection, **2** malformed/unsupported input or IO errors. For automation, inspect the JSON and exit status together. Help: `xml-namespace-contract --help`.

The fixture data is entirely synthetic. `demo.py` runs the example without installation and asserts a useful success and failure. `verify.py` additionally checks source tests, compilation and a fresh wheel installation in a temporary environment outside the source directory.

## Input and output

Read the checked-in fixture and policy JSON alongside `xml_namespace_contract.py`. Policies reject unknown keys and invalid types rather than silently defaulting. See [DEMO.md](DEMO.md) for exact commands, expected outcome and schema notes; [VALIDATION.md](VALIDATION.md) for measured checks; [RESEARCH.md](RESEARCH.md) for dated comparable evidence and limits.

## Scope and limits

Not XSD, Schematron or XPath. Paths are exact absolute child paths in Clark notation; counts/uniqueness are whole-document totals, not per-parent constraints. Unqualified attributes use empty namespace even under default namespaces. Local names restricted to an ASCII subset in contracts. UTF-8 only, at most 2 MiB, 50,000 elements, depth 64 and 1,000 rules. DTD/entity declarations rejected lexically, including comments containing such text; external resources never fetched. Parser is standard-library ElementTree, not a general untrusted-XML security sandbox. No output attribute values or text nodes.

## Support

[Support, contribution and security](SUPPORT.md). MIT license. No performance or superiority claim; existing established tools are preferable when you need their broader workflows.

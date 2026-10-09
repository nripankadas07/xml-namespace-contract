# Runnable example

Run `python demo.py`; it exercises the exact source API and fails if the intended positive/negative result changes. The installed CLI is separately exercised by `python verify.py` from outside the source directory.

Commands in `smoke.json` document the expected exit status for good, findings/replay and malformed-input cases. Snapshot files are synthetic and intentionally contain no credentials or private production data.

Match absolute expanded-name paths, whole-document count ranges, required attributes and unique attribute values; report namespace and cardinality drift.

Not XSD, Schematron or XPath. Paths are exact absolute child paths in Clark notation; counts/uniqueness are whole-document totals, not per-parent constraints. Unqualified attributes use empty namespace even under default namespaces. Local names restricted to an ASCII subset in contracts. UTF-8 only, at most 2 MiB, 50,000 elements, depth 64 and 1,000 rules. DTD/entity declarations rejected lexically, including comments containing such text; external resources never fetched. Parser is standard-library ElementTree, not a general untrusted-XML security sandbox. No output attribute values or text nodes.

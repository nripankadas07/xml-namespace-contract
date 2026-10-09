# Brief and comparable review — 9 October 2026

Observation: 9 October 2026, 06:34 UTC. Live connected GitHub queries `xml validation sort:stars; xml parser in:description sort:stars; xmlschema in:name sort:stars` sorted by stars, bounded result pages. Repository star counts fetched separately, with current default-branch code/docs/issues. Highest-star relevant comparable found: **leethomason/tinyxml2 (5,805)**. This is not an exhaustive global ranking; HTML-only parsers, unrelated extractors, mobile-only release automation and report-only tools were distinguished by workflow relevance. Stars are discovery signals, not reliability/performance measurements.

Actual user: Data integration reviewers with small XML feeds and simple business delivery invariants.

Painful task: A harmless prefix rename should pass while namespace-URI drift, missing paths or duplicate identifiers should fail with inspectable paths.

Smallest useful capability: Match absolute expanded-name paths, whole-document count ranges, required attributes and unique attribute values; report namespace and cardinality drift.

Acceptance: good synthetic fixture passes; confirmed contract violation produces actionable JSON/exit 1; malformed input produces exit 2; installed quickstart works outside source; core boundary/concurrency/format regressions pass; remote Python matrix passes before LIVE.

Evidence and demand: Demand for a small prefix-invariant business contract is inferred. Established tools already support XML validation and rich schemas; no claim that they cannot implement these rules. Need for this exact MVP is inferred, not an upstream request to build it.

Portfolio/distinctness: Existing GeoJSON/header/route contracts operate on other formats and semantics. This product handles expanded XML names and document attribute identity without treating prefix spelling as schema identity. Compared all five briefs and 148 current owned repository descriptions and files where overlapping. No fork, rename or product subdivision counted as new.

Discovery: XML namespace drift and feed-contract searches; prefix-renaming demo.

| Comparable | Stars | Last push UTC | License metadata | Observed workflow/capability tradeoff |
| --- | ---: | --- | --- | --- |
| [NaturalIntelligence/fast-xml-parser](https://github.com/NaturalIntelligence/fast-xml-parser) | 3140 | 2026-10-01T06:36:21Z | MIT | JavaScript parse/build and syntax validation with DTD features; rich general-purpose XML workflow. |
| [lxml/lxml](https://github.com/lxml/lxml) | 3062 | 2026-10-08T11:44:27Z | BSD-3-Clause | Python libxml2-backed toolkit with schemas/XPath/Schematron; native dependency and much broader validation. |
| [sissaschool/xmlschema](https://github.com/sissaschool/xmlschema) | 476 | 2026-06-30T05:57:52Z | MIT | Python XSD 1.0/1.1 validation and decoding; explicit schema infrastructure and richer semantics. |
Additional highest-star XML parser found: [leethomason/tinyxml2](https://github.com/leethomason/tinyxml2), 5,805 stars, pushed 24 May 2026, Zlib license, head `8224e427b655b83dae5e2298f1e6919523a78737`. Read readme.md, tinyxml2.cpp and five current issue/PR entries. C++ DOM parser with examples, not an XSD/business-contract engine.


- [NaturalIntelligence/fast-xml-parser source](https://github.com/NaturalIntelligence/fast-xml-parser/blob/80e88a848b073fd630bc181291a24922c6d1e839/src/validator.js), head `80e88a848b073fd630bc181291a24922c6d1e839`. README `README.md`, source and up to five current issue/PR entries read. Maintenance signal is the dated push, not a guarantee of support. Issue examples: fix: validator; accept XML name characters in entity references, fix: preserve stop-node paths in updateTag callbacks
- [lxml/lxml source](https://github.com/lxml/lxml/blob/584df5c85997bebdb23a4ab4aee15b0ffe96ac66/src/lxml/isoschematron/__init__.py), head `584df5c85997bebdb23a4ab4aee15b0ffe96ac66`. README `README.rst`, source and up to five current issue/PR entries read. Maintenance signal is the dated push, not a guarantee of support. Issue examples: Update libraries, Build: bump pypa/cibuildwheel from 4.2.1 to 4.3.0 in the github-actions group
- [sissaschool/xmlschema source](https://github.com/sissaschool/xmlschema/blob/627c179541ec2e79c0b42c1d493074f7450324c1/xmlschema/validators/schemas.py), head `627c179541ec2e79c0b42c1d493074f7450324c1`. README `README.rst`, source and up to five current issue/PR entries read. Maintenance signal is the dated push, not a guarantee of support. Issue examples: xmlschema-validate: Using `xs:keyref` in XSD for an optional element causes KeyError when XML does not contain this element, `xs:unique` to elements in `xs:alternative` does not work

Installability, time to first result, reliability and support comparison: README instructions, examples, current source and issues were reviewed. Competitor clean installations, workload timing, historical support response and demo reliability were **not measured**. Our own clean installation/demo proves only our behavior. NOASSERTION is incomplete license metadata, not a conclusion about permission. Licenses/attribution require actual upstream license review before reuse; no upstream code reused here.

No technical-performance benchmark or superiority claim. Workloads/hardware/versions were not measured equivalently, so stars and a successful example do not imply we outperform these tools. Broader tools already offer valuable workflows; this MVP chooses a small explicit contract with significant limits.

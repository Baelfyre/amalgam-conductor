# Routing Matrix

Confirm that named skills are installed before recommending them. Use a capability label only when no exact skill exists.

| Project signal | Project type | Recommended skill | Avoid | Reason |
|---|---|---|---|---|
| UI, UX, accessibility, forms, responsive layout, dashboards | Product experience | `cloak-meister` | Diagram or backend review alone | Cloak Meister owns the visible and experiential layer. |
| README, reports, implementation or test summaries | Documentation | `scribe-meister` | Domain review as prose owner | Scribe Meister owns verified project documentation. |
| UML, use case, sequence, ERD visual, architecture or process diagram | Diagram | `meister-weaver` | Cloak Meister for system modeling | Weaver owns notation and visual models; add a domain specialist for semantics. |
| Schema, constraints, SQL, seed data, migrations, data dictionary | Database | `meister-chronicler` | UI specialist alone | Chronicler owns database semantics and evidence. |
| Test plan, test cases, QA checklist | Quality review | `acme-overseer` | Generic QA routing | Acme Overseer owns testing and quality readiness. |
| Regression, smoke test, release readiness | Release quality | `acme-overseer` | `hidden-dagger` as first pass | Normal readiness comes before destructive testing. |
| Defect report, reproduction steps, expected versus actual | Defect triage | `acme-overseer` | Broad code review first | Defects need reproducibility, severity, evidence, and retest guidance. |
| Auth, authorization, RBAC, roles, sessions | Security review | `cipher-meister` | Generic security routing | Cipher owns security/privacy evidence review and remediation planning. |
| Secrets, credentials, tokens, API keys | Secrets review | `cipher-meister` | Documentation-only review | Secrets require defensive handling and evidence-based remediation. |
| Personal data, privacy, retention, minimization | Privacy review | `cipher-meister` | Database-only review | Privacy requires purpose, minimization, retention, and protection review. |
| API security, dependency security, supply chain | Security risk review | `cipher-meister`; scanner when code-level analysis is required | Generic QA routing | Use Cipher for reporting and scanners for source-level findings. |
| Destructive, negative, or fuzz testing | Gated resilience testing | `hidden-dagger` | Automatic routing | Hidden Dagger requires explicit invocation, non-production scope, and safety approval. |
| Break this, pressure-test, crash test, failure paths | Controlled adversarial QA | `hidden-dagger` | Production testing | The request requires bounded side effects and rollback. |
| Invalid inputs, malformed payloads, boundary abuse | Guardrail pressure testing | `hidden-dagger` | Normal QA when pressure testing is requested | Hidden Dagger tests whether validated guardrails fail under adverse conditions. |
| Database constraint stress testing | Database resilience testing | `hidden-dagger` after `meister-chronicler` when needed | Schema changes without approval | Safe data, rollback, and explicit mutation scope are required. |
| Release candidate, pre-production pressure test | Pre-release resilience | Recommend `hidden-dagger`; invoke only with user choice and gate | Early-stage or implicit use | Project maturity permits a recommendation, not automatic activation. |
| One-line text, style, or config correction | Any | Direct handling or one specialist | Full routing stack | Over-routing costs more than the task. |

## Conflict resolution

- Assign one owner per output and sequence dependencies.
- Prefer `acme-overseer` for normal QA and `cipher-meister` for normal security/privacy review.
- Use a dedicated security scanner only for source-level analysis; combine it with Cipher only when reporting is separately required.
- Use `hidden-dagger` only after its safety gate and never as the default QA, security, database, or UI reviewer.
- For ERDs, use `meister-chronicler` for semantics and `meister-weaver` for notation.
- Do not load or route specialists whose output is not required.

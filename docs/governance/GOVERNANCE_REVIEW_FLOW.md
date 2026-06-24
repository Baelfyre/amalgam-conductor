# Governance Review Flow

Every request passes through this flow before execution begins. Review depth scales to project risk.

## Standard User Flow

```
Request
↓
Project Context
↓
Governance Basis of Review
↓
Steward Review
↓
Governor Review
↓
Conductor Routing
↓
Specialist Execution
↓
Validation
↓
User Review
```

## Flow Diagram

```
Request
  │
  ▼
┌───────────────────┐
│  Project Context  │  Identify or request context profile
│    Discovery      │
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│ Governance Basis  │  Establish review dimensions & constraints
│    of Review      │
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│ Risk              │  LOW → lightweight review
│ Classification    │  MEDIUM → standard review
│                   │  HIGH → expanded review
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│   The Steward     │  Business alignment, scope, requirements
│     Review        │  (depth scaled to risk level)
└────────┬──────────┘
         │
  BLOCKED ──► STOP
  REVISION_REQUIRED ──► RETURN for revision
  NOT_APPLICABLE ──► SKIP to Governor
  APPROVED ──► Continue
         │
         ▼
┌───────────────────┐
│   The Governor    │  Legal, compliance, privacy, IP, licensing
│     Review        │  (depth scaled to risk level)
└────────┬──────────┘
         │
  BLOCKED ──► STOP
  REVISION_REQUIRED ──► RETURN for remediation
  human_review_required ──► PAUSE for human review
  NOT_APPLICABLE ──► SKIP to Conductor
  APPROVED ──► Continue
         │
         ▼
┌───────────────────┐
│ Amalgam Conductor │  Route to execution skills
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│ Execution         │  Skills perform work
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│ Validation        │  QA, testing, review
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│ Release Gate      │  Final compliance check
└───────────────────┘
```

## Fast Path (LOW Risk)

For trivial or low-risk requests:
- Steward returns `NOT_APPLICABLE` or lightweight `APPROVED`.
- Governor returns `NOT_APPLICABLE` or lightweight `APPROVED`.
- Conductor proceeds immediately.
- Governance adds near-zero token overhead.

## Standard Path (MEDIUM Risk)

- Steward checks scope, requirements, acceptance criteria.
- Governor checks license compat, basic privacy, attribution.
- Compact output format used.

## Expanded Path (HIGH Risk)

- Steward checks full alignment, stakeholders, traceability, roadmap.
- Governor checks full compliance, ToS/PP, human review flag.
- Expanded output format used when findings exist.

## Re-submission

When `REVISION_REQUIRED`:
1. Address all findings.
2. Fill documentation gaps.
3. Re-submit for review.
4. Review restarts from the authority that issued the revision.

## Missing Context

When project context is incomplete:
```
DECISION: REVISION_REQUIRED
REASON: Project context incomplete.
REQUIRED_ACTIONS: [Provide project type, release target, data collection status]
```

The system does not default to HIGH-risk assumptions for unknown projects.

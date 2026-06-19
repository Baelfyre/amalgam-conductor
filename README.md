# Orchestra of Amalgamation

A Markdown-first suite of eight specialist AI instructions for routing, review, documentation, diagrams, databases, quality, security/privacy, and gated resilience testing.

## What this repository is

The repository packages reusable instruction files and adapter guides. Amalgam Conductor selects the smallest useful specialist stack, assigns one owner per output, sequences dependent work, and marks risky actions that require approval.

## What this repository is not

- It is not a guaranteed native plugin for every AI tool.
- It does not contain project-specific instructions or private context.
- It does not grant authorization for production, destructive, or offensive testing.
- It does not bundle external plugins such as Ponytail or Caveman.

## Skills

| Skill | Use for | Do not use for |
|---|---|---|
| [Amalgam Conductor](skills/amalgam-conductor/SKILL.md) | Routing, sequencing, overlap control, and token efficiency | Replacing domain specialists |
| [Cloak Meister](skills/cloak-meister/SKILL.md) | UI/UX, accessibility, frontend layout, dashboards, forms, responsiveness | Database or system-diagram ownership |
| [Scribe Meister](skills/scribe-meister/SKILL.md) | Documentation audits, reports, README files, readiness documents, technical writing | Inventing technical facts |
| [Meister Weaver](skills/meister-weaver/SKILL.md) | UML, use cases, ERD visuals, architecture, workflow, and process diagrams | Database semantics without a database source |
| [Meister Chronicler](skills/meister-chronicler/SKILL.md) | Schema, constraints, SQL, seeds, migrations, dictionaries, database documentation | UI review |
| [Acme Overseer](skills/acme-overseer/SKILL.md) | QA, tests, defects, verification, validation, regression and release readiness | Destructive pressure testing by default |
| [Cipher Meister](skills/cipher-meister/SKILL.md) | Security/privacy evidence, auth, RBAC, secrets, sensitive data, dependencies, remediation | Offensive or destructive testing |
| [Hidden Dagger](skills/hidden-dagger/SKILL.md) | Approved destructive, negative, fuzz, boundary, failure-mode, guardrail, and resilience testing | Automatic, production, or unauthorized testing |

See [SKILL_INDEX.md](SKILL_INDEX.md) for activation levels and output details.

## Recommended routing flow

1. Use Amalgam Conductor when ownership or sequencing is unclear.
2. Route the primary artifact to one specialist.
3. Add another specialist only for a distinct required output.
4. Use Acme Overseer for normal quality evidence and Cipher Meister for normal security/privacy review.
5. Recommend Hidden Dagger only for an explicit or mature pre-production pressure-test need.
6. Invoke Hidden Dagger only after authorization, non-production isolation, scope, rollback, cleanup, and stop conditions are confirmed.

When the task is obvious, invoke the specialist directly.

## Installation summary

Clone or download this repository, then copy the required folders from `skills/` into the instruction or skill location supported by your AI environment. For Codex-compatible local skills, copy individual folders into your local Codex skills directory. See [INSTALLATION.md](INSTALLATION.md) and [adapters/](adapters/README.md).

## Compatibility

The guaranteed portable layer is Markdown. Codex may support direct local skill folders. VS Code AI tools, Antigravity, Claude Code, and local models may require manual context, workspace instructions, or retrieval configuration. This repository does not claim automatic discovery where it has not been configured. See [COMPATIBILITY.md](COMPATIBILITY.md).

## Git safety

Keep experimental agent files outside unrelated repositories. If local instruction files must live inside a project, use `.git/info/exclude` for machine-local exclusions. Use `.gitignore` only when the exclusion belongs to every clone. Check `git status` before staging.

## Test prompts

- Amalgam Conductor: `Use $amalgam-conductor to select the smallest skill stack for this task and explain the sequence.`
- Cloak Meister: `Use $cloak-meister to review this interface for task completion, accessibility, and responsive layout.`
- Scribe Meister: `Use $scribe-meister to audit this documentation against the supplied source files.`
- Meister Weaver: `Use $meister-weaver to review this sequence diagram against the supplied workflow.`
- Meister Chronicler: `Use $meister-chronicler to review this schema and migration for integrity and rollback risk.`
- Acme Overseer: `Use $acme-overseer to assess this test plan, regression evidence, and release readiness.`
- Cipher Meister: `Use $cipher-meister to review the supplied authentication, RBAC, secrets, and privacy evidence defensively.`
- Hidden Dagger: `Use $hidden-dagger to create a safety-gated negative-testing plan for this non-production system. Do not execute tests.`

## Validation

Run either structure validator, then the stale-reference check:

```powershell
./scripts/validate-structure.ps1
./scripts/check-stale-references.ps1
```

```sh
./scripts/validate-structure.sh
```

See [VALIDATION.md](VALIDATION.md) for the complete checklist.

## Contributing and roadmap

Read [CONTRIBUTING.md](CONTRIBUTING.md), [ROADMAP.md](ROADMAP.md), and [CHANGELOG.md](CHANGELOG.md).

## License

No public-release license has been selected. See [LICENSE](LICENSE).

## External plugin disclaimer

Ponytail and Caveman are external tools, are not part of this repository, and must be installed separately from their official sources if desired. This repository adopts only the general principle of concise, high-signal, low-filler review behavior.

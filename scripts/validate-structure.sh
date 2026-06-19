#!/usr/bin/env sh
set -eu

ROOT=${1:-"$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"}
missing=0

check() {
  if [ ! -e "$ROOT/$1" ]; then
    echo "Missing: $1" >&2
    missing=1
  fi
}

for file in README.md LICENSE .gitignore CONTRIBUTING.md CHANGELOG.md SKILL_INDEX.md FOUNDATION.md INSTALLATION.md LOCAL_ONLY_GUIDE.md COMPATIBILITY.md VALIDATION.md ROADMAP.md; do check "$file"; done
for skill in amalgam-conductor cloak-meister scribe-meister meister-weaver meister-chronicler acme-overseer cipher-meister hidden-dagger; do check "skills/$skill/SKILL.md"; done
for adapter in codex vscode antigravity claude-code local-ai; do check "adapters/$adapter"; done
for template in generic-skill-template.md review-output-template.md audit-output-template.md routing-output-template.md safety-gate-template.md scorecard-template.md local-install-template.md; do check "templates/$template"; done

[ "$missing" -eq 0 ] || exit 1
echo "Structure valid: 8 skills, 5 adapters, 7 templates."

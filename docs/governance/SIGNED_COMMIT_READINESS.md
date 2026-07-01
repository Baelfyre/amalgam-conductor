# Signed Commit Readiness

## Purpose

Record the current signed-commit readiness state for the solo maintainer and define the safest next setup path without changing repository rulesets, rewriting history, or weakening recovery options.

## Current Repository Policy

- The active `Protect main` ruleset already includes `required_signatures`.
- Maintainer bypass remains enabled for solo-maintainer recovery.
- Signed-commit readiness is currently a workflow-preparation task, not a new enforcement task.

## Readiness Outcome

`SIGNING_NOT_CONFIGURED`

Current evidence:

- `commit.gpgsign` is not configured.
- `gpg.format` is not configured.
- `user.signingkey` is not configured.
- `gpg.ssh.allowedSignersFile` is not configured.
- local `gpg` is not installed.
- OpenSSH is installed locally.
- no local `~/.ssh/*.pub` public keys were found.
- no GitHub GPG signing keys were found for the authenticated account.
- no GitHub SSH signing keys were found for the authenticated account.
- recent commits show `N` in `git log --format="%h %G? %GS %s"`, and GitHub reports the current `main` commit verification as `unsigned`.

## Recommended Signing Method

Recommended method: `SSH`

Reason:

- Windows already has OpenSSH available.
- local Git version supports modern signing workflows.
- GPG is not installed, so GPG signing would add more tooling work than needed.
- S/MIME is unnecessary for this repository.

This recommendation does not mean SSH signing is ready now. It is the simplest next method once the maintainer creates or selects a signing-capable SSH key and registers it with GitHub.

## Manual Setup Still Needed

1. Choose an SSH key to use for commit signing.
2. Add the public key to GitHub as an SSH signing key.
3. Configure local Git to use SSH signing.
4. Create a small signed test commit on a branch.
5. Verify the commit locally and on GitHub before relying on the workflow.

Do not:

- create or store private keys in the repository
- print private key material into logs or docs
- rewrite or amend old repository history for readiness work
- use bypass for routine unsigned development

## Normal Signed-Commit Workflow

1. Create a branch.
2. Make changes.
3. Run local validation.
4. Commit with signing enabled.
5. Push the branch.
6. Open a pull request.
7. Wait for required checks.
8. Merge only after checks pass.

## Emergency Bypass Workflow

Maintainer bypass remains available only for:

- ruleset repair
- CI repair
- repository access recovery
- urgent governance correction

If bypass is used and it affects governance behavior, CI behavior, release state, or repository protection state, document it afterward in the implementation report or `CHANGELOG.md`.

## Verification Commands

Local verification:

```powershell
git log --show-signature -n 5
git log --format="%h %G? %GS %s" -n 10
git config --show-origin --get commit.gpgsign
git config --show-origin --get gpg.format
git config --show-origin --get user.signingkey
```

GitHub verification:

```powershell
gh api repos/Baelfyre/Orchestra/commits/main --jq ".commit.verification"
```

Expected healthy direction:

- local new commits should no longer show `N`
- GitHub should no longer report `reason: "unsigned"` for newly signed commits

## Optional Local Configuration Examples

Do not run these blindly. Use them only after the maintainer chooses a signing method and confirms the exact key to use.

```powershell
git config --global commit.gpgsign true
git config --global gpg.format ssh
git config --global user.signingkey "<public signing key or key path>"
```

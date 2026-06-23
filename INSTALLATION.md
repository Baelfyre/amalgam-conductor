# Installation

## Plugin Installation

Amalgam Conductor can be installed directly as an AI workflow plugin:

```sh
agy plugin install https://github.com/Baelfyre/amalgam-conductor
```


## Clone or download manually

If you prefer not to use the plugin manager, you can still clone the repository:

```sh
git clone https://github.com/Baelfyre/amalgam-conductor.git
cd amalgam-conductor
```

## Install selected skills locally

Copy only the folders you need from `skills/` into the local skill or instruction location supported by your tool. For Codex-compatible environments, install Amalgam Conductor plus selected specialists in the configured local Codex skills directory.

Keep the repository copy separate from unrelated source repositories. If you deliberately use repo-local instructions, copy or reference only the required skill text and follow [LOCAL_ONLY_GUIDE.md](LOCAL_ONLY_GUIDE.md).

## Refresh installed integrations

To manually refresh your installed skills and plugin configurations, use the refresh script. This runs validation checks automatically.

**For Antigravity:**
```sh
powershell -ExecutionPolicy Bypass -File .\scripts\refresh-installed-integrations.ps1 -Target Antigravity
```

**For Codex (repo-local installation):**
```sh
powershell -ExecutionPolicy Bypass -File .\scripts\refresh-installed-integrations.ps1 -Target Codex -CodexRepoPath "C:\path\to\your\project"
```
*(Do not modify the global `.codex` directory by default.)*

## Verify

Run the structure validator and confirm that normal QA routes to Acme Overseer, normal security/privacy review routes to Cipher Meister, and Hidden Dagger remains gated.

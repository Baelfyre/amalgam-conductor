param(
    [Parameter(Mandatory=$true)]
    [ValidateSet("Antigravity", "Codex", "All")]
    [string]$Target,

    [string]$CodexRepoPath
)

if (($Target -eq "Codex" -or $Target -eq "All") -and [string]::IsNullOrWhiteSpace($CodexRepoPath)) {
    Write-Error "-CodexRepoPath is required when Target is Codex or All."
    exit 1
}

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RepoRoot = Split-Path -Parent $ScriptDir

Write-Host "Running pre-refresh validation..."
& "$ScriptDir\validate-structure.ps1"
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

& "$ScriptDir\validate-manifest.ps1"
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

if ($Target -eq "Antigravity" -or $Target -eq "All") {
    Write-Host "`n[Antigravity] Refreshing plugin..."
    # Tolerate uninstall failure if not installed
    try {
        agy plugin uninstall amalgam-conductor *>&1 | Out-Null
    } catch { }

    agy plugin install https://github.com/Baelfyre/amalgam-conductor
    agy plugin list
}

if ($Target -eq "Codex" -or $Target -eq "All") {
    Write-Host "`n[Codex] Refreshing skills to $CodexRepoPath..."
    
    $exportScript = "$RepoRoot\adapters\codex\export-codex-skills.ps1"
    $installScript = "$RepoRoot\adapters\codex\install-to-repo.ps1"
    
    if (Test-Path $exportScript) {
        Write-Host "Exporting Codex skills first..."
        & $exportScript
    }

    if (Test-Path $installScript) {
        & $installScript -TargetRepo $CodexRepoPath -Force
    } else {
        Write-Error "Codex install script missing: $installScript"
    }
}

Write-Host "`nRefresh complete."

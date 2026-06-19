param(
    [string]$Root = (Split-Path -Parent $PSScriptRoot)
)

$patterns = @(
    'ux-diagram-' + 'architect',
    'meister-' + 'virtuoso',
    'Meister ' + 'Virtuoso',
    'AO' + 'OP',
    'Motor' + 'PH',
    'Hive' + 'Mind',
    'Art ' + 'Appreciation',
    ('C:' + '[\\/]' + 'Users' + '[\\/]'),
    ('/' + 'home' + '/'),
    '(?i)production\s+secrets?',
    '(?i)api[_ -]?keys?\s*[:=]\s*\S+'
)

$self = (Resolve-Path -LiteralPath $PSCommandPath).Path
$findings = Get-ChildItem -LiteralPath $Root -Recurse -File |
    Where-Object { $_.FullName -notmatch '[\\/]\.git[\\/]' -and $_.FullName -ne $self } |
    Select-String -Pattern $patterns

if ($findings) {
    $findings | ForEach-Object { "{0}:{1}: {2}" -f $_.Path, $_.LineNumber, $_.Line.Trim() }
    exit 1
}

Write-Output 'No stale or disallowed references found.'

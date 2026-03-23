Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent $PSScriptRoot
$ComposeFile = Join-Path $RepoRoot "docker\docker-compose.yml"

Write-Host "Stopping MSBX Final Project containers..." -ForegroundColor Cyan
docker compose -f $ComposeFile down
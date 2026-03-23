Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

# Get repo root (parent of scripts folder)
$RepoRoot = Split-Path -Parent $PSScriptRoot
$ComposeFile = Join-Path $RepoRoot "docker\docker-compose.yml"

Write-Host "Starting MSBX Final Project containers..." -ForegroundColor Cyan
docker compose -f $ComposeFile up --build
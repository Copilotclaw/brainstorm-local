# Infrastructure

_Last updated: 2026-03-12_

## Secrets (set in GitHub repo settings)

| Secret | Purpose | Status |
|--------|---------|--------|
| `ALIKEY` | Alibaba Cloud DashScope API key | Required |
| `ALIURL` | Alibaba Cloud base URL | Optional (has default) |
| `COSMOS_ENDPOINT` | Azure Cosmos DB endpoint | Required for bulletin |
| `COSMOS_KEY` | Azure Cosmos DB master key | Required for bulletin |
| `AZURE_ENDPOINT` | Azure AI Foundry base URL | Optional fallback |
| `AZURE_APIKEY` | Azure AI Foundry API key | Optional fallback |

## Cosmos DB

- **Database**: `crunch`
- **Container**: `memories`
- **Partition key**: `/type`
- Tasks targeted at `brain` or `all` are picked up by bulletin-board workflow

## pi CLI

- **Package**: `@mariozechner/pi-coding-agent`
- **Config**: `~/.pi/agent/models.json` (written by configure-pi.py)
- **Sessions**: `state/sessions/*.jsonl`
- **Skills**: `.pi/skills/`

## No heartbeat

Brain is on-demand only. No scheduled workflow runs except bulletin board check (every 6 hours).

# CLAUDE.md — AI Assistant Guide for cyber-intelligence

## Project Overview

**cyber-intelligence** is a cyber-intelligence system for New Jersey cybersecurity news. The system is intended to aggregate, analyze, and surface relevant cybersecurity threat intelligence and news specific to the New Jersey region.

> **Status:** Early-stage repository. Only a README exists. No source code, dependencies, or configuration has been committed yet. This CLAUDE.md should be updated as the project evolves.

---

## Repository Structure (Current)

```
cyber-intelligence/
├── README.md       # One-line project description
└── CLAUDE.md       # This file
```

### Anticipated Structure (to be populated)

```
cyber-intelligence/
├── src/                    # Application source code
│   ├── collectors/         # Data ingestion / feed scrapers
│   ├── processors/         # NLP, classification, enrichment
│   ├── storage/            # Database models and access layer
│   ├── api/                # REST or GraphQL API layer
│   └── ui/                 # Frontend (if applicable)
├── tests/                  # Test suite mirroring src/
├── scripts/                # Dev/ops utility scripts
├── docs/                   # Architecture diagrams, ADRs
├── .github/workflows/      # CI/CD pipelines
├── requirements.txt        # Python deps (or package.json for Node)
├── .env.example            # Required environment variables (no secrets)
├── README.md
└── CLAUDE.md
```

---

## Development Workflow

### Branching Strategy

- `main` — stable, production-ready code
- `claude/<description>-<id>` — AI-assisted feature/documentation branches
- Feature branches should be short-lived and merged via pull request

### Commit Conventions

Use [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add RSS feed collector for NJ cybersecurity sources
fix: handle timeout in CISA feed scraper
docs: update architecture decision record for storage layer
refactor: extract feed normalization into shared utility
test: add unit tests for news classifier
```

### Pull Requests

- PRs should reference the issue they close (`Closes #123`)
- Include a brief description of what changed and why
- Ensure all CI checks pass before merging

---

## Key Conventions for AI Assistants

### Do

- **Read files before editing them.** Never modify a file without first reading it.
- **Preserve existing patterns.** If the codebase uses a specific style or structure, continue it rather than introducing a new one.
- **Keep changes scoped.** Only modify what is required for the task — no opportunistic refactoring or cleanup unless explicitly asked.
- **Use the correct branch.** Develop on the branch specified in the session. Never push to `main` directly.
- **Write tests** for any non-trivial logic added.
- **Document environment variables** in `.env.example` whenever a new one is introduced.

### Do Not

- Do not commit secrets, API keys, credentials, or `.env` files.
- Do not add error handling, abstractions, or features beyond what the task requires.
- Do not rename or restructure files unless explicitly asked.
- Do not add docstrings or comments to code you didn't write or change.
- Do not create new files when editing an existing one would suffice.
- Do not bypass git hooks (`--no-verify`) or security checks.

---

## Technology Stack

> **Not yet decided.** Update this section when the stack is chosen. Likely candidates based on the project domain:

| Layer | Candidates |
|---|---|
| Language | Python (preferred for data/ML tasks) or Node.js |
| Web framework | FastAPI / Flask (Python) or Express (Node) |
| Data storage | PostgreSQL or SQLite for structured data |
| Search / indexing | Elasticsearch or similar for news search |
| Task queue | Celery + Redis or similar for scheduled collection |
| Frontend | Plain HTML/JS, React, or Next.js |

---

## Environment Setup

> Update this section once the stack is decided.

Expected pattern once dependencies exist:

```bash
# Clone
git clone <repo-url>
cd cyber-intelligence

# Create and activate virtual environment (Python)
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Copy and fill in environment variables
cp .env.example .env

# Run tests
pytest

# Start the application
python -m src.main
```

---

## Testing

> No tests exist yet. Update this section as the test suite grows.

- Tests live in `tests/` and mirror the structure of `src/`
- Run the full suite with the project's test runner (e.g., `pytest`, `npm test`)
- Tests must pass in CI before merging any PR
- Aim for unit tests on business logic and integration tests on external feed collectors

---

## CI/CD

> No pipelines configured yet. When added, document them here.

Expected checks on every PR:
- Linting (e.g., `flake8`, `eslint`)
- Type checking (e.g., `mypy`, `tsc`)
- Test suite
- Dependency vulnerability scan

---

## Security Considerations

This project handles cybersecurity-related data. Key practices:

- Never log or commit sensitive data (API keys, credentials, PII)
- Validate and sanitize all external input (feed data, API requests)
- Use parameterized queries — never interpolate user input into SQL
- Keep dependencies updated and scan for known vulnerabilities
- Store secrets in environment variables, never in source code

---

## Updating This File

This file should be updated whenever:
- A technology stack decision is made
- A new major component or directory is added
- Development workflows or conventions change
- CI/CD pipelines are introduced or modified
- Onboarding instructions become more concrete

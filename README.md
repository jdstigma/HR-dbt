# HR dbt Project

A human resources analytics database built with dbt and PostgreSQL, running entirely in GitHub Codespaces. The project transforms raw HR seed data through a layered model architecture (staging → intermediate → marts) and connects to Power BI for reporting.

---

## Approach Comparison

### Traditional ETL Approach vs. dbt Approach

| | Traditional | This Project (dbt) |
|---|---|---|
| **Transformations** | SQL scripts run manually in SSMS or pgAdmin | dbt models — versioned, testable SQL SELECT statements |
| **Execution order** | Managed manually | dbt builds a DAG and runs models in the correct dependency order automatically |
| **Testing** | Ad-hoc queries to spot-check data | Built-in schema tests (`not_null`, `unique`, `accepted_values`, relationships) |
| **Documentation** | Usually none, or a separate Word doc | Auto-generated from `schema.yml` — always in sync with the code |
| **Reproducibility** | Depends on who runs the scripts and when | `dbt run` rebuilds the entire pipeline from scratch deterministically |
| **CI/CD** | Manual deployment | GitHub Actions runs `dbt seed → dbt run → dbt test` on every push |
| **Environment** | Local machine dependency | Fully containerized in GitHub Codespaces — works the same for everyone |
| **Version control** | SQL files sometimes committed, often not | Every model, test, and config lives in git |

### Tool Choices and Why

| Decision | Alternative Considered | What We Chose | Reason |
|---|---|---|---|
| **Warehouse** | DuckDB (local file, zero config) | PostgreSQL 14 | Native Power BI connector via ODBC — DuckDB has no direct Power BI support |
| **Environment** | Local machine install | GitHub Codespaces | Reproducible, no local dependencies, accessible from anywhere |
| **Devcontainer setup** | Devcontainer feature (`ghcr.io/devcontainers/features/postgres:1`) | Dockerfile + `setup.sh` | Feature requires elevated permissions not available on free Codespaces plans |
| **Install timing** | Everything in `setup.sh` at runtime | Dockerfile (build time) + `setup.sh` (runtime only) | Faster cold starts — installs are baked into the image, not re-run every time |
| **Dependency management** | `pip install dbt-postgres` inline | `requirements.txt` | Single source of truth — both Codespaces and GitHub Actions use the same file |
| **dbt project init** | Interactive `dbt init` prompts | `dbt init --skip-profile-setup` | `profiles.yml` written by `setup.sh` automatically — no manual input needed |

---

## Dataset

Fictional company **Meridian Global Corp** — 3,000 employees across 8 divisions, 30 departments, and 15 global office locations.

| File | Description | Rows |
|---|---|---|
| `employees.csv` | Employee profiles, hire dates, salaries | 3,000 |
| `departments.csv` | 30 departments across 8 divisions | 30 |
| `divisions.csv` | 8 business divisions | 8 |
| `jobs.csv` | 50 job titles with salary bands | 50 |
| `locations.csv` | 15 global office locations | 15 |
| `performance_reviews.csv` | Semi-annual reviews 2015–2024 | ~29,500 |
| `training_records.csv` | Course completions per employee | ~45,500 |
| `payroll_history.csv` | Monthly pay records 2020–2024 | ~125,700 |
| `job_history.csv` | Position and salary changes over tenure | ~7,200 |
| `benefits_enrollment.csv` | Benefit plan elections per employee | 15,000 |
| `attendance_summary.csv` | Monthly attendance 2020–2024 | ~126,100 |

**Total: ~352,000 rows**

---

## Architecture

```
seeds/ (raw CSVs)
    └── dbt seed → PostgreSQL (hr_db)

models/
    staging/        → one model per seed, cast types, rename columns   (views)
    intermediate/   → join staging models, business logic               (views)
    marts/          → final reporting tables for Power BI               (tables)
```

---

## Stack

| Layer | Tool |
|---|---|
| Transformation | dbt-postgres 1.10 |
| Database | PostgreSQL 14 |
| Environment | GitHub Codespaces |
| CI/CD | GitHub Actions |
| Reporting | Power BI (via port 5432 forwarding) |
| Language | Python 3.11 (dataset generation) |

---

## Getting Started

Open in Codespaces — the container builds automatically and runs setup:

1. Installs PostgreSQL and dbt *(Dockerfile — build time)*
2. Starts PostgreSQL, creates `hr_db`, writes `~/.dbt/profiles.yml` *(setup.sh — runtime)*

Then in the terminal:

```bash
cd hr_dbt
dbt seed       # load all CSVs into PostgreSQL
dbt run        # build all models
dbt test       # run data quality tests
```

---

## CI/CD

Every push to `main` triggers the GitHub Actions workflow which:
- Spins up a fresh PostgreSQL 14 container
- Installs dependencies from `requirements.txt`
- Writes `profiles.yml` dynamically (no secrets stored in repo)
- Auto-detects the dbt project directory via `dbt_project.yml` search
- Runs `dbt seed → dbt run → dbt test`

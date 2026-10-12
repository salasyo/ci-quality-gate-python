# ci-quality-gate-python

![CI](https://github.com/salasyo/ci-quality-gate-python/actions/workflows/ci.yml/badge.svg)
![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=salasyo_ci-quality-gate-python&metric=alert_status)
![Coverage](https://sonarcloud.io/api/project_badges/measure?project=salasyo_ci-quality-gate-python&metric=coverage)

Mini Project 1.4: CI Quality Gate & Reporting Implementation.
A small Python project whose CI pipeline blocks low-quality or insecure code from reaching `main`.

## Quality gates

| Gate | Tool | Threshold | Enforced by |
|---|---|---|---|
| Lint | ruff | 0 errors | `ruff check .` fails the job |
| Test coverage | pytest-cov | >= 80% | `--cov-fail-under=80` |
| Static security | bandit | no HIGH severity | `bandit -r src -lll` |
| Dependency vulns | pip-audit | no known vulnerable deps | `pip-audit` |
| Code quality | SonarCloud | Quality Gate = Passed | `sonar.qualitygate.wait=true` |
| Merge protection | GitHub ruleset `protect-main` | all checks required | branch rules |

## Run locally

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
ruff check .
pytest
bandit -r src -lll
pip-audit -r requirements.txt
```

## Reports
- Coverage HTML + XML: download the `coverage-report` artifact from any Actions run.
- Static analysis: SonarCloud dashboard (link in the metrics report).
- Metrics analysis: `Quality-Metrics-Report.md`

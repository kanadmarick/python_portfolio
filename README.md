# Python Fullstack Portfolio

This is a monorepo portfolio containing multiple fullstack projects (backend + frontend) with DevOps automation and CI/CD integration.

## Structure
- `projects/` - Contains all individual projects
- `shared/` - Shared modules/utilities
- `devops/` - DevOps scripts, Dockerfiles, k8s, terraform, ansible, etc.
- `.github/workflows/` - GitHub Actions CI/CD workflows

## Getting Started
- Each project has its own README and setup instructions.
- See `devops_automation.py` for DevOps pipeline automation.


## CI/CD
- Automated with GitHub Actions and `devops_automation.py`.
- Python CI workflow for `projects/project1/backend` is set up in `.github/workflows/python-ci-project1-backend.yml`.
	- Runs on push and pull request to `projects/project1/backend`.
	- Installs dependencies, lints with flake8, and runs tests if present.

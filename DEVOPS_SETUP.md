# DevOps Setup & Deployment Guide

## Week 1 Implementation - Basic DevOps

This guide covers the DevOps infrastructure added to the Smart Planning Agent project.

### ✅ What's Been Added

#### 1. **Containerization**

- **Dockerfile**: Multi-stage Docker build for optimized production images
- **.dockerignore**: Excludes unnecessary files from Docker build context
- **docker-compose.yml**: Orchestrates backend and frontend services locally
- **Frontend Dockerfile**: Separate container for React Vite frontend

**Start containers:**

```bash
docker-compose up -d
# Backend: http://localhost:8000
# Frontend: http://localhost:5173
```

#### 2. **CI/CD Pipeline**

- **.github/workflows/ci-cd.yml**: GitHub Actions workflow that:
  - Runs on every push and pull request
  - Lints code (Black, Pylint, Flake8)
  - Type checks with mypy
  - Runs unit tests with pytest
  - Generates coverage reports
  - Builds Docker images

**Trigger:** Push to `main` or `develop` branches, or create pull requests

#### 3. **Code Quality Tools**

**Black (Code Formatter)**

```bash
black src/ tests/ api.py
```

**Pylint (Code Quality)**

```bash
pylint src/**/*.py api.py --fail-under=7.0
```

**Flake8 (Linting)**

```bash
flake8 src/ api.py
```

**mypy (Type Checking)**

```bash
mypy src/ api.py --ignore-missing-imports
```

#### 4. **Testing Framework**

- **pytest**: Unit test framework
- **pytest-cov**: Code coverage reporting
- **Fixtures**: Pre-configured mocks for testing

**Run tests:**

```bash
pytest tests/ -v --cov=src --cov-report=html
```

**Test files:**

- `tests/test_api.py` - API endpoint tests
- `tests/test_agents.py` - Agent creation and task tests
- `tests/test_logging.py` - Logging functionality tests
- `tests/conftest.py` - Shared test fixtures and mocks

#### 5. **Logging**

- Centralized logging setup with rotation
- Logs to console and file (`logs/app_*.log`)
- Structured format with timestamps
- Integrated into API for request/response tracking

**Usage in code:**

```python
from src.utils.logging import get_logger
logger = get_logger(__name__)
logger.info("Message")
logger.error("Error", exc_info=True)
```

#### 6. **Configuration Files**

- `pytest.ini` - Pytest configuration
- `.flake8` - Flake8 rules
- `.pylintrc` - Pylint configuration
- `mypy.ini` - Type checking configuration

---

## Local Development Setup

### 1. **Install Dependencies**

```bash
pip install -r requirements.txt
```

### 2. **Set Environment Variables**

```bash
cp .env.example .env
# Edit .env with your API keys
```

### 3. **Run Linting & Formatting**

```bash
# Format code
black src/ tests/ api.py

# Check for issues
flake8 src/ api.py
pylint src/**/*.py api.py
mypy src/ api.py
```

### 4. **Run Tests**

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=src --cov-report=html
# Open htmlcov/index.html in browser

# Run specific test
pytest tests/test_api.py::test_health_endpoint -v
```

### 5. **Run Application**

**Without Docker:**

```bash
uvicorn api:app --reload --host 0.0.0.0 --port 8000
```

**With Docker:**

```bash
docker-compose up
```

---

## Docker Commands

### Build Images

```bash
# Build backend
docker build -t smart-marketing-backend .

# Build frontend
docker build -t smart-marketing-frontend ./frontend
```

### Run Containers

```bash
# Run backend only
docker run -p 8000:8000 \
  -e OPENROUTER_API_KEY=your_key \
  smart-marketing-backend

# Run with docker-compose (both services)
docker-compose up -d

# View logs
docker-compose logs -f backend
docker-compose logs -f frontend

# Stop containers
docker-compose down
```

---

## GitHub Actions Workflow

The CI/CD pipeline runs automatically on:

- ✅ Push to `main` branch
- ✅ Push to `develop` branch
- ✅ Pull requests to `main` and `develop`

**Jobs executed:**

1. **Lint and Test** (~5-10 min)
   - Install dependencies
   - Format check (Black)
   - Lint (Pylint, Flake8)
   - Type check (mypy)
   - Run tests (pytest with coverage)

2. **Build Docker** (~3-5 min)
   - Build Docker image
   - Cache layers for faster builds

View workflow results in GitHub → Actions tab

---

## Project Structure After DevOps Integration

```
Smart-Marketing-Assistant-Crew-AI/
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # GitHub Actions workflow
├── src/
│   ├── agents.py
│   ├── tasks.py
│   ├── tools.py
│   └── utils/
│       ├── __init__.py
│       └── logging.py          # Centralized logging
├── tests/
│   ├── conftest.py             # Pytest fixtures
│   ├── test_api.py             # API tests
│   ├── test_agents.py          # Agent tests
│   └── test_logging.py         # Logging tests
├── frontend/
│   ├── Dockerfile              # Frontend container
│   ├── src/
│   └── package.json
├── Dockerfile                  # Backend container
├── docker-compose.yml          # Container orchestration
├── .dockerignore               # Docker build exclusions
├── .env.example                # Environment template
├── .flake8                      # Flake8 config
├── .pylintrc                    # Pylint config
├── mypy.ini                     # mypy config
├── pytest.ini                   # Pytest config
├── requirements.txt            # Python dependencies
├── api.py                       # FastAPI app (logging integrated)
└── logs/                        # Generated at runtime
```

---

## Common Commands

| Task               | Command                                     |
| ------------------ | ------------------------------------------- |
| Install deps       | `pip install -r requirements.txt`           |
| Format code        | `black src/ tests/ api.py`                  |
| Run linter         | `flake8 src/ api.py`                        |
| Type check         | `mypy src/ api.py --ignore-missing-imports` |
| Run tests          | `pytest tests/ -v`                          |
| Coverage report    | `pytest tests/ --cov=src --cov-report=html` |
| Run API locally    | `uvicorn api:app --reload`                  |
| Run with Docker    | `docker-compose up`                         |
| Stop Docker        | `docker-compose down`                       |
| View backend logs  | `docker-compose logs -f backend`            |
| Build Docker image | `docker build -t smart-marketing:latest .`  |

---

## Next Steps (Week 2+)

1. **Database Integration** - PostgreSQL + SQLAlchemy ORM
2. **API Enhancements** - Rate limiting, authentication
3. **Advanced Monitoring** - Prometheus, Grafana
4. **Kubernetes** - K8s manifests for cloud deployment
5. **Terraform** - Infrastructure as Code for cloud deployment

---

## Troubleshooting

### Docker build fails

```bash
# Clear cache and rebuild
docker-compose build --no-cache
```

### Port already in use

```bash
# Change port in docker-compose.yml
# Or kill process using port 8000
lsof -i :8000
kill -9 <PID>
```

### Tests fail in CI but pass locally

- Ensure `.env` variables are set in GitHub Secrets
- Check Python version (should be 3.10)
- Verify all dependencies match requirements.txt

### Logs not appearing

- Check `logs/` directory exists and has write permissions
- Verify `PYTHONUNBUFFERED=1` environment variable is set

---

## Resources

- [Docker Documentation](https://docs.docker.com/)
- [GitHub Actions](https://docs.github.com/en/actions)
- [pytest Documentation](https://docs.pytest.org/)
- [Black Code Formatter](https://black.readthedocs.io/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)

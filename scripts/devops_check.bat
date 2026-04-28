@echo off
REM DevOps setup and validation script for Windows

echo.
echo 🚀 Smart Marketing Assistant - DevOps Setup
echo ==========================================

REM Check Python version
echo ✓ Checking Python version...
python --version

REM Install dependencies
echo ✓ Installing dependencies...
pip install -r requirements.txt

REM Run code formatting
echo ✓ Formatting code with Black...
black src\ tests\ api.py --quiet

REM Run linting
echo ✓ Running Flake8...
flake8 src\ api.py --count

REM Run type checking
echo ✓ Type checking with mypy...
mypy src\ api.py --ignore-missing-imports --quiet

REM Run tests
echo ✓ Running tests...
pytest tests\ -v --cov=src --cov-report=term-missing

echo.
echo ✅ All checks passed!
echo.
echo Next steps:
echo 1. Set up .env file: copy .env.example .env and edit .env
echo 2. Run locally: uvicorn api:app --reload
echo 3. Or use Docker: docker-compose up

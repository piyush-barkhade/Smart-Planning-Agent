#!/bin/bash
# DevOps setup and validation script

echo "🚀 Smart Marketing Assistant - DevOps Setup"
echo "=========================================="

# Check Python version
echo "✓ Checking Python version..."
python --version

# Install dependencies
echo "✓ Installing dependencies..."
pip install -r requirements.txt

# Run code formatting
echo "✓ Formatting code with Black..."
black src/ tests/ api.py --quiet

# Run linting
echo "✓ Running Flake8..."
flake8 src/ api.py --count

# Run type checking
echo "✓ Type checking with mypy..."
mypy src/ api.py --ignore-missing-imports

# Run tests
echo "✓ Running tests..."
pytest tests/ -v --cov=src --cov-report=term-missing

echo ""
echo "✅ All checks passed!"
echo ""
echo "Next steps:"
echo "1. Set up .env file: cp .env.example .env && edit .env"
echo "2. Run locally: uvicorn api:app --reload"
echo "3. Or use Docker: docker-compose up"

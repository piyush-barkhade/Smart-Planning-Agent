import pytest
import sys
import os
from unittest.mock import patch, MagicMock

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


# Mock environment variables for testing
@pytest.fixture(autouse=True)
def mock_env_vars():
    """Mock environment variables for all tests"""
    with patch.dict(
        os.environ,
        {
            "OPENROUTER_API_KEY": "test-key-123",
            "OPENROUTER_MODEL": "openrouter/openai/gpt-3.5-turbo",
            "EXA_API_KEY": "test-exa-key",
            "LANGCHAIN_API_KEY": "test-langchain-key",
            "LANGCHAIN_TRACING_V2": "false",
        },
    ):
        yield


@pytest.fixture
def mock_llm():
    """Mock LLM for testing"""
    mock = MagicMock()
    mock.model = "openrouter/openai/gpt-3.5-turbo"
    return mock


@pytest.fixture
def mock_agent():
    """Mock agent for testing"""
    mock = MagicMock()
    mock.role = "Test Agent"
    mock.goal = "Test goal"
    return mock


@pytest.fixture
def mock_task():
    """Mock task for testing"""
    mock = MagicMock()
    mock.description = "Test task"
    mock.expected_output = "Test output"
    return mock

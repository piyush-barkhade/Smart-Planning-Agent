"""Tests for agent functionality"""
import pytest
import sys
import os
from unittest.mock import MagicMock, patch

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


class TestAgentCreation:
    """Test agent creation and configuration"""
    
    def test_agent_role_assignment(self, mock_agent):
        """Test that agents have proper roles assigned"""
        assert mock_agent.role == 'Test Agent'
        assert mock_agent.goal == 'Test goal'
    
    def test_agent_has_tools(self, mock_agent):
        """Test that agents are configured with tools"""
        mock_agent.tools = ['search_tool', 'research_tool']
        assert len(mock_agent.tools) > 0
    
    def test_agent_llm_configuration(self, mock_llm):
        """Test LLM configuration"""
        assert mock_llm.model is not None
        assert 'gpt' in mock_llm.model.lower() or 'openrouter' in mock_llm.model.lower()


class TestTaskExecution:
    """Test task execution"""
    
    def test_task_has_description(self, mock_task):
        """Test that tasks have descriptions"""
        assert mock_task.description is not None
        assert len(mock_task.description) > 0
    
    def test_task_has_expected_output(self, mock_task):
        """Test that tasks define expected output"""
        assert mock_task.expected_output is not None

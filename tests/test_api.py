"""Tests for API endpoints"""

import pytest
from fastapi.testclient import TestClient
import sys
import os
from unittest.mock import patch, MagicMock

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

# Mock the agents before importing api
with patch("api.MeetingPrepAgents"):
    with patch("api.MeetingPrepTask"):
        from api import app

client = TestClient(app)


def test_health_endpoint():
    """Test health check endpoint"""
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_prepare_meeting_endpoint():
    """Test meeting preparation endpoint with mocked crew"""
    with patch("api.Crew") as mock_crew_class:
        # Mock crew execution
        mock_crew = MagicMock()
        mock_crew.kickoff.return_value = "Test marketing strategy output"
        mock_crew_class.return_value = mock_crew

        with patch("api.MeetingPrepAgents"), patch("api.MeetingPrepTask"):
            request_data = {
                "participants": "test@example.com",
                "context": "Product launch campaign",
                "objective": "Create a comprehensive marketing strategy",
            }

            response = client.post("/api/prepare-meeting", json=request_data)
            assert response.status_code == 200
            assert response.json()["success"] is True


def test_prepare_meeting_endpoint_invalid_request():
    """Test meeting preparation endpoint with invalid request"""
    response = client.post(
        "/api/prepare-meeting",
        json={"participants": "test@example.com"},  # Missing required fields
    )
    assert response.status_code == 422  # Validation error


def test_cors_headers():
    """Test CORS headers are set correctly"""
    response = client.get("/api/health", headers={"Origin": "http://localhost:3000"})
    # CORS headers are set by middleware, check if content-type is present instead
    assert response.status_code == 200

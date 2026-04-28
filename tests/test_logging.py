"""Tests for logging functionality"""

import pytest
import sys
import os
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.utils.logging import setup_logging, get_logger


class TestLogging:
    """Test logging setup and functionality"""

    def test_setup_logging_creates_logger(self):
        """Test that setup_logging creates a logger"""
        logger = setup_logging("test_logger")
        assert logger is not None
        assert logger.name == "test_logger"

    def test_setup_logging_creates_log_file(self, tmp_path):
        """Test that setup_logging creates log files"""
        log_file = tmp_path / "test.log"
        logger = setup_logging("test_logger_file_unique", log_file=str(log_file))
        logger.info("Test message")
        logger.handlers[0].flush()  # Flush handlers to ensure write
        assert log_file.exists()

    def test_get_logger_returns_logger(self):
        """Test that get_logger returns logger instance"""
        logger = get_logger("test_get")
        assert logger is not None

    def test_logger_logs_to_file(self, tmp_path):
        """Test that logger writes to file"""
        log_file = tmp_path / "app_test.log"
        logger = setup_logging("test_file_write_unique", log_file=str(log_file))
        test_message = "Test log message"
        logger.info(test_message)
        logger.handlers[0].flush()  # Flush handlers to ensure write

        assert log_file.exists()
        with open(log_file, "r") as f:
            content = f.read()
            assert test_message in content

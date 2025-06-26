"""Fixtures for Duolingo integration tests."""

from unittest.mock import patch

import pytest


@pytest.fixture(autouse=True)
def auto_enable_custom_integrations(enable_custom_integrations):
    """Enable loading of custom integrations in all tests."""
    return


@pytest.fixture
def mock_setup_entry():
    """Mock setup entry."""
    with patch(
        "custom_components.duolingo.async_setup_entry", return_value=True
    ) as mock_setup:
        yield mock_setup


@pytest.fixture
def mock_duolingo_api():
    """Mock DuolingoApiClient."""
    with patch("custom_components.duolingo.api.DuolingoApiClient") as mock_client:
        client = mock_client.return_value
        client.get_streak_data.return_value = {
            "username": "testuser",
            "streak_extended_today": True,
            "site_streak": 42,
        }
        yield client

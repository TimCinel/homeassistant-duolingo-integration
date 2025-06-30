"""Test Duolingo API."""

from unittest.mock import MagicMock, patch

import pytest
import requests

from custom_components.duolingo.api import DuolingoApiClient


def test_api_get_streak_data_success():
    """Test successful API call."""
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "users": [
            {
                "username": "testuser",
                "streakData": {
                    "currentStreak": {"endDate": "2023-12-01", "length": 42}
                },
                "totalXp": 12500,
            }
        ]
    }
    mock_response.raise_for_status = MagicMock()

    with (
        patch(
            "custom_components.duolingo.api.requests.get", return_value=mock_response
        ),
        patch("custom_components.duolingo.api.datetime") as mock_datetime,
    ):
        mock_datetime.now.return_value.strftime.return_value = "2023-12-01"

        client = DuolingoApiClient("testuser")
        result = client.get_streak_data()

    assert result == {
        "username": "testuser",
        "streak_extended_today": True,
        "site_streak": 42,
        "total_xp": 12500,
    }


def test_api_get_streak_data_no_streak():
    """Test API call with no current streak."""
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "users": [
            {
                "username": "testuser",
                "streakData": {"currentStreak": None},
                "totalXp": 0,
            }
        ]
    }
    mock_response.raise_for_status = MagicMock()

    with patch(
        "custom_components.duolingo.api.requests.get", return_value=mock_response
    ):
        client = DuolingoApiClient("testuser")
        result = client.get_streak_data()

    assert result == {
        "username": "testuser",
        "streak_extended_today": False,
        "site_streak": 0,
        "total_xp": 0,
    }


def test_api_get_streak_data_no_user():
    """Test API call with no user found."""
    mock_response = MagicMock()
    mock_response.json.return_value = {"users": []}
    mock_response.raise_for_status = MagicMock()

    with patch(
        "custom_components.duolingo.api.requests.get", return_value=mock_response
    ):
        client = DuolingoApiClient("invaliduser")

        with pytest.raises(
            ValueError, match="No user found with username: invaliduser"
        ):
            client.get_streak_data()


def test_api_request_error():
    """Test API request error."""
    with patch(
        "custom_components.duolingo.api.requests.get",
        side_effect=requests.RequestException("Connection error"),
    ):
        client = DuolingoApiClient("testuser")

        with pytest.raises(requests.RequestException):
            client.get_streak_data()

"""Duolingo API client."""

import logging
from datetime import UTC, datetime
from typing import Any

import requests

_LOGGER: logging.Logger = logging.getLogger(__package__)


class DuolingoApiClient:
    """Client for communicating with Duolingo API."""

    def __init__(self, username: str) -> None:
        """Duolingo API Client."""
        self._username = username

    def get_streak_data(self) -> dict[str, Any]:
        """Get streak data for the configured user."""
        url = f"https://www.duolingo.com/2017-06-30/users?username={self._username}"
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/91.0.4472.124 Safari/537.36"
            )
        }

        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        json_data = response.json()
        users = json_data.get("users", [])

        if not users:
            msg = f"No user found with username: {self._username}"
            raise ValueError(msg)

        user_data = users[0]
        today = datetime.now(tz=UTC).strftime("%Y-%m-%d")

        # Handle case where currentStreak is null (no active streak)
        current_streak = user_data["streakData"].get("currentStreak")
        if current_streak:
            streak_extended_today = today == current_streak.get("endDate", "")
            site_streak = current_streak.get("length", 0)
        else:
            streak_extended_today = False
            site_streak = 0

        return {
            "username": user_data["username"],
            "streak_extended_today": streak_extended_today,
            "site_streak": site_streak,
        }

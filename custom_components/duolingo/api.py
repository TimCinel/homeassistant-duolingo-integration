import logging
from datetime import datetime

import requests

_LOGGER: logging.Logger = logging.getLogger(__package__)

class DuolingoApiClient:
    def __init__(self, user_id: str) -> None:
        """Duolingo API Client."""
        self._user_id = user_id

    def get_streak_data(self) -> dict:
        url = f"https://www.duolingo.com/2017-06-30/users/{self._user_id}"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        json = response.json()
        today = datetime.now().strftime("%Y-%m-%d")
        self._username = json['username']

        return {
                "username": json['username'],
                "streak_extended_today": today == json['streakData']['currentStreak']['lastExtendedDate'],
                "site_streak": json['streakData']['currentStreak']['length']}

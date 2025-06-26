"""Adds config flow for Duolingual."""

import voluptuous as vol
from homeassistant import config_entries

from .api import DuolingoApiClient
from .const import (
    CONF_USERNAME,
    DOMAIN,
)


class DuolingualFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for Duolingual."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

    def __init__(self):
        """Initialize."""
        self._errors = {}

    async def async_step_user(self, user_input=None):
        """Handle a flow initialized by the user."""
        self._errors = {}

        if user_input is not None:
            username = user_input[CONF_USERNAME]

            # Validate username directly
            try:
                valid = await self._test_credentials(username)
                if valid:
                    # Store username in config entry
                    config_data = {CONF_USERNAME: username}
                    return self.async_create_entry(title=username, data=config_data)
                self._errors["base"] = "auth"
            except Exception:
                self._errors["base"] = "auth"

            return await self._show_config_form(user_input)

        user_input = {}
        # Provide defaults for form
        user_input[CONF_USERNAME] = ""

        return await self._show_config_form(user_input)

    async def _show_config_form(self, user_input):  # pylint: disable=unused-argument
        """Show the configuration form to edit location data."""
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_USERNAME, default=user_input[CONF_USERNAME]): str,
                }
            ),
            errors=self._errors,
        )

    async def _test_credentials(self, username):
        """Return true if credentials is valid."""
        try:
            client = DuolingoApiClient(username)
            await self.hass.async_add_executor_job(
                client.get_streak_data,
            )

            return True
        except Exception:  # pylint: disable=broad-except
            pass
        return False

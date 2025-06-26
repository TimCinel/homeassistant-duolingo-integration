"""Test Duolingo config flow."""

from unittest.mock import patch

from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResultType

from custom_components.duolingo.const import CONF_USERNAME, DOMAIN


async def test_form_user(hass: HomeAssistant):
    """Test user config flow."""
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )
    assert result["type"] == FlowResultType.FORM
    assert result["errors"] == {}

    with patch(
        "custom_components.duolingo.config_flow.DuolingoApiClient",
    ) as mock_client:
        mock_client.return_value.get_streak_data.return_value = {
            "username": "testuser",
            "streak_extended_today": True,
            "site_streak": 42,
        }

        result2 = await hass.config_entries.flow.async_configure(
            result["flow_id"],
            {
                CONF_USERNAME: "testuser",
            },
        )
        await hass.async_block_till_done()

    assert result2["type"] == FlowResultType.CREATE_ENTRY
    assert result2["title"] == "testuser"
    assert result2["data"] == {
        CONF_USERNAME: "testuser",
    }


async def test_form_invalid_auth(hass: HomeAssistant):
    """Test invalid authentication."""
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )

    with patch(
        "custom_components.duolingo.config_flow.DuolingoApiClient",
    ) as mock_client:
        mock_client.return_value.get_streak_data.side_effect = ValueError(
            "No user found"
        )

        result2 = await hass.config_entries.flow.async_configure(
            result["flow_id"],
            {
                CONF_USERNAME: "invaliduser",
            },
        )

    assert result2["type"] == FlowResultType.FORM
    assert result2["errors"]["base"] == "auth"


async def test_form_connection_error(hass: HomeAssistant):
    """Test connection error."""
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )

    with patch(
        "custom_components.duolingo.config_flow.DuolingoApiClient",
    ) as mock_client:
        mock_client.return_value.get_streak_data.side_effect = Exception(
            "Connection error"
        )

        result2 = await hass.config_entries.flow.async_configure(
            result["flow_id"],
            {
                CONF_USERNAME: "testuser",
            },
        )

    assert result2["type"] == FlowResultType.FORM
    assert result2["errors"]["base"] == "auth"

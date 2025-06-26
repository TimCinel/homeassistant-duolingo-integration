"""Support for a Duolingo data sensor."""

import logging
from typing import Any

from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from custom_components.duolingo.entity import DuolingoEntity

from .const import (
    DOMAIN,
)

_LOGGER = logging.getLogger(__name__)

ATTR_DUO_STREAK_LENGTH = "streak_length"
ATTR_DUO_STREAK_EXTENDED_TODAY = "streak_extended_today"


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_devices: AddEntitiesCallback,
) -> None:
    """Set up binary_sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_devices([DuolingualBinarySensor(coordinator, entry)])


class DuolingualBinarySensor(DuolingoEntity, BinarySensorEntity):
    """Implementation of the Duolingual binary sensor."""

    @property
    def name(self) -> str:
        """Return the name of the binary_sensor."""
        return f"{DOMAIN}_{self.coordinator.data.get('username')}"

    @property
    def is_on(self) -> bool:
        """Return true if the binary sensor is on."""
        return self.coordinator.data.get("streak_extended_today", False)

    @property
    def icon(self) -> str:
        """Return the icon to use in the frontend."""
        return "mdi:fire"

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return the state attributes."""
        return {
            ATTR_DUO_STREAK_EXTENDED_TODAY: self.coordinator.data.get(
                "streak_extended_today", False
            ),
            ATTR_DUO_STREAK_LENGTH: self.coordinator.data.get("site_streak", 0),
        }

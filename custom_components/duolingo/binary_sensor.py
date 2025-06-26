"""Support for a Duolingo data sensor."""

import logging

from homeassistant.components.binary_sensor import BinarySensorEntity

from custom_components.duolingo.entity import DuolingoEntity

from .const import (
    DOMAIN,
)

_LOGGER = logging.getLogger(__name__)

ATTR_DUO_STREAK_LENGTH = "streak_length"
ATTR_DUO_STREAK_EXTENDED_TODAY = "streak_extended_today"


async def async_setup_entry(hass, entry, async_add_devices):
    """Setup binary_sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_devices([DuolingualBinarySensor(coordinator, entry)])


class DuolingualBinarySensor(DuolingoEntity, BinarySensorEntity):
    """Implementation of the Duolingual binary sensor."""

    @property
    def name(self):
        """Return the name of the binary_sensor."""
        return f"{DOMAIN}_{self.coordinator.data.get('username')}"

    @property
    def is_on(self):
        """Return true if the binary sensor is on."""
        return self.coordinator.data.get("streak_extended_today", False)

    @property
    def icon(self):
        """Return the icon to use in the frontend."""
        return "mdi:fire"

    @property
    def extra_state_attributes(self):
        """Return the state attributes."""
        attrs = {
            ATTR_DUO_STREAK_EXTENDED_TODAY: self.coordinator.data.get(
                "streak_extended_today", False
            ),
            ATTR_DUO_STREAK_LENGTH: self.coordinator.data.get("site_streak", 0),
        }
        return attrs

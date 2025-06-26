"""Support for Duolingo streak sensors."""

import logging

from homeassistant.components.sensor import SensorEntity
from homeassistant.const import ATTR_ATTRIBUTION

from custom_components.duolingo.entity import DuolingoEntity

from .const import (
    DOMAIN,
)

_LOGGER = logging.getLogger(__name__)

ATTRIBUTION = "Data provided by Duolingo"


async def async_setup_entry(hass, entry, async_add_devices):
    """Setup sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_devices([DuolingoStreakSensor(coordinator, entry)])


class DuolingoStreakSensor(DuolingoEntity, SensorEntity):
    """Implementation of the Duolingo streak sensor."""

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"{DOMAIN}_{self.coordinator.data.get('username')}_streak"

    @property
    def unique_id(self):
        """Return a unique ID to use for this entity."""
        return f"{DOMAIN}_{self.coordinator.data.get('username')}_streak"

    @property
    def native_value(self):
        """Return the state of the sensor."""
        return self.coordinator.data.get("site_streak", 0)

    @property
    def native_unit_of_measurement(self):
        """Return the unit of measurement."""
        return "days"

    @property
    def icon(self):
        """Return the icon to use in the frontend."""
        return "mdi:calendar"

    @property
    def extra_state_attributes(self):
        """Return the state attributes."""
        attrs = {
            ATTR_ATTRIBUTION: ATTRIBUTION,
            "username": self.coordinator.data.get("username"),
            "streak_extended_today": self.coordinator.data.get(
                "streak_extended_today", False
            ),
        }
        return attrs

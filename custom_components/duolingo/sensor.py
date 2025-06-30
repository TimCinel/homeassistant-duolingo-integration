"""Support for Duolingo streak sensors."""

import logging
from typing import Any

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import ATTR_ATTRIBUTION
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from custom_components.duolingo.entity import DuolingoEntity

from .const import (
    DOMAIN,
)

_LOGGER = logging.getLogger(__name__)

ATTRIBUTION = "Data provided by Duolingo"


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_devices: AddEntitiesCallback,
) -> None:
    """Set up sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_devices(
        [
            DuolingoStreakSensor(coordinator, entry),
            DuolingoXPSensor(coordinator, entry),
        ]
    )


class DuolingoStreakSensor(DuolingoEntity, SensorEntity):
    """Implementation of the Duolingo streak sensor."""

    @property
    def name(self) -> str:
        """Return the name of the sensor."""
        return f"{DOMAIN}_{self.coordinator.data.get('username')}_streak"

    @property
    def unique_id(self) -> str:
        """Return a unique ID to use for this entity."""
        return f"{DOMAIN}_{self.coordinator.data.get('username')}_streak"

    @property
    def native_value(self) -> int:
        """Return the state of the sensor."""
        return self.coordinator.data.get("site_streak", 0)

    @property
    def native_unit_of_measurement(self) -> str:
        """Return the unit of measurement."""
        return "days"

    @property
    def icon(self) -> str:
        """Return the icon to use in the frontend."""
        return "mdi:calendar"

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return the state attributes."""
        return {
            ATTR_ATTRIBUTION: ATTRIBUTION,
            "username": self.coordinator.data.get("username"),
            "streak_extended_today": self.coordinator.data.get(
                "streak_extended_today", False
            ),
        }


class DuolingoXPSensor(DuolingoEntity, SensorEntity):
    """Implementation of the Duolingo XP sensor."""

    @property
    def name(self) -> str:
        """Return the name of the sensor."""
        return f"{DOMAIN}_{self.coordinator.data.get('username')}_xp"

    @property
    def unique_id(self) -> str:
        """Return a unique ID to use for this entity."""
        return f"{DOMAIN}_{self.coordinator.data.get('username')}_xp"

    @property
    def native_value(self) -> int:
        """Return the state of the sensor."""
        return self.coordinator.data.get("total_xp", 0)

    @property
    def native_unit_of_measurement(self) -> str:
        """Return the unit of measurement."""
        return "XP"

    @property
    def icon(self) -> str:
        """Return the icon to use in the frontend."""
        return "mdi:star"

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return the state attributes."""
        return {
            ATTR_ATTRIBUTION: ATTRIBUTION,
            "username": self.coordinator.data.get("username"),
        }

"""DuolingoEntity class."""

from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
)


class DuolingoEntity(CoordinatorEntity):
    """Base entity for Duolingual integration."""

    def __init__(
        self,
        coordinator: DataUpdateCoordinator,
        config_entry: ConfigEntry,
    ) -> None:
        """Initialize the entity."""
        super().__init__(coordinator)
        self.config_entry = config_entry

    @property
    def unique_id(self) -> str:
        """Return a unique ID to use for this entity."""
        return self.config_entry.entry_id

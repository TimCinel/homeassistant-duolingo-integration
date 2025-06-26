"""Test Duolingo sensors."""

from unittest.mock import MagicMock

from custom_components.duolingo.binary_sensor import DuolingualBinarySensor
from custom_components.duolingo.sensor import DuolingoStreakSensor


def test_binary_sensor_is_on():
    """Test binary sensor is_on when streak extended today."""
    coordinator = MagicMock()
    coordinator.data = {
        "username": "testuser",
        "streak_extended_today": True,
        "site_streak": 42,
    }
    entry = MagicMock()

    sensor = DuolingualBinarySensor(coordinator, entry)

    assert sensor.is_on is True
    assert sensor.name == "duolingo_testuser"
    assert sensor.icon == "mdi:fire"


def test_binary_sensor_is_off():
    """Test binary sensor is_on when streak not extended today."""
    coordinator = MagicMock()
    coordinator.data = {
        "username": "testuser",
        "streak_extended_today": False,
        "site_streak": 42,
    }
    entry = MagicMock()

    sensor = DuolingualBinarySensor(coordinator, entry)

    assert sensor.is_on is False


def test_binary_sensor_attributes():
    """Test binary sensor attributes."""
    coordinator = MagicMock()
    coordinator.data = {
        "username": "testuser",
        "streak_extended_today": True,
        "site_streak": 42,
    }
    entry = MagicMock()

    sensor = DuolingualBinarySensor(coordinator, entry)
    attrs = sensor.extra_state_attributes

    assert attrs["streak_extended_today"] is True
    assert attrs["streak_length"] == 42


def test_streak_sensor_native_value():
    """Test streak sensor native value."""
    coordinator = MagicMock()
    coordinator.data = {
        "username": "testuser",
        "streak_extended_today": True,
        "site_streak": 42,
    }
    entry = MagicMock()

    sensor = DuolingoStreakSensor(coordinator, entry)

    assert sensor.native_value == 42
    assert sensor.name == "duolingo_testuser_streak"
    assert sensor.unique_id == "duolingo_testuser_streak"
    assert sensor.native_unit_of_measurement == "days"
    assert sensor.icon == "mdi:calendar"


def test_streak_sensor_no_streak():
    """Test streak sensor with no streak."""
    coordinator = MagicMock()
    coordinator.data = {
        "username": "testuser",
        "streak_extended_today": False,
        "site_streak": 0,
    }
    entry = MagicMock()

    sensor = DuolingoStreakSensor(coordinator, entry)

    assert sensor.native_value == 0


def test_streak_sensor_attributes():
    """Test streak sensor attributes."""
    coordinator = MagicMock()
    coordinator.data = {
        "username": "testuser",
        "streak_extended_today": True,
        "site_streak": 42,
    }
    entry = MagicMock()

    sensor = DuolingoStreakSensor(coordinator, entry)
    attrs = sensor.extra_state_attributes

    assert attrs["username"] == "testuser"
    assert attrs["streak_extended_today"] is True
    assert "Data provided by Duolingo" in attrs.values()

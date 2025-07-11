"""Constants for Duolingual."""

# Base component constants
NAME = "Duolingual"
DOMAIN = "duolingo"
VERSION = "0.1.0"

ISSUE_URL = "https://github.com/TimCinel/duolingual/issues"

# Platforms
BINARY_SENSOR = "binary_sensor"
SENSOR = "sensor"
PLATFORMS = [BINARY_SENSOR, SENSOR]

# Configuration and options
CONF_USERNAME = "username"


STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
This is a custom integration!
If you have any issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""

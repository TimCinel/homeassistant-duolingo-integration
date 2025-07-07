# Duolingual - A Home Assistanat integration for Duolingo

[![GitHub Release][releases-shield]][releases]
[![License][license-shield]](LICENSE)
[![CI][ci-shield]][ci]

_Home Assistant integration to track your Duolingo daily streak progress._

## About


This integration is easy to set up (just enter your username) and it creates sensors to monitor your Duolingo streak activity:

<img width="416" alt="image" src="https://github.com/user-attachments/assets/28036aaa-67e7-419b-980e-5926433aad07" />

<img width="343" alt="image" src="https://github.com/user-attachments/assets/66d0518e-802a-4a27-8397-f1fdaa551a06" />



- **🔥 Binary Sensor**: Shows if you extended your streak today (on/off)
- **📅 Streak Sensor**: Displays your current streak count in days
- **⭐ XP Sensor**: Shows your total XP across all courses

### Fork Notes

This is a fork of [sphanley/Duolinguist](https://github.com/sphanley/Duolinguist), updated to work with current Duolingo APIs and modern Home Assistant versions.

⚠️ **Important**: This integration uses reverse-engineered Duolingo APIs since no official API documentation exists. It may break if Duolingo changes their endpoints.

## Installation

### Manual Installation

1. Download the latest release or clone this repository
2. Copy the `custom_components/duolingo/` folder to your Home Assistant `custom_components/` directory
3. Restart Home Assistant
4. Go to **Settings → Devices & Services → Add Integration** and search for "Duolingual"

### HACS Installation

Add this repository as a custom repository in HACS:

1. Go to HACS → Integrations → ⋮ → Custom repositories
2. Add repository URL: `https://github.com/TimCinel/duolingual`
3. Category: Integration
4. Install and restart Home Assistant

## Configuration

1. Go to **Settings → Devices & Services → Add Integration**
2. Search for "Duolingual"
3. Enter your Duolingo username (the one visible in your profile URL)
4. The integration will create two entities for tracking your streak

## Contributions are welcome!

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)

***

[ci-shield]: https://img.shields.io/github/actions/workflow/status/TimCinel/duolingual/ci.yml?style=for-the-badge
[ci]: https://github.com/TimCinel/duolingual/actions
[license-shield]: https://img.shields.io/github/license/TimCinel/duolingual.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/TimCinel/duolingual.svg?style=for-the-badge
[releases]: https://github.com/TimCinel/duolingual/releases

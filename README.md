# Duolinguist

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)

_Component to integrate with a Duolingo account, providing the status of your daily streak._

### Fork Notes

The Duolinguist integration relies on reverse engineering due to there being no published API docs for Duolingo. Adjust your expectations, it's a little bit brittle.
[For this reason, the original author no longer supports the component](https://github.com/sphanley/Duolinguist/issues/1#issuecomment-1672419062).

This fork attempts to fix things when Duolingo's API (a moving target) changes.


## Installation (manual)

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
2. If you do not have a `custom_components` directory (folder) there, you need to create it.
3. In the `custom_components` directory (folder) create a new folder called `duolinguist`.
4. Download _all_ the files from the `custom_components/duolinguist/` directory (folder) in this repository.
5. Place the files you downloaded in the new directory (folder) you created.
6. Restart Home Assistant
7. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "Duolinguist".

## Installation (HACS)

**Untested**

Apparently it's possible to [add custom repositories to HACS](https://hacs.xyz/docs/faq/custom_repositories).

Try adding this repository. If it works, let me know and I'll update this section =)

## Configuration

This integration utilizes the UI configuration flow, and no YAML configuration is needed!

## Contributions are welcome!

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)

***

[integration_blueprint]: https://github.com/sphanley/duolinguist
[commits-shield]: https://img.shields.io/github/commit-activity/y/sphanley/duolinguist.svg?style=for-the-badge
[commits]: https://github.com/sphanley/duolinguist/commits/master
[license-shield]: https://img.shields.io/github/license/sphanley/duolinguist.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/sphanley/duolinguist.svg?style=for-the-badge
[releases]: https://github.com/sphanley/duolinguist/releases

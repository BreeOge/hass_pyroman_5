## [1.2.6.2] - 2026-09-17

- Replace SunFounder's legacy LGPIO source download/build with Ubuntu's packaged python3-lgpio.
- Avoid the old plain-HTTP abyz.me.uk download that can stall Home Assistant app builds.

## [1.2.6.1] - 2026-09-17

- Based on SunFounder's Home Assistant Pironman 5 app 1.2.6.
- Build Pironman 5 1.2.7 from source instead of using the old prebuilt image.
- Remove the OLED peripheral before installation.
- Remove the OLED-only vibration-switch peripheral.
- Remove access to /dev/i2c-1 from the Home Assistant app manifest.
- Default oled_enable to false as an additional safeguard.
- Pin the historical pm_auto 1.2.5 dependency to immutable commit 1b8b4d05b50358eb09831066304d51ddec268d19 because the old 1.2.5 ref no longer resolves.

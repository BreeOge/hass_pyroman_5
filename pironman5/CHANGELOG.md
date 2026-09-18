## [1.2.6.5] - 2026-09-17

- Stop rebuilding SunFounder Pironman from source.
- Use sunfounder/aarch64-pironman5:1.2.6 as the base image.
- Patch the installed Pironman variant definitions to remove OLED, OLED sleep, and the OLED-only vibration switch.
- Patch installed pm_auto OLED/vibration initialization and update guards as defense in depth.
- Keep /dev/i2c-1 unavailable to the app.
- Eliminate build-time apt, GitHub clone, pm_auto source install, dashboard source install, and pip dependency downloads.

## [1.2.6.4] - 2026-09-17

- Use current app_config mapping.

## [1.2.6.3] - 2026-09-17

- Migrate the local app build to Home Assistant's current Docker BuildKit format.
- Set the Ubuntu base image directly in Dockerfile instead of relying on legacy build.yaml.
- Add required Home Assistant image labels.
- Add repository.yaml for current Home Assistant app repository discovery.

## [1.2.6.2] - 2026-09-17

- Replace SunFounder's legacy LGPIO source download/build with Ubuntu's packaged python3-lgpio.
- Avoid the old plain-HTTP abyz.me.uk download that can stall Home Assistant app builds.

## [1.2.6.1] - 2026-09-17

- Initial No-OLED custom build.

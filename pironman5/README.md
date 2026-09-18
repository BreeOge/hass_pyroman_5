# Pironman 5 - No OLED

A Home Assistant OS app based on SunFounder's Pironman 5 Home Assistant add-on, with OLED/I2C support permanently removed.

## Why

The stock Pironman 5 software initializes the OLED even when the dashboard reports the OLED as disabled. On Raspberry Pi 5 this can trigger repeated kernel messages from the DesignWare I2C controller:

```
i2c_designware 1f00074000.i2c: i2c_dw_handle_tx_abort: lost arbitration
```

This build removes the OLED peripheral before Pironman is installed and does not expose `/dev/i2c-1` to the app.

## Retained functionality

- Pironman dashboard
- RGB / WS2812 control
- Fan control
- CPU/GPU/system information
- NVMe/storage information
- Other non-OLED Pironman functions

The OLED-only vibration switch is also removed because its handler only wakes the OLED in the pinned Pironman release.

## Upstream versions

- Home Assistant app base: SunFounder Pironman 5 app 1.2.6
- Pironman software: 1.2.7
- pm_auto: historical 1.2.5 commit pinned by SHA
- Adafruit Blinka: 8.55.0

## Install

Add this repository to Home Assistant under **Settings -> Apps -> App Store -> Repositories**, then install **Pironman 5 - No OLED**.

Stop and disable the stock SunFounder Pironman 5 app before starting this one.

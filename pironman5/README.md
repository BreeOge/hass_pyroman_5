# Pironman 5 - No OLED

A Home Assistant OS app based on SunFounder's Pironman 5 Home Assistant image, with OLED/I2C support permanently removed.

## Why

The stock Pironman 5 software initializes the OLED even when the dashboard reports the OLED as disabled. On Raspberry Pi 5 this can trigger repeated kernel messages from the DesignWare I2C controller:

```
i2c_designware 1f00074000.i2c: i2c_dw_handle_tx_abort: lost arbitration
```

This build uses SunFounder's existing Pironman 5 image as its base and patches the installed software in-place. It does not build Pironman from source and it does not expose `/dev/i2c-1` to the app.

## What is removed

- OLED peripheral
- OLED sleep peripheral
- OLED-only vibration switch
- OLED initialization/update paths in pm_auto
- /dev/i2c-1 access from the Home Assistant app manifest

## Retained functionality

- Pironman dashboard
- RGB / WS2812 control
- Fan control
- CPU/GPU/system information
- NVMe/storage information
- Other non-OLED Pironman functions

## Upstream base

- SunFounder Home Assistant image: `sunfounder/aarch64-pironman5:1.2.6`
- Pironman software inside that image: 1.2.7

## Install

Add this repository to Home Assistant under **Settings -> Apps -> App Store -> Repositories**, then install **Pironman 5 - No OLED**.

The stock SunFounder Pironman 5 app should remain uninstalled or stopped.

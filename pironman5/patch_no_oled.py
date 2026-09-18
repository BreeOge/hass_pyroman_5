#!/usr/bin/env python3
from pathlib import Path
import sys

root = Path(sys.argv[1] if len(sys.argv) > 1 else "/pironman5")

variant_files = [
    root / "pironman5" / "variants" / "pironman5.py",
    root / "pironman5" / "variants" / "pironman5v10.py",
]

# These peripherals are tied to the OLED path in Pironman 5 1.2.7.
# Removing them prevents pm_auto from constructing the OLED object or
# registering the vibration-switch callback that only wakes the OLED.
remove_entries = {
    '"oled",',
    "'oled',",
    '"oled_sleep",',
    "'oled_sleep',",
    '"vibration_switch",',
    "'vibration_switch',",
}

for path in variant_files:
    text = path.read_text()
    original = text

    lines = []
    for line in text.splitlines(keepends=True):
        if line.strip() in remove_entries:
            continue
        lines.append(line)

    text = "".join(lines)
    text = text.replace('"oled_enable": True', '"oled_enable": False')
    text = text.replace("'oled_enable': True", "'oled_enable': False")

    if text == original:
        raise RuntimeError(f"No OLED changes were made to {path}")

    path.write_text(text)

# SunFounder's Pironman 5 1.2.7 installer references pm_auto@1.2.5,
# but that old ref no longer resolves on GitHub. Pin the exact historical
# commit that contains pm_auto version 1.2.5 so fresh rebuilds remain possible.
install_py = root / "install.py"
text = install_py.read_text()
old = "git+https://github.com/sunfounder/pm_auto.git@1.2.5"
new = "git+https://github.com/sunfounder/pm_auto.git@1b8b4d05b50358eb09831066304d51ddec268d19"

if old not in text:
    raise RuntimeError("Expected pm_auto 1.2.5 dependency was not found in install.py")

install_py.write_text(text.replace(old, new))

print("Pironman 5 No-OLED patch applied successfully.")

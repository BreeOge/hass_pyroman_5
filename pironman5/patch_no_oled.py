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

install_py = root / "install.py"
text = install_py.read_text()

# SunFounder's old installer downloads lgpio over plain HTTP from abyz.me.uk.
# The Home Assistant image installs Ubuntu's packaged python3-lgpio instead,
# so remove the legacy download/build hook entirely.
lgpio_hook = """    'run_commands_before_install': {
        'Install LGPIO': 'bash install_lgpio.sh',
    },
"""
if lgpio_hook not in text:
    raise RuntimeError("Expected legacy LGPIO install hook was not found")
text = text.replace(lgpio_hook, "")

# The old pm_auto@1.2.5 ref no longer resolves. Pin its exact historical commit.
old = "git+https://github.com/sunfounder/pm_auto.git@1.2.5"
new = "git+https://github.com/sunfounder/pm_auto.git@1b8b4d05b50358eb09831066304d51ddec268d19"
if old not in text:
    raise RuntimeError("Expected pm_auto 1.2.5 dependency was not found in install.py")
text = text.replace(old, new)

install_py.write_text(text)

print("Pironman 5 No-OLED patch applied successfully.")

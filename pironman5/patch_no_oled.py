#!/usr/bin/env python3
from pathlib import Path

roots = [
    Path("/opt/pironman5/venv/lib"),
    Path("/opt/pironman5"),
]

# Patch the installed Pironman variant definitions so OLED-related peripherals
# are no longer advertised at all.
variant_files = []
for root in roots:
    if root.exists():
        variant_files.extend(root.rglob("pironman5/variants/pironman5.py"))
        variant_files.extend(root.rglob("pironman5/variants/pironman5v10.py"))

variant_files = list(dict.fromkeys(variant_files))
if not variant_files:
    raise RuntimeError("Could not locate installed Pironman variant files")

remove_entries = {
    '"oled",',
    "'oled',",
    '"oled_sleep",',
    "'oled_sleep',",
    '"vibration_switch",',
    "'vibration_switch',",
}

variant_changes = 0
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

    if text != original:
        path.write_text(text)
        variant_changes += 1

if variant_changes == 0:
    raise RuntimeError("Pironman variant files were found but no OLED changes were applied")

# Defense in depth: also prevent the installed pm_auto 1.2.x code from ever
# constructing or updating OLED/vibration objects even if a peripheral list
# containing those names is supplied later.
pm_files = []
for root in roots:
    if root.exists():
        pm_files.extend(root.rglob("pm_auto/pm_auto.py"))

pm_files = list(dict.fromkeys(pm_files))
if not pm_files:
    raise RuntimeError("Could not locate installed pm_auto/pm_auto.py")

pm_changes = 0
replacements = {
    "if 'oled' in peripherals:": "if False and 'oled' in peripherals:",
    'if "oled" in peripherals:': 'if False and "oled" in peripherals:',
    "if 'oled' in self.peripherals:": "if False and 'oled' in self.peripherals:",
    'if "oled" in self.peripherals:': 'if False and "oled" in self.peripherals:',
    "if 'vibration_switch' in peripherals:": "if False and 'vibration_switch' in peripherals:",
    'if "vibration_switch" in peripherals:': 'if False and "vibration_switch" in peripherals:',
    "if 'vibration_switch' in self.peripherals:": "if False and 'vibration_switch' in self.peripherals:",
    'if "vibration_switch" in self.peripherals:': 'if False and "vibration_switch" in self.peripherals:',
}

for path in pm_files:
    text = path.read_text()
    original = text
    for old, new in replacements.items():
        text = text.replace(old, new)

    if text != original:
        path.write_text(text)
        pm_changes += 1

if pm_changes == 0:
    raise RuntimeError("pm_auto was found but no OLED/vibration guards were patched")

print(f"Patched {variant_changes} Pironman variant file(s)")
print(f"Patched {pm_changes} pm_auto file(s)")
print("OLED/I2C path permanently disabled.")

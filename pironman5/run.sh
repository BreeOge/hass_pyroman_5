#!/usr/bin/with-contenv /usr/bin/bashio

# Pironman 5 service. OLED/I2C support has been removed at image build time.
/opt/pironman5/venv/bin/pironman5-service --config-path /data/config.json start

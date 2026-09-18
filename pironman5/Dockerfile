ARG BUILD_FROM
FROM $BUILD_FROM

# Dependencies retained from SunFounder's original Home Assistant add-on.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        git \
        python3 \
        python3-pip \
        python3-setuptools \
        libraspberrypi-bin \
    && rm -rf /var/lib/apt/lists/*

# Use the same Pironman 5 release as SunFounder's HA add-on.
RUN git clone https://github.com/sunfounder/pironman5.git -b 1.2.7 /pironman5

# Permanently remove the OLED/I2C peripheral before installation.
COPY patch_no_oled.py /tmp/patch_no_oled.py
RUN python3 /tmp/patch_no_oled.py /pironman5 \
    && rm -f /tmp/patch_no_oled.py

# Install Pironman without auto-start/reboot/device-tree/module changes.
RUN cd /pironman5 \
    && python3 install.py \
        --skip-auto-start \
        --skip-reboot \
        --skip-dtoverlay \
        --skip-modules \
        --plain-text

# Match SunFounder's original compatibility pin.
RUN /opt/pironman5/venv/bin/pip install adafruit-blinka==8.55.0

WORKDIR /data

COPY run.sh /run.sh
RUN chmod a+x /run.sh

CMD ["/run.sh"]

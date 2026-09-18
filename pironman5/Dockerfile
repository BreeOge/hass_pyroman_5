FROM sunfounder/aarch64-pironman5:1.2.6

ARG BUILD_VERSION
ARG BUILD_ARCH

LABEL \
  io.hass.version="${BUILD_VERSION}" \
  io.hass.type="app" \
  io.hass.arch="${BUILD_ARCH}"

# Patch the already-installed SunFounder software in-place.
COPY patch_no_oled.py /tmp/patch_no_oled.py
RUN python3 /tmp/patch_no_oled.py \
    && rm -f /tmp/patch_no_oled.py

WORKDIR /data

COPY run.sh /run.sh
RUN chmod a+x /run.sh

CMD ["/run.sh"]

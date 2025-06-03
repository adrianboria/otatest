# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD

firmware_url = "https://raw.githubusercontent.com/adrianboria/otatest/"
ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "boot.py")
ota_updater.download_and_install_update_if_available()

#------------------

import machine
import time

led = machine.Pin(2,machine.Pin.OUT)

while True:
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1)


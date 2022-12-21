import time

import network

from wifi import PASSWORD, SSID, WIFI_CONFIG


def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.ifconfig(WIFI_CONFIG)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)

    print("Connecting to wifi", end="")
    max_wait = 10 # seconds
    while max_wait and not wlan.isconnected():
        max_wait -= 1
        print(".", end="")
        time.sleep(1)
    
    print("")

    if wlan.isconnected():
        print(f"Connected: {wlan.ifconfig()[0]}") # ip
    else:
        raise RuntimeError(f"Couldn't connect to Wifi. Error: {wlan.status()}")

    

# Basic Wifi Scanner Code 
# ESP8266


import network
import time

# Set up WiFi in station mode
wlan = network.WLAN(network.STA_IF)
wlan.active(True)


print(wlan.active())


# Disconnect from any previously connected WiFi network
wlan.disconnect()

time.sleep(1)

print("Scanning for WiFi networks...")



# Scan for available networks
networks = wlan.scan()

if len(networks) == 0:
    print("No networks found")
else:
    print(f"{len(networks)} networks found")
    for idx, network in enumerate(networks):
        ssid = network[0].decode('utf-8')
        rssi = network[3]
        encryption = network[4]
        encryption_type = "Open" if encryption == 0 else "Secured"
        print(f"{idx+1}: SSID: {ssid}, RSSI: {rssi}, Encryption: {encryption_type}")

time.sleep(5)


def wifi_me():
    import network
    print('[wifi_me]')

    SSID = '<***redacted***>'
    password = '<***redacted***>'

    wlan = network.WLAN(network.STA_IF)  # STA_IF means station interface
    ap = network.WLAN(network.AP_IF)  # AP_IF means access point
    print('Shutting down access point...')
    ap.active(False)  # shut down access point

    if not wlan.isconnected():
        SSID = 'FraggleRock'
        password = '47Durney20'
        print('Connecting to wifi network {}...'.format(SSID))
        wlan.active(True)
        wlan.connect(SSID, password)
        if wlan.config('mac') == b'\\\xcf\x7f\x87\x1cf':
            wlan.config(dhcp_hostname="mcu0")
        else:
            wlan.config(dhcp_hostname="mcu1")
        while not wlan.isconnected():
            pass
    else:
        print('Already connected to wifi network {}...'.format(SSID))

    print('hostname: ', wlan.config('dhcp_hostname'))
    print(wlan.ifconfig())
    (ip, netmask, gateway, dns) = wlan.ifconfig()

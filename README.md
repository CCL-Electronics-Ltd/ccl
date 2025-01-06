[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/custom-components/hacs)

# CCL Electronics

The CCL Electronics integration for Home Assistant. It reads sensor data from CCL weather stations on the local network.

## Configurations

1. Prepare the **WSLink** app in your mobile device.
2. Open **HACS** in the Home Assistant sidebar.
2. Search for **CCL Electronics** repository and click on the item in the **Available for download** list.
3. On the overview page, click the **Download** button in the bottom-right corner.
4. Restart Home Assistant once the integration has been downloaded or updated.
5. In the **Settings** -> **Devices & services**, click **Add integration** and select **CCL Electronics** from the pop-up menu.
6. Follow the instructions and press **Submit** to generate the following details.  
   For example:
   - Server IP: '192.168.1.154' (example: use your Home Assistant IP address)
   - Port: '8123' (constant)
   - Path: '/webhook/api/54fa0b9c' (automatically generated)
7. Open the **WSLink** app on your mobile device.
8. Connect your mobile device to your weather station in AP mode.
9. In the WSLink app, go to **Weather Server** → **Home Assistant**, and enter the Server IP, Port, and Path assigned by Home Assistant.
10. Save

## Sensors

One weather station includes 3 components. Each of them represents a "device" in Home Assistant:

- Console & Sensor Array

  The basic sensors of a weather station, provide the bare essential data:
  - Air pressure
  - Dew point, Feels like, Heat index, WBGT & Wind chill
  - Indoor/Outdoor Temperature
  - Indoor/Outdoor Humidity
  - Light intensity
  - Rainfall & Rain rate
  - UVI
  - Wind direction, Wind gust & Wind speed

- Other Sensors

  Optional sensor channels if added, including:
  - Air quality
  - Leakage
  - Lightning
  - Thermo‐hygrometer

- Status

  - Battery
  - Connection

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
6. Follow the instructions shown to finish your configuration.

## Sensors
Data received from one weather station set will be split into 3 sensor groups (or cards in displaying). Each of them represents a "device" in Home Assistant:
- Console & Sensor Array
- Other Sensors
- Status

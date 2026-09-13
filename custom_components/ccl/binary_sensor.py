"""Platform for binary sensor integration."""

from __future__ import annotations

import dataclasses
from typing import Any, override

from aioccl import CCLSensor, CCLSensorTypes
from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntity,
    BinarySensorEntityDescription,
)
from homeassistant.config_entries import AddConfigEntryEntitiesCallback
from homeassistant.core import HomeAssistant

from .coordinator import CCLConfigEntry, CCLCoordinator
from .entity import CCLEntity

CCL_BINARY_SENSOR_DESCRIPTIONS: dict[str, BinarySensorEntityDescription] = {
    CCLSensorTypes.BATTERY_BINARY: BinarySensorEntityDescription(
        key="BATTERY_BINARY",
        device_class=BinarySensorDeviceClass.BATTERY,
    ),
    CCLSensorTypes.CONNECTION: BinarySensorEntityDescription(
        key="CONNECTION",
        device_class=BinarySensorDeviceClass.CONNECTIVITY,
    ),
    CCLSensorTypes.LEAKAGE: BinarySensorEntityDescription(
        key="LEAKAGE",
        translation_key="leakage",
    ),
}


async def async_setup_entry(
    hass: HomeAssistant,
    entry: CCLConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Add binary sensors for passed config entry in HA."""
    coordinator = entry.runtime_data

    def _new_binary_sensors(sensors: dict[str, CCLSensor]) -> bool:
        """Add binary sensors to the data entry."""
        sensor_entities = []

        for sensor in sensors.values():
            if sensor.sensor_type in CCL_BINARY_SENSOR_DESCRIPTIONS:
                description = CCL_BINARY_SENSOR_DESCRIPTIONS[sensor.sensor_type]
                replace_args: dict[str, Any] = {
                    "key": sensor.key,
                }
                if description.translation_key is None:
                    replace_args["name"] = sensor.name
                entity_description = dataclasses.replace(
                    description,
                    **replace_args,
                )
                sensor_entities.append(
                    CCLBinarySensorEntity(
                        coordinator,
                        entity_description,
                        sensor,
                    )
                )

        async_add_entities(sensor_entities)

        return True

    coordinator.device.set_new_sensor_callback(_new_binary_sensors)

    if coordinator.data is not None:
        _new_binary_sensors(coordinator.data)


class CCLBinarySensorEntity(CCLEntity, BinarySensorEntity):
    """Representation of a Binary Sensor."""

    def __init__(
        self,
        coordinator: CCLCoordinator,
        entity_description: BinarySensorEntityDescription,
        internal: CCLSensor,
    ) -> None:
        """Initialize a CCL Sensor Entity."""
        super().__init__(internal, coordinator)

        self.entity_description = entity_description

    @override
    @property
    def native_value(self) -> int | float | str | None:
        """Return the state of the sensor."""
        return self._internal.value
    
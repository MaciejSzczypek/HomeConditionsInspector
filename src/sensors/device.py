from abc import ABC, abstractmethod
from typing import Type

import adafruit_dht
import board


class TempHumSensor(ABC):
    @abstractmethod
    def __init__(self) -> None:
        raise NotImplementedError

    @property
    @abstractmethod
    def temperature(self) -> float:
        raise NotImplementedError

    @property
    @abstractmethod
    def humidity(self) -> float:
        raise NotImplementedError

    @abstractmethod
    def exit(self) -> None:
        raise NotImplementedError


class DHT22Device(TempHumSensor):
    def __init__(self) -> None:
        self._device = adafruit_dht.DHT22(board.D4, use_pulseio=False)

    @property
    def temperature(self) -> float:
        return self._device.temperature

    @property
    def humidity(self) -> float:
        return self._device.temperature

    def exit(self) -> None:
        self._device.exit()


def setup_sensor_device(sensor: Type[TempHumSensor] = DHT22Device) -> TempHumSensor:
    return sensor()

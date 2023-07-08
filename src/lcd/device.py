from abc import ABC, abstractmethod

from RPLCD.i2c import CharLCD

from src.conf.config import LCDConfig
from typing import Tuple, Type


class LCDDevice(ABC):
    @abstractmethod
    def __init__(self, *args, **kwargs) -> None:
        raise NotImplementedError

    @abstractmethod
    def create_custom_symbol(self, *args, **kwargs) -> None:
        pass


class CharLCDDevice(LCDDevice):
    def __init__(self, config: LCDConfig) -> None:
        self._device = CharLCD(
            i2c_expander=config.i2c_expander,
            address=config.address,
            port=config.port,
            cols=config.cols,
            rows=config.rows,
            backlight_enabled=config.backlight_enabled,
        )

    def create_custom_symbol(self, mem_location: int, symbol: Tuple[int]) -> None:
        self._device.create_char(mem_location, symbol)


def setup_lcd_device(
    config: LCDConfig, lcd: Type[LCDDevice] = CharLCDDevice
) -> LCDDevice:
    return lcd(config)

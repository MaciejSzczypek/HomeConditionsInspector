import datetime
import time

from aws.s3 import upload_file_to_s3
from conf.config import get_config
from sensors.device import setup_sensor_device
from lcd.custom_symbols import degree_symbol
from lcd.device import setup_lcd_device
from loggers.conditions_logger import log_conditions_to_file, Conditions


def run():
    config = get_config()
    dht_device = setup_sensor_device()
    lcd = setup_lcd_device(config.lcd)

    lcd.create_custom_symbol(0, degree_symbol)

    log_file_path = "/tmp/conditions.csv"
    while True:
        try:
            t = datetime.datetime.now()
            lcd.clear()
            lcd.write_string(f"Temp.: {dht_device.temperature}\x00C")
            lcd.crlf()
            lcd.write_string(f"Hum.: {dht_device.humidity}%")
            log_conditions_to_file(
                log_file_path,
                conditions=Conditions(
                    timestamp=t.timestamp(),
                    temperature=dht_device.temperature,
                    humidity=dht_device.humidity,
                ),
            )

        except RuntimeError:
            time.sleep(2)
            continue
        except Exception as error:
            dht_device.exit()
            raise error

        upload_file_to_s3(config.aws.s3, log_file_path)
        time.sleep(60)

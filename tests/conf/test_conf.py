from src.conf.config import (
    get_config,
    AWSConfig,
    LCDConfig,
    SensorsConfig,
    LogsConfig,
)
from tests.test_data import TEST_CONFIG_DATA_PATH

expected_config_aws = AWSConfig(
    {
        "s3": {
            "aws_access_key_id": "test_aws_access_key_id",
            "aws_secret_access_key": "test_aws_secret_access_key",
            "bucket": "test_bucket",
            "push_file_every_n_seconds": 0,
            "push_file_automatically": False,
        }
    }
)

expected_config_lcd = LCDConfig(
    {
        "refresh_every_n_seconds": 0,
        "i2c_expander": "test_i2c_expander",
        "address": 39,
        "port": 1,
        "cols": 16,
        "rows": 2,
        "backlight_enabled": True,
    }
)

expected_config_sensors = SensorsConfig({"dht": {"read_every_n_seconds": 0}})
expected_config_logs = LogsConfig(
    {"log_file_path": "test_file_path", "log_every_n_seconds": 0},
)


def test_get_config():
    config = get_config(TEST_CONFIG_DATA_PATH)
    assert config.aws == expected_config_aws
    assert config.lcd == expected_config_lcd
    assert config.sensors == expected_config_sensors
    assert config.logs == expected_config_logs

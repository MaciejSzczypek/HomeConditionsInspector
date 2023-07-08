import yaml
from dataclasses import dataclass
from typing import Dict, Optional
import os


_DEFAULT_CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.yml")


@dataclass
class S3Config:
    aws_access_key_id: str
    aws_secret_access_key: str
    bucket: str

    def __init__(self, config_dict: Dict) -> None:
        self.aws_access_key_id = config_dict.get("aws_access_key_id")
        self.aws_secret_access_key = config_dict.get("aws_secret_access_key")
        self.bucket = config_dict.get("bucket")


@dataclass
class AWSConfig:
    s3: S3Config

    def __init__(self, config_dict: Dict) -> None:
        self.s3 = S3Config(config_dict.get("s3", {}))


@dataclass
class LCDConfig:
    refresh_every_n_seconds: int
    i2c_expander: str
    address: int
    port: int
    cols: int
    rows: int
    backlight_enabled: bool

    def __init__(self, config_dict: Dict) -> None:
        self.refresh_every_n_seconds = config_dict.get("refresh_every_n_seconds")
        self.i2c_expander = config_dict.get("i2c_expander")
        self.address = config_dict.get("address")
        self.port = config_dict.get("port")
        self.cols = config_dict.get("cols")
        self.rows = config_dict.get("rows")
        self.backlight_enabled = config_dict.get("backlight_enabled")


@dataclass
class DHTConfig:
    read_every_n_seconds: int

    def __init__(self, config_dict: Dict) -> None:
        self.read_every_n_seconds = config_dict.get("read_every_n_seconds")


@dataclass
class SensorsConfig:
    dht: DHTConfig

    def __init__(self, config_dict: Dict) -> None:
        self.dht = DHTConfig(config_dict.get("dht", {}))


@dataclass
class LogsConfig:
    log_file_path: int
    log_every_n_seconds: int

    def __init__(self, config_dict: Dict) -> None:
        self.log_file_path = config_dict.get("log_file_path")
        self.log_every_n_seconds = config_dict.get("log_every_n_seconds")


@dataclass
class Config:
    aws = AWSConfig
    lcd = LCDConfig

    def __init__(self, config_dict: Dict) -> None:
        self.aws = AWSConfig(config_dict.get("aws", {}))
        self.lcd = LCDConfig(config_dict.get("lcd", {}))
        self.sensors = SensorsConfig(config_dict.get("sensors", {}))
        self.logs = LogsConfig(config_dict.get("logs", {}))


def get_config(config_path: Optional[str] = None) -> Config:
    with open(config_path or _DEFAULT_CONFIG_PATH, "r") as stream:
        config_dict = yaml.safe_load(stream)
        config = Config(config_dict)
        return config

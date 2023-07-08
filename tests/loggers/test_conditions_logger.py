from tempfile import NamedTemporaryFile

from src.loggers.conditions_logger import log_conditions_to_file
from tests.test_data.conditions import conditions_1, conditions_2


def test_log_conditions_to_file():
    temp_file = NamedTemporaryFile()
    log_conditions_to_file(temp_file.name, conditions_1)
    log_conditions_to_file(temp_file.name, conditions_2)
    assert temp_file.read() == b"1,25,50.0\n2,26,51.0\n"

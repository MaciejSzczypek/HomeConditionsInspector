from dataclasses import dataclass


@dataclass
class Conditions:
    timestamp: float
    temperature: float
    humidity: float


def log_conditions_to_file(file_path: str, conditions: Conditions) -> None:
    with open(file_path, "a") as log_file:
        log_file.write(
            f"{conditions.timestamp},{conditions.temperature},{conditions.humidity}\n"
        )

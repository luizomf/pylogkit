from collections.abc import Callable
from os import getenv
from pathlib import Path
from typing import Literal

from dotenv import load_dotenv

load_dotenv()

type LogLevel = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
ALLOWED_LEVELS: set[LogLevel] = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}


def define_setting[T](value: T, validator: Callable[[T], T] | None = None) -> T:
    if validator is not None:
        return validator(value)
    return value


def validate_path_dir(path: Path) -> Path:
    if not path.is_dir():
        raise NotADirectoryError(path)
    return path


def validate_path_file(path: Path) -> Path:
    if not path.is_file():
        raise FileNotFoundError(path)
    return path


def validate_level(level: str) -> LogLevel:
    if level not in ALLOWED_LEVELS:
        msg = f"Level {level!r} is not allowed. Use one of these: {ALLOWED_LEVELS}"
        raise ValueError(msg)
    return level


root_dir = Path(".").resolve()
logs_dir = root_dir / getenv("LOGS_DIR", "logs")
logging_config_json = root_dir / getenv("LOGGING_CONFIG_JSON", "logging.conf.json")

setup_logger_name = getenv("SETUP_LOGGER_NAME", "WARNING")
setup_logger_level = getenv("SETUP_LOGGER_LEVEL", "WARNING")

default_logger_level = getenv("DEFAULT_LOGGER_LEVEL", "WARNING")


def validate() -> None:
    global \
        root_dir, \
        logs_dir, \
        logging_config_json, \
        setup_logger_name, \
        setup_logger_level, \
        default_logger_level

    root_dir = define_setting(root_dir, validator=validate_path_dir)
    logs_dir = logs_dir / getenv("LOGS_DIR", "logs")
    logging_config_json = define_setting(
        root_dir / getenv("LOGGING_CONFIG_JSON", "logging.conf.json"),
        validator=validate_path_file,
    )

    setup_logger_name = getenv("SETUP_LOGGER_NAME", "config_setup")

    default_logger_level = define_setting(
        getenv("SETUP_LOGGER_LEVEL", "WARNING"), validator=validate_level
    )

    default_logger_level = define_setting(
        getenv("DEFAULT_LOGGER_LEVEL", "WARNING"), validator=validate_level
    )


def change_settings(
    new_root_dir: Path | None = None,
    new_logs_dir: Path | None = None,
    new_logging_config_json: Path | None = None,
    new_setup_logger_name: str | None = None,
    new_setup_logger_level: LogLevel | None = None,
    new_default_logger_level: LogLevel | None = None,
) -> None:
    global \
        root_dir, \
        logs_dir, \
        logging_config_json, \
        setup_logger_name, \
        setup_logger_level, \
        default_logger_level

    if new_root_dir:
        root_dir = define_setting(new_root_dir, validator=validate_path_dir)

    if new_logs_dir:
        logs_dir = define_setting(new_logs_dir, validator=validate_path_dir)

    if new_logging_config_json:
        logging_config_json = define_setting(
            new_logging_config_json,
            validator=validate_path_file,
        )

    if new_setup_logger_name:
        setup_logger_name = new_setup_logger_name

    if new_setup_logger_level:
        setup_logger_level = define_setting(
            new_setup_logger_level, validator=validate_level
        )

    if new_default_logger_level:
        default_logger_level = define_setting(
            new_default_logger_level, validator=validate_level
        )

"""
This type stub file was generated by pyright.
"""

import logging
from logging.handlers import QueueListener
from pylogkit.settings import LogLevel

_setup_logging_done: bool = ...
_default_queue_listener: QueueListener | None = ...
_logger = ...
def get_logger(name: str = ..., level: LogLevel | None = ...) -> logging.Logger:
    ...


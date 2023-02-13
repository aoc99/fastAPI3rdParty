import os
from loguru import logger
from typing import Callable, Optional
from app.config import Settings


class Logging:
    def __init__(self) -> None:
        self.logger = logger
        self.logger.remove()
        self.log_path = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), "..", "storage/logs/")
        self.create_log("app", "INFO")
        self.create_log("errors", "ERROR")

    @property
    def log(self):
        return self.logger

    def create_log(self, log_name: str, log_level: str, callable: Callable = None) -> None:
        # print(callable)
        if callable is None:
            def callable_filter(
                record): return record["level"].name == log_level
        else:
            callable_filter = callable
        self.logger.add(
            "".join([self.log_path, log_name + "-{time:YYYY-MM-DD}.log"]),
            level=log_level,
            filter=callable_filter,
            backtrace=Settings.log_backtrace,
            # compression=Settings.log_compress,
            diagnose=Settings.log_diagnose,
            enqueue=Settings.log_enqueue,
            # rotation=Settings.log_rotation,
            serialize=Settings.log_serialize,
        )

    def error_log(self, error: str, stacktraces: Optional[str] = None) -> None:
        self.logger.error(error)
        if stacktraces:
            self.logger.error(stacktraces)

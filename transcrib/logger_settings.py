"""
Модуль настраивает логирование библиотеки loguru

Def:
    configure_logger: Настраивает логгер с указанным уровнем логирования.
"""

import pathlib
import sys
from pathlib import Path

from dotenv import load_dotenv
from loguru import logger

dotenv_path = f"{Path((__file__)).parent.parent}/.env"
if Path(dotenv_path).is_file():
    load_dotenv(dotenv_path)
else:
    exit(f"Файл {dotenv_path} не существует.")


def configure_logger(level: str) -> None:
    """
    Настраивает логгер с указанным уровнем логирования.

    Args:
        level: Уровень логирования, который будет установлен.

    Returns:
        None
    """
    # Директория лог файлов
    log_path = pathlib.Path.joinpath(
        pathlib.Path(__file__).absolute().parent.parent,
        "logs/",
        f"{pathlib.Path(__file__).absolute().parent.parent.stem}.log",
    )
    # Максимальный размер файла логирования
    rotation_size = "50 MB"

    logger.remove()
    # logger.add(sys.stdout, level=level)
    logger.add(
        sys.stdout,
        colorize=True,
        level=level,
        format="<green>{time:YYYY-MM-DD HH:mm:ss!UTC} UTC </green> |"
        " <level>{level:^}</level> |"
        " {module}:{function}:{line} | : <level>{message}</level>",
    )

    logger.add(
        log_path,
        level=level,
        rotation=rotation_size,
        format="{time:YYYY-MM-DD HH:mm:ss!UTC} UTC | {level:^} |"
        "{module}:{function}:{line}| : {message}",
    )
    logger.debug(
        f"Настройки системы логирования: \n"
        f" путь к лог-файлу:    {log_path}\n"
        f" Уровень логирования: {level}"
    )


__all__ = ["logger"]

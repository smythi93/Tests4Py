import logging

from tests4py.logger import LOGGER


def debug():
    LOGGER.setLevel(logging.DEBUG)


def info():
    LOGGER.setLevel(logging.INFO)


def warning():
    LOGGER.setLevel(logging.WARNING)


def error():
    LOGGER.setLevel(logging.ERROR)


def deactivate():
    LOGGER.setLevel(logging.CRITICAL)

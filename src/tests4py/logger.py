import logging

LOGGER = logging.getLogger("tests4py")
logging.basicConfig(
    level=logging.INFO,
    format="%(name)s :: %(levelname)-8s :: %(message)s",
)


def init_logger(verbose=True):
    if not verbose:
        LOGGER.setLevel(logging.WARNING)

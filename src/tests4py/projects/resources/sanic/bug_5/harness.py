import logging
import sys

from sanic.log import LOGGING_CONFIG_DEFAULTS


if __name__ == "__main__":
    # argv: <base> <target> <name>
    #   base/target are logging level names; name is the Sanic app name.
    # Force the real root logger to <base>, then try to configure the
    # ``sanic.root`` logger to <target> via sanic's logging defaults and report
    # the resulting effective level of ``sanic.root``.  On the fixed build the
    # defaults expose a ``sanic.root`` logger, so the effective level becomes
    # <target>; on the buggy build the logger is named ``root`` instead, so
    # ``sanic.root`` remains at the inherited <base> level.
    base = sys.argv[1]
    target = sys.argv[2]
    name = sys.argv[3]
    logging.getLogger().setLevel(base)
    cfg = LOGGING_CONFIG_DEFAULTS
    if "sanic.root" in cfg["loggers"]:
        cfg["loggers"]["sanic.root"]["level"] = target
    from sanic import Sanic

    app = Sanic(name, log_config=cfg)
    eff = logging.getLevelName(logging.getLogger("sanic.root").getEffectiveLevel())
    print("RESULT " + str(eff))

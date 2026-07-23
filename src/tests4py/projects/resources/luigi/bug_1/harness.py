import sys
from unittest import mock

import tornado.web
import luigi.server

if __name__ == "__main__":
    mode = sys.argv[1]
    tag = sys.argv[2]
    has_metrics = mode == "metrics"
    sched = mock.MagicMock()
    handler = luigi.server.MetricsHandler(
        tornado.web.Application(), mock.MagicMock(), scheduler=sched
    )
    coll = sched._state._metrics_collector
    coll.generate_latest.return_value = mock.MagicMock() if has_metrics else None
    with mock.patch.object(handler, "write"):
        handler.get()
    called = coll.configure_http_handler.called
    print("HARNESS_OK" if called == has_metrics else "MISMATCH")

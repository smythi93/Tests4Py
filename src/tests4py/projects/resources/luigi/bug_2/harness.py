import sys

import luigi
from luigi.contrib import bigquery, gcs
from luigi.contrib.beam_dataflow import BeamDataflowJobTask

if __name__ == "__main__":
    kind = sys.argv[1]
    if kind == "bq":
        target = bigquery.BigQueryTarget(
            sys.argv[2], sys.argv[3], sys.argv[4], client="fake_client"
        )
    elif kind == "gcs":
        target = gcs.GCSTarget(sys.argv[2], client="fake_client")
    else:
        target = luigi.LocalTarget(sys.argv[2])
    print(repr(BeamDataflowJobTask.get_target_path(target)))

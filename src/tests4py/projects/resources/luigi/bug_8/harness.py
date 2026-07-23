import sys
from unittest import mock

import luigi
import luigi.contrib.redshift

if __name__ == "__main__":
    mode = sys.argv[1]
    tag = sys.argv[2]
    table_name = sys.argv[3]

    class Dummy(luigi.contrib.redshift.S3CopyToTable):
        host = "h"
        database = "d"
        user = "u"
        password = "p"
        aws_access_key_id = "key"
        aws_secret_access_key = "secret"
        copy_options = ""
        table = luigi.Parameter(default=table_name)
        columns = None

        def s3_load_path(self):
            return "s3://bucket/key"

    task = Dummy()
    conn = mock.MagicMock()
    cursor = conn.cursor.return_value
    luigi.contrib.redshift.S3CopyToTable.does_table_exist(task, conn)
    query = cursor.execute.call_args[0][0]
    if mode == "lower":
        ok = "lower(" in query
    else:
        ok = "table_exists" in query
    print("HARNESS_OK" if ok else "BAD:" + query)

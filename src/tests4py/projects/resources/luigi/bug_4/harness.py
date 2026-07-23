import sys

import luigi
import luigi.contrib.redshift


class FakeCursor:
    def execute(self, query):
        pass


if __name__ == "__main__":
    mode = sys.argv[1]
    table_name = sys.argv[2]
    cols = None if mode == "none" else (("a", "int"), ("b", "varchar"))

    class Dummy(luigi.contrib.redshift.S3CopyToTable):
        host = "h"
        database = "d"
        user = "u"
        password = "p"
        aws_access_key_id = "key"
        aws_secret_access_key = "secret"
        copy_options = ""
        table = luigi.Parameter(default=table_name)
        columns = cols

        def s3_load_path(self):
            return "s3://bucket/key"

    task = Dummy()
    luigi.contrib.redshift.S3CopyToTable.copy(task, FakeCursor(), "s3://bucket/key")
    print("HARNESS_OK")

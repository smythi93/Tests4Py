import sys
from unittest import mock

import luigi
import luigi.contrib.redshift

if __name__ == "__main__":
    mode = sys.argv[1]
    bucket = sys.argv[2]
    key = sys.argv[3]
    load_path = "s3://%s/%s" % (bucket, key)

    attrs = {
        "host": "h",
        "database": "d",
        "user": "u",
        "password": "p",
        "table": "t",
        "columns": (("c", "text"),),
        "aws_access_key_id": "k",
        "aws_secret_access_key": "s",
        "copy_options": "",
    }
    if mode == "attr":
        attrs["s3_load_path"] = load_path
    else:
        attrs["s3_load_path"] = lambda self: load_path

    cls_name = "DummyS3CopyToTable_%s_%s_%s" % (mode, bucket, key)
    Dummy = type(cls_name, (luigi.contrib.redshift.S3CopyToTable,), attrs)

    with mock.patch("luigi.contrib.redshift.RedshiftTarget"), mock.patch(
        "luigi.contrib.redshift.S3CopyToTable.copy"
    ):
        task = Dummy()
        task.run()
    print("HARNESS_OK")

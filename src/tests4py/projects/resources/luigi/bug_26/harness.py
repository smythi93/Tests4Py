import sys

from luigi.contrib.hadoop_jar import HadoopJarJobRunner, HadoopJarJobError

if __name__ == "__main__":
    mode = sys.argv[1]
    name = sys.argv[2]
    if mode == "none":
        jarval = None
    else:
        jarval = f"/no/such/dir_{name}/{name}.jar"

    class FakeJob:
        def ssh(self):
            return None

        def jar(self):
            return jarval

    try:
        HadoopJarJobRunner().run_job(FakeJob())
        print("NO_EXCEPTION")
    except HadoopJarJobError:
        print("HARNESS_OK")
    except Exception as exc:
        print("OTHER:", type(exc).__name__)

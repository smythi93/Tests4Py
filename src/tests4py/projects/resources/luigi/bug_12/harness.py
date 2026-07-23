import sys

from luigi.contrib.hdfs import get_autoconfig_client

if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "same":
        a = get_autoconfig_client()
        b = get_autoconfig_client()
        print("HARNESS_OK" if a is b else "DIFFERENT")
    else:
        c = get_autoconfig_client()
        print("HARNESS_OK" if c is not None else "NONE")

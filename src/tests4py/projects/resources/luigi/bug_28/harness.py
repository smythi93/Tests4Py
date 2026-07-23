import sys

import luigi.contrib.hive as hive

if __name__ == "__main__":
    mode = sys.argv[1]
    table = sys.argv[2]
    lower = table.lower()
    hive.run_hive_cmd = lambda *a, **k: "OK\n" + lower
    client = hive.HiveCommandClient()
    result = client.table_exists(table)
    print("HARNESS_OK" if result else "NOT_FOUND")

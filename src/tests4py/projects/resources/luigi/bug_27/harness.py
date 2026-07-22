import sys

import luigi
import luigi.configuration

if __name__ == "__main__":
    mode = sys.argv[1]
    section = sys.argv[2]
    pname = sys.argv[3]
    cfgval = sys.argv[4]

    conf = luigi.configuration.get_config()
    if not conf.has_section(section):
        conf.add_section(section)
    conf.set(section, pname, cfgval)

    p = luigi.Parameter(default="defval")
    if mode == "cfg":
        result = p.parse_from_input(pname, "", task_name=section)
    else:  # explicit
        result = p.parse_from_input(pname, cfgval)
    print(result)

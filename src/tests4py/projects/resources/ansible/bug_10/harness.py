import sys

from ansible.modules.system.pamd import PamdService

if __name__ == "__main__":
    idx = int(sys.argv[1])
    rules = [tok.split(":") for tok in sys.argv[2:]]
    content = "\n".join(" ".join(r) for r in rules)
    svc = PamdService(content)
    t, c, p = rules[idx]
    try:
        changed = svc.remove(t, c, p)
        print("OK" if (changed and not svc.has_rule(t, c, p)) else "FAIL")
    except Exception as e:
        print("ERROR:" + type(e).__name__)

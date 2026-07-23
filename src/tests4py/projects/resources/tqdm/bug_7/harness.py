import io
import sys

from tqdm import main

if __name__ == "__main__":
    desc = sys.argv[1]
    data = sys.argv[2]
    sys.argv = ["", "--desc", desc]
    sys.stdin = io.StringIO(data + "\n")
    real_out = sys.stdout
    cap = io.StringIO()
    sys.stdout = cap
    ok = True
    try:
        main(fp=io.StringIO())
    except SystemExit:
        pass
    except Exception:
        ok = False
    finally:
        sys.stdout = real_out
    if ok:
        sys.stdout.write("OUT:" + cap.getvalue().rstrip("\n") + "\n")
    else:
        sys.stdout.write("TQDM_ERROR\n")

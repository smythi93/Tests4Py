import os
from pathlib import Path


def main():
    root = Path("src", "tests4py", "projects", "resources")
    assert root.exists() and root.is_dir(), f"Wrong cwd {Path.cwd()}"
    for p in os.listdir(root):
        project = root / p
        default_req = project / "requirements.txt"
        if p != "__pycache__" and project.is_dir():
            reqs = dict()
            for b in os.listdir(project):
                bug = project / b
                if bug.is_dir():
                    req = bug / "requirements.txt"
                    if req.exists():
                        print(req)
                        with open(req, "rb") as fp:
                            content = fp.read()
                        try:
                            if b"\x00" in content:
                                raise ValueError()
                            content = content.decode("utf-8")
                        except (UnicodeDecodeError, ValueError):
                            content = (
                                content.replace(b"\xff", b"")
                                .replace(b"\xfe", b"")
                                .replace(b"\x00", b"")
                                .decode("utf-8")
                            )
                            with open(req, "w") as fp:
                                fp.write(content)
                        reqs[b] = content
            if len(reqs) > 0:
                count = dict()
                for r in reqs.values():
                    if r in count:
                        count[r] += 1
                    else:
                        count[r] = 1
                r = max(count, key=count.get)
                if count[r] > 1:
                    with open(default_req, "w") as fp:
                        fp.write(r)
                    for b in reqs:
                        if r == reqs[b]:
                            os.remove(project / b / "requirements.txt")


if __name__ == "__main__":
    main()

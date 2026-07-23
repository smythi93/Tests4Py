import subprocess
import sys

if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "cli":
        cmd = [sys.executable, "-m", "scrapy.cmdline", "version"]
    else:
        cmd = [
            sys.executable,
            "-c",
            "import scrapy; print('Scrapy ' + scrapy.__version__)",
        ]
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = proc.stdout.decode("utf-8", "replace").strip()
    line = out.splitlines()[-1] if out else ""
    if proc.returncode == 0 and line.startswith("Scrapy "):
        print("OK")
    else:
        print("ERR")

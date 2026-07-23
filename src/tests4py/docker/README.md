# Tests4Py Docker mode (optional)

An **optional** containerised backend. The default backend (host + pyenv
virtualenvs) is unchanged; nothing here runs unless you ask for it via
`t4p docker ...` or `t4p docker mode docker`. If Docker is not installed or its
daemon is not running, every command fails fast with a clear message instead of
falling over.

## Why three layers

The build cost of a Tests4Py subject is dominated by three things: the CPython
toolchain, the pinned interpreter, and the project's dependencies. Docker's
layer cache lets us pay for each **once** and reuse it:

| layer | image | contains | reused by |
|-------|-------|----------|-----------|
| environment | `tests4py-env:latest` | OS + build toolchain + pyenv + Tests4Py | every project & bug |
| project | `tests4py-project-<name>:latest` | one bug warmed → interpreter + deps cached | every bug of `<name>` |
| instance | `tests4py-instance-<name>-<id>:latest` | one specific bug checked out & built | that bug |

The env image installs Tests4Py from the **local source**, so local changes
(e.g. the merge-commit checkout fix) are baked in.

## Commands

```bash
# 1. one-time base image (OS + pyenv + t4p)
t4p docker env

# 2. per-project image, warmed by one representative bug (default -i 1)
t4p docker project -p middle

# 3. per-bug image, ready to run
t4p docker instance -p middle -i 1

# 4. run a slice inside the bug's container
t4p docker run -p middle -i 1                      # default: the bug's failing tests
t4p docker run -p middle -i 1 systemtest generate -n 4 -p 0.5
t4p docker run -p middle -i 1 test -w /work/middle_1
```

Each build step auto-builds the layer beneath it if that image is missing, so
`t4p docker run -p middle -i 1` on a clean machine will build env → project →
instance and then run — you only ever call the layer you want.

## Toggle

```bash
t4p docker mode docker   # record docker as the preferred backend
t4p docker mode pyenv    # back to the default host backend
```

The setting lives in `~/.t4p/config.ini` as `mode` and defaults to `pyenv`.

## Python API

```python
from tests4py.api import docker

docker.build_env()
docker.build_project("middle")
docker.build_instance("middle", 1)
report = docker.run_slice("middle", 1, ["systemtest", "generate", "-n", "4"])
print(report.successful, report.returncode)
```

## Manual builds

The Dockerfiles are plain templates; the build context must be the repository
root:

```bash
docker build -f src/tests4py/docker/Dockerfile.env -t tests4py-env:latest .
docker build -f src/tests4py/docker/Dockerfile.project \
  --build-arg PROJECT=middle --build-arg WARM_BUG=1 \
  -t tests4py-project-middle:latest .
docker build -f src/tests4py/docker/Dockerfile.instance \
  --build-arg PROJECT=middle --build-arg BUG=1 \
  --build-arg PROJECT_IMAGE=tests4py-project-middle:latest \
  -t tests4py-instance-middle-1:latest .
```

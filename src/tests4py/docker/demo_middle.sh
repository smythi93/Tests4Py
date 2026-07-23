#!/usr/bin/env bash
#
# End-to-end demo of the optional Tests4Py Docker backend on `middle`.
# Requires a running Docker daemon. Run from the repository root:
#
#   bash src/tests4py/docker/demo_middle.sh
#
set -euo pipefail

if ! docker version >/dev/null 2>&1; then
  echo "Docker daemon is not running. Start Docker Desktop and retry." >&2
  exit 1
fi

echo "== [1/4] environment image =="
t4p docker env

echo "== [2/4] project image (middle, warmed by bug 1) =="
t4p docker project -p middle -i 1

echo "== [3/4] instance image (middle_2) =="
t4p docker instance -p middle -i 2

echo "== [4/4] run slices inside middle_2 =="
echo "-- the bug's failing tests (expected: failures on the buggy build) --"
t4p docker run -p middle -i 2 || true
echo "-- generate 4 system tests --"
t4p docker run -p middle -i 2 systemtest generate -n 4 -p 0.5

echo "Done. Images:"
docker images --filter "reference=tests4py-*" \
  --format 'table {{.Repository}}\t{{.Tag}}\t{{.Size}}'

"""Packaged Docker assets for the optional containerised Tests4Py backend.

This package ships the three Dockerfile templates used by the layered image
build (environment -> project -> instance). The build/run logic lives in
:mod:`tests4py.api.docker`; the CLI lives in
:mod:`tests4py.cli.framework.docker` (``t4p docker ...``).
"""

from pathlib import Path

DOCKER_DIR = Path(__file__).parent

DOCKERFILE_ENV = DOCKER_DIR / "Dockerfile.env"
DOCKERFILE_PROJECT = DOCKER_DIR / "Dockerfile.project"
DOCKERFILE_INSTANCE = DOCKER_DIR / "Dockerfile.instance"

# Changelog

All notable changes to Tests4Py are documented here. The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres
to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-07-23

First stable release. **Every reproducible bug in the benchmark is now fully
supported** — each ships an oracle, a unit-test generator, a system-test
generator, a harness, a valid grammar, and a manually curated diversity set of
10 passing + 10 failing tests. All failing tests are *fault-distinguishing*:
they fail on the buggy build and pass on the fixed build.

### Coverage

- **328 / 328 reproducible bugs fully supported** across 20 projects
  (ansible, black, calculator, cookiecutter, expression, fastapi, httpie, keras,
  luigi, markup, matplotlib, middle, pysnooper, sanic, scrapy, spacy, thefuck,
  tornado, tqdm, youtubedl).
- 328 reproducible = 338 registered bugs − 10 non-evaluatable
  (`test_status_buggy == PASSING`).
- Includes 18 bugs that stock Tests4Py could not distinguish because the fixed
  build failed its own canonical test (`test_status_fixed == FAILING`): 14 were
  unlocked by the merge-commit checkout fix below and 4 by bespoke oracles that
  distinguish the fault through the diversity tests.
- The 25 keras bugs whose fault requires TensorFlow (unavailable on Apple
  Silicon) were built and validated on x86_64 Linux.

### Added

- **Optional Docker backend** (`t4p docker {env,project,instance,run,mode}`).
  A three-layer image model — environment → project → instance — so the
  expensive layers (toolchain, interpreter, dependencies) are built once and
  reused via Docker's layer cache. Configurable via `mode = pyenv | docker`
  (default `pyenv`). Fully additive: the host/pyenv backend is untouched and the
  commands degrade gracefully when no Docker daemon is available. See
  `src/tests4py/docker/README.md`.
- **Per-subject acceptance suite** (`tests/test_subjects.py`, marker
  `subjects`). Auto-discovers fully-enabled bugs and checks grammar validity,
  system/unit diversity behaviour, and system/unit generation. Excluded from the
  GitHub workflow (`pytest -m "not subjects"`); run locally with
  `pytest -m subjects`.
- Oracles, generators, harnesses, grammars, and 10+10 diversity resources for
  every supported bug.

### Fixed

- **Merge-commit checkout.** When a fix commit is a *merge*,
  `git show --name-only` lists only the merge's combined-diff files (usually just
  the test), so the actual source fix was never overlaid onto the fixed build —
  leaving it byte-identical to the buggy build. Checkout now detects a merge fix
  commit (`git rev-list --parents -n 1 HEAD`) and locates the changed files via
  `git diff <buggy>..<fixed>` in that case. Non-merge commits keep the exact
  `git show` path, so there is no change in behaviour for them.

### Changed

- Version bumped to 1.0.0.

[1.0.0]: https://github.com/smythi93/Tests4Py/releases/tag/v1.0.0

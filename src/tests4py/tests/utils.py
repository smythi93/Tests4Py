import abc
import enum
import os
import shlex
import subprocess
import tempfile
from abc import abstractmethod
from os import PathLike
from pathlib import Path
from typing import List, Tuple, Collection, Any, Optional, Sequence

from tests4py.constants import Environment, HARNESS_FILE, PYTHON
from tests4py.logger import LOGGER


class TestResult(enum.Enum):
    FAILING = "FAILING"
    PASSING = "PASSING"
    UNDEFINED = "UNDEFINED"


class SpecificationError(ValueError):
    pass


class API:
    def __init__(self, default_timeout=5):
        self.default_timeout = default_timeout

    @abstractmethod
    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        raise NotImplementedError()

    # noinspection PyMethodMayBeStatic
    def get_test_arguments_from_string(self, s: str) -> List[str]:
        parts = shlex.split(s)
        if parts and parts[-1] == "":
            parts.pop()
        return parts if parts else []

    def get_test_arguments(self, system_test_path: PathLike) -> List[str]:
        with open(system_test_path, "r") as fp:
            test = fp.read()
        return self.get_test_arguments_from_string(test)

    # noinspection PyBroadException
    def execute(
        self,
        args: Sequence[str],
        environ: Environment,
        work_dir: Optional[Path] = None,
        pipe: bool = True,
    ) -> Any:
        try:
            process = subprocess.run(
                [PYTHON, HARNESS_FILE] + list(args),
                stdout=subprocess.PIPE if pipe else None,
                stderr=subprocess.PIPE if pipe else None,
                timeout=self.default_timeout,
                env=environ,
                cwd=Path.cwd() if work_dir is None else work_dir,
            )
            return process
        except subprocess.TimeoutExpired:
            return None
        except Exception:
            return None

    def test(
        self,
        system_test_path: PathLike,
        environ: Environment,
        work_dir: Optional[Path] = None,
    ) -> Tuple[PathLike, TestResult, str]:
        try:
            try:
                return system_test_path, *self.oracle(
                    self.execute(
                        self.prepare_args(
                            self.get_test_arguments(system_test_path), work_dir
                        ),
                        environ,
                        work_dir=work_dir,
                    )
                )
            except SpecificationError as e:
                return (
                    system_test_path,
                    TestResult.UNDEFINED,
                    f"Test does not match specification: {e}",
                )
        finally:
            self.clean_up()

    def clean_up(self):
        pass

    def run(
        self,
        args_or_path: List[str] | PathLike,
        environ: Environment,
        invoke_oracle: bool = False,
        work_dir: Optional[Path] = None,
    ) -> Tuple[TestResult, str, str, str]:
        if isinstance(args_or_path, list):
            args = self.prepare_args(args_or_path, work_dir)
        else:
            system_tests_path = Path(args_or_path)
            if (
                len(args_or_path) > 256
                or not system_tests_path.exists()
                or system_tests_path.is_dir()
            ):
                raise ValueError(f"{system_tests_path} does not exist or is not a file")
            args = self.prepare_args(self.get_test_arguments(args_or_path), work_dir)
        process = self.execute(args, environ, work_dir=work_dir)
        if hasattr(process, "stdout"):
            stdout = process.stdout.decode("utf8")
        else:
            stdout = ""
        if hasattr(process, "stderr"):
            stderr = process.stderr.decode("utf8")
        else:
            stderr = ""
        if invoke_oracle:
            return *self.oracle(process), stdout, stderr
        else:
            return TestResult.UNDEFINED, "", stdout, stderr

    def tests(
        self,
        system_tests: PathLike | str | List[PathLike | str],
        environ: Environment,
        work_dir: Optional[Path] = None,
    ) -> List[Tuple[PathLike | str, TestResult, str]]:
        tests = list()
        if isinstance(system_tests, List):
            for test in system_tests:
                tests.append(self.test(test, environ, work_dir=work_dir))
        else:
            system_tests_path = Path(system_tests)
            if len(str(system_tests_path)) > 256 or not system_tests_path.exists():
                LOGGER.info(
                    f"Path {repr(system_tests)} does not exist, try to execute it as test case"
                )
                with tempfile.NamedTemporaryFile(mode="w") as tmp:
                    tmp.write(system_tests)
                    tmp.flush()
                    _, test_result, feedback = self.test(
                        tmp.name, environ, work_dir=work_dir
                    )
                    tests.append((system_tests, test_result, feedback))
            elif not system_tests_path.is_dir():
                LOGGER.info(f"Path {system_tests_path} is a file")
                tests.append(self.test(system_tests_path, environ, work_dir=work_dir))
            else:
                for dir_path, _, files in os.walk(system_tests_path):
                    for file in files:
                        path = Path(dir_path, file)
                        tests.append(self.test(path, environ, work_dir=work_dir))
        return tests

    def prepare_args(self, args: List[str], work_dir: Path) -> List[str]:
        return args


class CLIAPI(API, abc.ABC):
    def __init__(self, cli: List[str], default_timeout=5):
        super().__init__(default_timeout=default_timeout)
        self.cli = cli

    def execute(
        self,
        args: Sequence[str],
        environ: Environment,
        work_dir: Optional[Path] = None,
        pipe: bool = True,
    ) -> Any:
        try:
            process = subprocess.run(
                self.cli + list(args),
                stdout=subprocess.PIPE if pipe else None,
                stderr=subprocess.PIPE if pipe else None,
                timeout=self.default_timeout,
                env=environ,
                cwd=Path.cwd() if work_dir is None else work_dir,
            )
            return process
        except subprocess.TimeoutExpired:
            return None
        except Exception:
            return None


class ExpectOutputAPI(API):
    def __init__(
        self,
        expected: bytes | Collection[bytes],
        executable: PathLike = HARNESS_FILE,
        expect_in: bool = False,
        is_stdout: bool = False,
        no_check: bool = False,
        is_or: bool = True,
        default_timeout: int = 5,
    ):
        self.expected = expected
        self.executable = executable
        self.is_stdout = is_stdout
        self.expect_in = expect_in
        self.no_check = no_check
        self.is_or = is_or
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        process = args
        if process is None:
            return TestResult.UNDEFINED, "Cannot identify executed process"
        feedback = process.stdout if self.is_stdout else process.stderr
        if self.no_check or process.returncode:
            if (any if self.is_or else all)(
                map(
                    feedback.__contains__,
                    [self.expected]
                    if isinstance(self.expected, bytes)
                    else self.expected,
                )
            ):
                return (
                    TestResult.PASSING if self.expect_in else TestResult.FAILING,
                    feedback,
                )
            elif self.no_check:
                return (
                    TestResult.FAILING if self.expect_in else TestResult.PASSING,
                    feedback,
                )
            else:
                return TestResult.UNDEFINED, feedback
        else:
            return TestResult.PASSING, feedback


class ExpectErrAPI(ExpectOutputAPI):
    def __init__(
        self, expected: bytes | Collection[bytes], executable: PathLike = HARNESS_FILE
    ):
        super().__init__(expected, executable)


class ExpectOutAPI(ExpectOutputAPI):
    def __init__(
        self, expected: bytes | Collection[bytes], executable: PathLike = HARNESS_FILE
    ):
        super().__init__(expected, executable, is_stdout=True)


class ExpectNotErrAPI(ExpectOutputAPI):
    def __init__(
        self, expected: bytes | Collection[bytes], executable: PathLike = HARNESS_FILE
    ):
        super().__init__(expected, executable, expect_in=True)


class ExpectNotOutAPI(ExpectOutputAPI):
    def __init__(
        self, expected: bytes | Collection[bytes], executable: PathLike = HARNESS_FILE
    ):
        super().__init__(expected, executable, is_stdout=True, expect_in=True)

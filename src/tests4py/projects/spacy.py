import ast
import os.path
import random
import string
import subprocess
from _ast import Call, ImportFrom, Assign, Expr, Assert, Module
from pathlib import Path
from typing import List, Optional, Tuple, Any, Callable
from tests4py.constants import PYTHON
from tests4py.grammars import python
from tests4py.grammars.fuzzer import Grammar
from tests4py.grammars.fuzzer import is_valid_grammar
from tests4py.grammars.fuzzer import srange
from tests4py.projects import Project, Status, TestingFramework, TestStatus
from tests4py.tests.generator import UnittestGenerator, SystemtestGenerator
from tests4py.tests.utils import API, TestResult

PROJECT_NAME = "spacy"


class SpaCy(Project):
    def __init__(
            self,
            bug_id: int,
            buggy_commit_id: str,
            fixed_commit_id: str,
            test_files: List[Path],
            test_cases: List[str],
            test_status_fixed: TestStatus = TestStatus.PASSING,
            test_status_buggy: TestStatus = TestStatus.FAILING,
            unittests: Optional[UnittestGenerator] = None,
            systemtests: Optional[SystemtestGenerator] = None,
            api: Optional[API] = None,
            loc: int = 0,
            relevant_test_files: Optional[List[Path]] = None,
            skip_tests: Optional[List[str]] = None,
    ):
        super().__init__(
            bug_id=bug_id,
            project_name=PROJECT_NAME,
            github_url="https://github.com/explosion/spaCy",
            status=Status.OK,
            python_version="3.7.7",
            python_path="",
            buggy_commit_id=buggy_commit_id,
            fixed_commit_id=fixed_commit_id,
            testing_framework=TestingFramework.PYTEST,
            test_files=test_files,
            test_cases=test_cases,
            darwin_python_version="3.7.8",
            python_fallback_version="3.7.8",
            test_status_fixed=test_status_fixed,
            test_status_buggy=test_status_buggy,
            unittests=unittests,
            systemtests=systemtests,
            api=api,
            grammar=None,
            loc=loc,
            source_base=Path(PROJECT_NAME),
            test_base=Path(PROJECT_NAME, "tests"),
            included_files=[PROJECT_NAME],
            excluded_files=[os.path.join(PROJECT_NAME, "tests")],
            setup=[
                [PYTHON, "setup.py", "build_ext", "--inplace"],
            ],
            relevant_test_files=relevant_test_files,
            skip_tests=skip_tests,
        )

    def patch(self, location: Path):
        with open(location / "pyproject.toml", "r") as fp:
            content = fp.read()
        content = content.replace(
            "cython>=0.25",
            "cython==0.29.19",
        )
        with open(location / "pyproject.toml", "w") as fp:
            fp.write(content)
        if self.bug_id in (4, 5, 6, 7, 8, 9):
            with open(location / "setup.cfg", "r") as fp:
                content = fp.read()
            if self.bug_id == 9:
                content = content.replace(
                    "spacy_lookups_data>=0.0.4<0.2.0",
                    "spacy_lookups_data>=0.0.4,<0.2.0",
                )
            else:
                content = content.replace(
                    "spacy_lookups_data>=0.0.5<0.2.0",
                    "spacy_lookups_data>=0.0.5,<0.2.0",
                )
            with open(location / "setup.cfg", "w") as fp:
                fp.write(content)


def register():
    SpaCy(
        bug_id=1,
        buggy_commit_id="9ce059dd067ecc3f097d04023e3cfa0d70d35bb8",
        fixed_commit_id="a987e9e45d4084f30964a4cec9914ae6ed25a73c",
        test_files=[
            Path("spacy", "tests", "test_errors.py"),
            Path("spacy", "tests", "test_architectures.py"),
        ],
        test_cases=[os.path.join("spacy", "tests", "test_errors.py::test_add_codes")],
        api=SpaCyAPI1(),
        unittests=SpaCyUnittestGenerator1(),
        systemtests=SpaCySystemtestGenerator1(),
        loc=80165,
    )
    SpaCy(
        bug_id=2,
        buggy_commit_id="efec28ce70a0ff69471cc379867deebe7eb881e0",
        fixed_commit_id="cfdaf99b8029d6762730c5d5bd2b6f6c173c1241",
        test_files=[
            Path("spacy", "tests", "regression", "test_issue5137.py"),
            Path("spacy", "tests", "pipeline", "test_analysis.py"),
        ],
        test_cases=[
            os.path.join(
                "spacy", "tests", "regression", "test_issue5137.py::test_issue5137"
            )
        ],
        skip_tests=[
            "test_component_decorator_assigns",
            "test_component_factories_from_nlp",
        ],
        api=SpaCyAPI2(),
        unittests=SpaCyUnittestGenerator2(),
        systemtests=SpaCySystemtestGenerator2(),
        loc=80024,
    )
    SpaCy(
        bug_id=3,
        buggy_commit_id="dac70f29eb3b1f21ae9e2c6346666bf6a46307b6",
        fixed_commit_id="663333c3b2bad90915d1a48a626ca1275b7ef077",
        test_files=[Path("spacy", "tests", "regression", "test_issue5314.py")],
        test_cases=[
            os.path.join(
                "spacy",
                "tests",
                "regression",
                "test_issue5314.py::test_issue5314"
                '[<text bytes="11456" xml:space="preserve">[[Fil:Arch\\xe4ologie '
                "schichtengrabung.jpg|thumb|Ark\\xe6ologisk [[udgravning]] med profil."
                "]] '''Ark\\xe6ologi''' er studiet af tidligere tiders "
                "[[menneske]]lige [[aktivitet]], prim\\xe6rt gennem studiet af "
                "menneskets materielle levn.</text>0]",
            ),
            os.path.join(
                "spacy",
                "tests",
                "regression",
                "test_issue5314.py::test_issue5314"
                '[<text bytes="11456" xml:space="preserve">[[Fil:Arch\\xe4ologie schichtengrabung.jpg|thumb|Ark'
                "\\xe6ologisk [[udgravning]] med profil.]] '''Ark\\xe6ologi''' er studiet af tidligere tiders "
                "[[menneske]]lige [[aktivitet]], prim\\xe6rt gennem studiet af menneskets materielle levn.</text>1]",
            ),
        ],
        api=SpaCyAPI3(),
        unittests=SpaCyUnittestGenerator3(),
        systemtests=SpaCySystemtestGenerator3(),
        loc=79665,
    )
    SpaCy(
        bug_id=4,
        buggy_commit_id="abd5c06374eab5db0cf897b73543b1f3eb007e12",
        fixed_commit_id="9fa9d7f2cb52ce6a70c264d4e57c7f190d7686bf",
        test_files=[
            Path("spacy", "tests", "regression", "test_issue4665.py"),
            Path("spacy", "tests", "test_cli.py"),
        ],
        test_cases=[
            os.path.join(
                "spacy", "tests", "regression", "test_issue4665.py::test_issue4665"
            )
        ],
        api=SpaCyAPI4(),
        unittests=SpaCyUnittestGenerator4(),
        systemtests=SpaCySystemtestGenerator4(),
        loc=73718,
    )
    SpaCy(
        bug_id=5,
        buggy_commit_id="bdfb696677a7591ced018e7597c00929e97c6837",
        fixed_commit_id="3bd15055ce74b04dcaf3b9abe2adeb01fb595776",
        test_files=[Path("spacy", "tests", "test_language.py")],
        test_cases=[
            os.path.join("spacy", "tests", "test_language.py::test_evaluate_no_pipe")
        ],
        api=SpaCyAPI5(),
        unittests=SpaCyUnittestGenerator5(),
        systemtests=SpaCySystemtestGenerator5(),
        loc=73083,
    )
    SpaCy(
        bug_id=6,
        buggy_commit_id="6b874ef09611ac32ad038203423d44087cbeb3ae",
        fixed_commit_id="afe4a428f78abe45d6104d74ef42a066570fa43d",
        test_files=[Path("spacy", "tests", "pipeline", "test_analysis.py")],
        test_cases=[
            os.path.join(
                "spacy",
                "tests",
                "pipeline",
                "test_analysis.py::test_analysis_validate_attrs_remove_pipe",
            )
        ],
        api=SpaCyAPI6(),
        unittests=SpaCyUnittestGenerator6(),
        systemtests=SpaCySystemtestGenerator6(),
        test_status_fixed=TestStatus.FAILING,
        loc=72871,
    )
    SpaCy(
        bug_id=7,
        buggy_commit_id="da6e0de34f4947fdebc839df3969c641014cfa97",
        fixed_commit_id="6f54e59fe7ccb3bacce896ed33d36b39f11cbfaf",
        test_files=[Path("spacy", "tests", "doc", "test_span.py")],
        test_cases=[
            os.path.join("spacy", "tests", "doc", "test_span.py::test_filter_spans")
        ],
        api=SpaCyAPI7(),
        unittests=SpaCyUnittestGenerator7(),
        systemtests=SpaCySystemtestGenerator7(),
        loc=72264,
    )
    SpaCy(
        bug_id=8,
        buggy_commit_id="fa95c030a511337935d1a2e930cb954c7a4cd376",
        fixed_commit_id="5efae495f18f37316bd641a05ca26e62cb78e242",
        test_files=[Path("spacy", "tests", "matcher", "test_matcher_logic.py")],
        test_cases=[
            os.path.join(
                "spacy",
                "tests",
                "matcher",
                "test_matcher_logic.py::test_matcher_remove",
            )
        ],
        api=SpaCyAPI8(),
        unittests=SpaCyUnittestGenerator8(),
        systemtests=SpaCySystemtestGenerator8(),
        loc=72263,
    )
    SpaCy(
        bug_id=9,
        buggy_commit_id="bc7e7db208d351fae2982afbcdff7633f9636779",
        fixed_commit_id="3297a19545027c8d8550b1ae793ce290567eff32",
        test_files=[
            Path("spacy", "tests", "pipeline", "test_tagger.py"),
            Path("spacy", "tests", "regression", "test_issue2501-3000.py"),
        ],
        test_cases=[
            os.path.join(
                "spacy",
                "tests",
                "pipeline",
                "test_tagger.py::test_tagger_warns_no_lemma_lookups",
            )
        ],
        api=SpaCyAPI9(),
        unittests=SpaCyUnittestGenerator9(),
        systemtests=SpaCySystemtestGenerator9(),
        loc=72195,
    )
    SpaCy(
        bug_id=10,
        buggy_commit_id="38de08c7a99d5d8c490223126071afe7dd4f4b67",
        fixed_commit_id="52904b72700a3f301a26563d3f94493bad96a446",
        test_files=[Path("spacy", "tests", "matcher", "test_matcher_api.py")],
        test_cases=[
            os.path.join(
                "spacy",
                "tests",
                "matcher",
                "test_matcher_api.py::test_matcher_valid_callback",
            )
        ],
        api=SpaCyAPI10(),
        unittests=SpaCyUnittestGenerator10(),
        systemtests=SpaCySystemtestGenerator10(),
        loc=72240,
    )


class SpaCyAPI1(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[3]
        result = process.stdout.decode("utf8")
        result = result.strip()
        expected = expected[:-1]
        expected = expected.replace("\\n", "\n")
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class SpaCyAPI2(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        expected = expected[1:]
        expected = expected[:-1]
        result = process.stdout.decode("utf8")
        result = result.strip()
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class SpaCyAPI3(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[3]
        result = process.stdout.decode("utf8")
        result = result.strip()
        expected = expected[:-1]
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class SpaCyAPI4(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        result = process.stdout.decode("utf8")
        result = result.strip()
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class SpaCyAPI5(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        result = process.stdout.decode("utf8")
        result = result.strip()
        print("args: ", args)
        print("result: ", result)
        print("expected: ", expected)
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class SpaCyAPI6(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        expected = expected[1:]
        expected = expected[:-1]
        result = process.stdout.decode("utf8")
        result = result.strip()
        print("args: ", args)
        print("result: ", result)
        print("expected: ", expected)
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class SpaCyAPI7(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        expected = expected[1:]
        expected = expected[:-1]
        result = process.stdout.decode("utf8")
        result = result.strip()
        print("args: ", args)
        print("result: ", result)
        print("expected: ", expected)
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class SpaCyAPI8(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        expected = expected[1:]
        expected = expected[:-1]
        result = process.stdout.decode("utf8")
        result = result.strip()
        print("args: ", args)
        print("result: ", result)
        print("expected: ", expected)
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class SpaCyAPI9(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        expected = expected[1:]
        expected = expected[:-1]
        result = process.stdout.decode("utf8")
        result = result.strip()
        print("args: ", args)
        print("result: ", result)
        print("expected: ", expected)
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class SpaCyAPI10(API):
    def __init__(self, default_timeout: int = 5):
        super().__init__(default_timeout=default_timeout)

    def oracle(self, args: Any) -> Tuple[TestResult, str]:
        if args is None:
            return TestResult.UNDEFINED, "No process finished"
        process: subprocess.CompletedProcess = args
        expected = process.args[2]
        expected = expected[1:]
        expected = expected[:-1]
        result = process.stdout.decode("utf8")
        result = result.strip()
        print("args: ", args)
        print("result: ", result)
        print("expected: ", expected)
        if result == expected:
            return TestResult.PASSING, ""
        else:
            return TestResult.FAILING, f"Expected {expected}, but was {result}"


class SpaCyTestGenerator:
    @staticmethod
    def generate_values(producer: Callable) -> str:
        return producer()

    @staticmethod
    def generate_random_string():
        return "".join(random.choices(string.ascii_letters, k=random.randint(5, 15)))

    @staticmethod
    def spacy1_generate():
        all_errors = (
            "E001", "E002", "E003", "E004", "E005", "E006", "E007", "E008", "E009", "E010",
            "E011", "E012", "E013", "E014", "E015", "E016", "E017", "E018", "E019", "E020",
            "E021", "E022", "E023", "E024", "E025", "E026", "E027", "E028", "E029", "E030",
            "E031", "E032", "E033", "E034", "E035", "E036", "E037", "E038", "E039", "E040",
            "E041", "E042", "E043", "E044", "E045", "E046", "E047", "E048", "E049", "E050",
            "E051", "E052", "E053", "E054", "E055", "E056", "E057", "E058", "E059", "E060",
            "E061", "E062", "E063", "E064", "E065", "E066", "E067", "E068", "E069", "E070",
            "E071", "E072", "E073", "E074", "E075", "E076", "E077", "E078", "E079", "E080",
            "E081", "E082", "E083", "E084", "E085", "E086", "E087", "E088", "E089", "E090",
            "E091", "E092", "E093", "E094", "E095", "E096", "E097", "E098", "E099", "E100",
            "E101", "E102", "E103", "E104", "E105", "E106", "E107", "E108", "E109", "E110",
            "E111", "E112", "E113", "E114", "E115", "E116", "E117", "E118", "E119", "E120",
            "E121", "E122", "E123", "E124", "E125", "E126", "E127", "E128", "E129", "E130",
            "E131", "E132", "E133", "E134", "E135", "E136", "E137", "E138", "E139", "E140",
            "E141", "E142", "E143", "E144", "E145", "E146", "E147", "E148", "E149", "E150",
            "E151", "E152", "E153", "E154", "E155", "E156", "E157", "E158", "E159", "E160",
            "E161", "E162", "E163", "E164", "E165", "E166", "E167", "E168", "E169", "E170",
            "E171", "E172", "E173", "E174", "E175", "E176", "E177", "E178", "E179", "E180",
            "E181", "E182", "E183", "E184", "E185", "E186", "E187", "E188", "E189", "E190",
            "E191", "E192", "E193", "E194", "E195", "E196", "E197"
        )
        all_error_messages = (
            "No component '{name}' found in pipeline. Available names: {opts}",
            "Can't find factory for '{name}'. This usually happens when spaCy "
            "calls `nlp.create_pipe` with a component name that's not built "
            "in - for example, when constructing the pipeline from a model's "
            "meta.json. If you're using a custom component, you can write to "
            "`Language.factories['{name}']` or remove it from the model meta "
            "and add it via `nlp.add_pipe` instead.",
            "Not a valid pipeline component. Expected callable, but "
            "got {component} (name: '{name}').",
            "If you meant to add a built-in component, use `create_pipe`: "
            "`nlp.add_pipe(nlp.create_pipe('{component}'))`",
            "Pipeline component '{name}' returned None. If you're using a "
            "custom component, maybe you forgot to return the processed Doc?",
            "Invalid constraints. You can only set one of the following: "
            "before, after, first, last.",
            "'{name}' already exists in pipeline. Existing names: {opts}",
            "Some current components would be lost when restoring previous "
            "pipeline state. If you added components after calling "
            "`nlp.disable_pipes()`, you should remove them explicitly with "
            "`nlp.remove_pipe()` before the pipeline is restored. Names of "
            "the new components: {names}",
            "The `update` method expects same number of docs and golds, but "
            "got: {n_docs} docs, {n_golds} golds.",
            "Word vectors set to length 0. This may be because you don't have "
            "a model installed or loaded, or because your model doesn't "
            "include word vectors. For more info, see the docs:\n"
            "https://spacy.io/usage/models",
            "Unknown operator: '{op}'. Options: {opts}",
            "Cannot add pattern for zero tokens to matcher.\nKey: {key}",
            "Error selecting action in matcher",
            "Unknown tag ID: {tag}",
            "Conflicting morphology exception for ({tag}, {orth}). Use "
            "`force=True` to overwrite.",
            "MultitaskObjective target should be function or one of: dep, "
            "tag, ent, dep_tag_offset, ent_tag.",
            "Can only add unicode or bytes. Got type: {value_type}",
            "Can't retrieve string for hash '{hash_value}'. This usually "
            "refers to an issue with the `Vocab` or `StringStore`.",
            "Can't create transition with unknown action ID: {action}. Action "
            "IDs are enumerated in spacy/syntax/{src}.pyx.",
            "Could not find a gold-standard action to supervise the "
            "dependency parser. The tree is non-projective (i.e. it has "
            "crossing arcs - see spacy/syntax/nonproj.pyx for definitions). "
            "The ArcEager transition system only supports projective trees. "
            "To learn non-projective representations, transform the data "
            "before training and after parsing. Either pass "
            "`make_projective=True` to the GoldParse class, or use "
            "spacy.syntax.nonproj.preprocess_training_data.",
            "Could not find a gold-standard action to supervise the "
            "dependency parser. The GoldParse was projective. The transition "
            "system has {n_actions} actions. State at failure: {state}",
            "Could not find a transition with the name '{name}' in the NER "
            "model.",
            "Error cleaning up beam: The same state occurred twice at "
            "memory address {addr} and position {i}.",
            "Could not find an optimal move to supervise the parser. Usually, "
            "this means that the model can't be updated in a way that's valid "
            "and satisfies the correct annotations specified in the GoldParse. "
            "For example, are all labels added to the model? If you're "
            "training a named entity recognizer, also make sure that none of "
            "your annotated entity spans have leading or trailing whitespace "
            "or punctuation. "
            "You can also use the experimental `debug-data` command to "
            "validate your JSON-formatted training data. For details, run:\n"
            "python -m spacy debug-data --help",
            "String is too long: {length} characters. Max is 2**30.",
            "Error accessing token at position {i}: out of bounds in Doc of "
            "length {length}.",
            "Arguments 'words' and 'spaces' should be sequences of the same "
            "length, or 'spaces' should be left default at None. spaces "
            "should be a sequence of booleans, with True meaning that the "
            "word owns a ' ' character following it.",
            "orths_and_spaces expects either a list of unicode string or a "
            "list of (unicode, bool) tuples. Got bytes instance: {value}",
            "noun_chunks requires the dependency parse, which requires a "
            "statistical model to be installed and loaded. For more info, see "
            "the documentation:\nhttps://spacy.io/usage/models",
            "Sentence boundaries unset. You can add the 'sentencizer' "
            "component to the pipeline with: "
            "nlp.add_pipe(nlp.create_pipe('sentencizer')) "
            "Alternatively, add the dependency parser, or set sentence "
            "boundaries by setting doc[i].is_sent_start.",
            "Invalid token: empty string ('') at position {i}.",
            "Conflicting attributes specified in doc.from_array(): "
            "(HEAD, SENT_START). The HEAD attribute currently sets sentence "
            "boundaries implicitly, based on the tree structure. This means "
            "the HEAD attribute would potentially override the sentence "
            "boundaries set by SENT_START.",
            "Cannot load into non-empty Doc of length {length}.",
            "Doc.merge received {n_args} non-keyword arguments. Expected "
            "either 3 arguments (deprecated), or 0 (use keyword arguments).\n"
            "Arguments supplied:\n{args}\nKeyword arguments:{kwargs}",
            "Error creating span with start {start} and end {end} for Doc of "
            "length {length}.",
            "Error calculating span: Can't find a token starting at character "
            "offset {start}.",
            "Error calculating span: Can't find a token ending at character "
            "offset {end}.",
            "Error finding sentence for span. Infinite loop detected.",
            "Array bounds exceeded while searching for root word. This likely "
            "means the parse tree is in an invalid state. Please report this "
            "issue here: http://github.com/explosion/spaCy/issues",
            "Attempt to access token at {i}, max length {max_length}.",
            "Invalid comparison operator: {op}. Likely a Cython bug?",
            "Error accessing doc[{i}].nbor({j}), for doc of length {length}.",
            "Refusing to write to token.sent_start if its document is parsed, "
            "because this may cause inconsistent state.",
            "Invalid value for token.sent_start: {value}. Must be one of: "
            "None, True, False",
            "Possibly infinite loop encountered while looking for {attr}.",
            "Can't retrieve unregistered extension attribute '{name}'. Did "
            "you forget to call the `set_extension` method?",
            "Can't assign a value to unregistered extension attribute "
            "'{name}'. Did you forget to call the `set_extension` method?",
            "Can't import language {lang} from spacy.lang: {err}",
            "Can't find spaCy data directory: '{path}'. Check your "
            "installation and permissions, or use spacy.util.set_data_path "
            "to customise the location if necessary.",
            "Can't find model '{name}'. It doesn't seem to be a shortcut "
            "link, a Python package or a valid path to a data directory.",
            "Cant' load '{name}'. If you're using a shortcut link, make sure "
            "it points to a valid package (not just a data directory).",
            "Can't find model directory: {path}",
            "Could not read meta.json from {path}",
            "No valid '{setting}' setting found in model meta.json.",
            "Invalid ORTH value in exception:\nKey: {key}\nOrths: {orths}",
            "Invalid tokenizer exception: ORTH values combined don't match "
            "original string.\nKey: {key}\nOrths: {orths}",
            "Stepped slices not supported in Span objects. Try: "
            "list(tokens)[start:stop:step] instead.",
            "Could not retrieve vector for key {key}.",
            "One (and only one) keyword arg must be set. Got: {kwargs}",
            "Cannot add new key to vectors: the table is full. Current shape: "
            "({rows}, {cols}).",
            "Bad file name: {filename}. Example of a valid file name: "
            "'vectors.128.f.bin'",
            "Cannot find empty bit for new lexical flag. All bits between 0 "
            "and 63 are occupied. You can replace one by specifying the "
            "`flag_id` explicitly, e.g. "
            "`nlp.vocab.add_flag(your_func, flag_id=IS_ALPHA`.",
            "Invalid value for flag_id: {value}. Flag IDs must be between 1 "
            "and 63 (inclusive).",
            "Error fetching a Lexeme from the Vocab. When looking up a "
            "string, the lexeme returned had an orth ID that did not match "
            "the query string. This means that the cached lexeme structs are "
            "mismatched to the string encoding table. The mismatched:\n"
            "Query string: {string}\nOrth cached: {orth}\nOrth ID: {orth_id}",
            "Only one of the vector table's width and shape can be specified. "
            "Got width {width} and shape {shape}.",
            "Error creating model helper for extracting columns. Can only "
            "extract columns by positive integer. Got: {value}.",
            "Invalid BILUO tag sequence: Got a tag starting with 'I' (inside "
            "an entity) without a preceding 'B' (beginning of an entity). "
            "Tag sequence:\n{tags}",
            "Invalid BILUO tag: '{tag}'.",
            "Invalid gold-standard parse tree. Found cycle between word "
            "IDs: {cycle} (tokens: {cycle_tokens}) in the document starting "
            "with tokens: {doc_tokens}.",
            "Invalid gold-standard data. Number of documents ({n_docs}) "
            "does not align with number of annotations ({n_annots}).",
            "Error creating lexeme: specified orth ID ({orth}) does not "
            "match the one in the vocab ({vocab_orth}).",
            "Error serializing lexeme: expected data length {length}, "
            "got {bad_length}.",
            "Cannot assign vector of length {new_length}. Existing vectors "
            "are of length {length}. You can use `vocab.reset_vectors` to "
            "clear the existing vectors and resize the table.",
            "Error interpreting compiled match pattern: patterns are expected "
            "to end with the attribute {attr}. Got: {bad_attr}.",
            "Error accepting match: length ({length}) > maximum length "
            "({max_len}).",
            "Error setting tensor on Doc: tensor has {rows} rows, while Doc "
            "has {words} words.",
            "Error computing {value}: number of Docs ({n_docs}) does not "
            "equal number of GoldParse objects ({n_golds}) in batch.",
            "Error computing score: number of words in Doc ({words_doc}) does "
            "not equal number of words in GoldParse ({words_gold}).",
            "Error computing states in beam: number of predicted beams "
            "({pbeams}) does not equal number of gold beams ({gbeams}).",
            "Duplicate state found in beam: {key}.",
            "Error getting gradient in beam: number of histories ({n_hist}) "
            "does not equal number of losses ({losses}).",
            "Error deprojectivizing parse: number of heads ({n_heads}), "
            "projective heads ({n_proj_heads}) and labels ({n_labels}) do not "
            "match.",
            "Error setting extension: only one of `default`, `method`, or "
            "`getter` (plus optional `setter`) is allowed. Got: {nr_defined}",
            "Error assigning label ID {label} to span: not in StringStore.",
            "Can't create lexeme for string '{string}'.",
            "Error deserializing lexeme '{string}': orth ID {orth_id} does "
            "not match hash {hash_id} in StringStore.",
            "Unknown displaCy style: {style}.",
            "Text of length {length} exceeds maximum of {max_length}. The "
            "v2.x parser and NER models require roughly 1GB of temporary "
            "memory per 100,000 characters in the input. This means long "
            "texts may cause memory allocation errors. If you're not using "
            "the parser or NER, it's probably safe to increase the "
            "`nlp.max_length` limit. The limit is in number of characters, so "
            "you can check whether your inputs are too long by checking "
            "`len(text)`.",
            "Extensions can't have a setter argument without a getter "
            "argument. Check the keyword arguments on `set_extension`.",
            "Extension '{name}' already exists on {obj}. To overwrite the "
            "existing extension, set `force=True` on `{obj}.set_extension`.",
            "Invalid extension attribute {name}: expected callable or None, "
            "but got: {value}",
            "Could not find or assign name for word vectors. Ususally, the "
            "name is read from the model's meta.json in vector.name. "
            "Alternatively, it is built from the 'lang' and 'name' keys in "
            "the meta.json. Vector names are required to avoid issue #1660.",
            "token.ent_iob values make invalid sequence: I without B\n{seq}",
            "Error reading line {line_num} in vectors file {loc}.",
            "Can't write to frozen dictionary. This is likely an internal "
            "error. Are you writing to a default function argument?",
            "Invalid object passed to displaCy: Can only visualize Doc or "
            "Span objects, or dicts if set to manual=True.",
            "Invalid pattern: expected token pattern (list of dicts) or "
            "phrase pattern (string) but got:\n{pattern}",
            "Invalid pattern specified: expected both SPEC and PATTERN.",
            "First node of pattern should be a root node. The root should "
            "only contain NODE_NAME.",
            "Nodes apart from the root should contain NODE_NAME, NBOR_NAME and "
            "NBOR_RELOP.",
            "NODE_NAME should be a new node and NBOR_NAME should already have "
            "have been declared in previous edges.",
            "Can't merge non-disjoint spans. '{token}' is already part of "
            "tokens to merge. If you want to find the longest non-overlapping "
            "spans, you can use the util.filter_spans helper:\n"
            "https://spacy.io/api/top-level#util.filter_spans",
            "Trying to set conflicting doc.ents: '{span1}' and '{span2}'. A "
            "token can only be part of one entity, so make sure the entities "
            "you're setting don't overlap.",
            "Can't find JSON schema for '{name}'.",
            "The Doc.print_tree() method is now deprecated. Please use "
            "Doc.to_json() instead or write your own function.",
            "Can't find doc._.{attr} attribute specified in the underscore "
            "settings: {opts}",
            "Value of doc._.{attr} is not JSON-serializable: {value}",
            "As of spaCy v2.1, the pipe name `sbd` has been deprecated "
            "in favor of the pipe name `sentencizer`, which does the same "
            "thing. For example, use `nlp.create_pipeline('sentencizer')`",
            "Model for component '{name}' not initialized. Did you forget to "
            "load a model, or forget to call begin_training()?",
            "Invalid displaCy render wrapper. Expected callable, got: {obj}",
            "Pickling a token is not supported, because tokens are only views "
            "of the parent Doc and can't exist on their own. A pickled token "
            "would always have to include its Doc and Vocab, which has "
            "practically no advantage over pickling the parent Doc directly. "
            "So instead of pickling the token, pickle the Doc it belongs to.",
            "Pickling a span is not supported, because spans are only views "
            "of the parent Doc and can't exist on their own. A pickled span "
            "would always have to include its Doc and Vocab, which has "
            "practically no advantage over pickling the parent Doc directly. "
            "So instead of pickling the span, pickle the Doc it belongs to or "
            "use Span.as_doc to convert the span to a standalone Doc object.",
            "The newly split token can only have one root (head = 0).",
            "The newly split token needs to have a root (head = 0).",
            "All subtokens must have associated heads.",
            "Cannot currently add labels to pretrained text classifier. Add "
            "labels before training begins. This functionality was available "
            "in previous versions, but had significant bugs that led to poor "
            "performance.",
            "The newly split tokens must match the text of the original token. "
            "New orths: {new}. Old text: {old}.",
            "The custom extension attribute '{attr}' is not registered on the "
            "Token object so it can't be set during retokenization. To "
            "register an attribute, use the Token.set_extension classmethod.",
            "Can't set custom extension attribute '{attr}' during "
            "retokenization because it's not writable. This usually means it "
            "was registered with a getter function (and no setter) or as a "
            "method extension, so the value is computed dynamically. To "
            "overwrite a custom attribute manually, it should be registered "
            "with a default value or with a getter AND setter.",
            "Can't set custom extension attributes during retokenization. "
            "Expected dict mapping attribute names to values, but got: {value}",
            "Can't bulk merge spans. Attribute length {attr_len} should be "
            "equal to span length ({span_len}).",
            "Cannot find token to be split. Did it get merged?",
            "Cannot find head of token to be split. Did it get merged?",
            "Cannot read from file: {path}. Supported formats: {formats}",
            "Unexpected value: {value}",
            "Unexpected matcher predicate: '{bad}'. Expected one of: {good}. "
            "This is likely a bug in spaCy, so feel free to open an issue.",
            "Cannot create phrase pattern representation for length 0. This "
            "is likely a bug in spaCy.",
            "Unsupported serialization argument: '{arg}'. The use of keyword "
            "arguments to exclude fields from being serialized or deserialized "
            "is now deprecated. Please use the `exclude` argument instead. "
            "For example: exclude=['{arg}'].",
            "Cannot write the label of an existing Span object because a Span "
            "is a read-only view of the underlying Token objects stored in the "
            "Doc. Instead, create a new Span object and specify the `label` "
            "keyword argument, for example:\nfrom spacy.tokens import Span\n"
            "span = Span(doc, start={start}, end={end}, label='{label}')",
            "You are running a narrow unicode build, which is incompatible "
            "with spacy >= 2.1.0. To fix this, reinstall Python and use a wide "
            "unicode build instead. You can also rebuild Python and set the "
            "--enable-unicode=ucs4 flag.",
            "Cannot write the kb_id of an existing Span object because a Span "
            "is a read-only view of the underlying Token objects stored in "
            "the Doc. Instead, create a new Span object and specify the "
            "`kb_id` keyword argument, for example:\nfrom spacy.tokens "
            "import Span\nspan = Span(doc, start={start}, end={end}, "
            "label='{label}', kb_id='{kb_id}')",
            "The vectors for entities and probabilities for alias '{alias}' "
            "should have equal length, but found {entities_length} and "
            "{probabilities_length} respectively.",
            "The sum of prior probabilities for alias '{alias}' should not "
            "exceed 1, but found {sum}.",
            "Entity '{entity}' is not defined in the Knowledge Base.",
            "If you meant to replace a built-in component, use `create_pipe`: "
            "`nlp.replace_pipe('{name}', nlp.create_pipe('{name}'))`",
            "This additional feature requires the jsonschema library to be "
            "installed:\npip install jsonschema",
            "Expected 'dict' type, but got '{type}' from '{line}'. Make sure "
            "to provide a valid JSON object as input with either the `text` "
            "or `tokens` key. For more info, see the docs:\n"
            "https://spacy.io/api/cli#pretrain-jsonl",
            "Invalid JSONL format for raw text '{text}'. Make sure the input "
            "includes either the `text` or `tokens` key. For more info, see "
            "the docs:\nhttps://spacy.io/api/cli#pretrain-jsonl",
            "Knowledge Base for component '{name}' not initialized. Did you "
            "forget to call set_kb()?",
            "The list of entities, prior probabilities and entity vectors "
            "should be of equal length.",
            "Entity vectors should be of length {required} instead of the "
            "provided {found}.",
            "Unsupported loss_function '{loss_func}'. Use either 'L2' or "
            "'cosine'.",
            "Labels for component '{name}' not initialized. Did you forget to "
            "call add_label()?",
            "Could not find parameter `{param}` when building the entity "
            "linker model.",
            "Error reading `{param}` from input file.",
            "Could not access `{path}`.",
            "Unexpected error in the {method} functionality of the "
            "EntityLinker: {msg}. This is likely a bug in spaCy, so feel free "
            "to open an issue.",
            "Expected {ents} KB identifiers but got {ids}. Make sure that "
            "each entity in `doc.ents` is assigned to a KB identifier.",
            "Error deserializing model. Check that the config used to create "
            "the component matches the model being loaded.",
            "The language of the `nlp` object and the `vocab` should be the "
            "same, but found '{nlp}' and '{vocab}' respectively.",
            "Trying to call nlp.update without required annotation types. "
            "Expected top-level keys: {exp}. Got: {unexp}.",
            "The attribute {attr} is not supported for token patterns. "
            "Please use the option validate=True with Matcher, PhraseMatcher, "
            "or EntityRuler for more details.",
            "The value type {vtype} is not supported for token patterns. "
            "Please use the option validate=True with Matcher, PhraseMatcher, "
            "or EntityRuler for more details.",
            "One of the attributes or values is not supported for token "
            "patterns. Please use the option validate=True with Matcher, "
            "PhraseMatcher, or EntityRuler for more details.",
            "The pipeline needs to include a tagger in order to use "
            "Matcher or PhraseMatcher with the attributes POS, TAG, or LEMMA. "
            "Try using nlp() instead of nlp.make_doc() or list(nlp.pipe()) "
            "instead of list(nlp.tokenizer.pipe()).",
            "The pipeline needs to include a parser in order to use "
            "Matcher or PhraseMatcher with the attribute DEP. Try using "
            "nlp() instead of nlp.make_doc() or list(nlp.pipe()) instead of "
            "list(nlp.tokenizer.pipe()).",
            "Can't render negative values for dependency arc start or end. "
            "Make sure that you're passing in absolute token indices, not "
            "relative token offsets.\nstart: {start}, end: {end}, label: "
            "{label}, direction: {dir}",
            "Can't add table '{name}' to lookups because it already exists.",
            "Can't find table '{name}' in lookups. Available tables: {tables}",
            "Can't find language data file: {path}",
            "Found an internal inconsistency when predicting entity links. "
            "This is likely a bug in spaCy, so feel free to open an issue.",
            "Cannot evaluate textcat model on data with different labels.\n"
            "Labels in model: {model_labels}\nLabels in evaluation "
            "data: {eval_labels}",
            "cumsum was found to be unstable: its last element does not "
            "correspond to sum",
            "x is neither increasing nor decreasing: {}.",
            "Only one class present in y_true. ROC AUC score is not defined in "
            "that case.",
            "Can only merge DocBins with the same pre-defined attributes.\n"
            "Current DocBin: {current}\nOther DocBin: {other}",
            "Unknown morphological feature: '{feat}' ({feat_id}). This can "
            "happen if the tagger was trained with a different set of "
            "morphological features. If you're using a pretrained model, make "
            "sure that your models are up to date:\npython -m spacy validate",
            "Unknown field: {field}",
            "Can't find module: {module}",
            "Cannot apply transition {name}: invalid for the current state.",
            "Matcher.add received invalid on_match callback argument: expected "
            "callable or None, but got: {arg_type}",
            "The Lemmatizer.load classmethod is deprecated. To create a "
            "Lemmatizer, initialize the class directly. See the docs for "
            "details: https://spacy.io/api/lemmatizer",
            "As of v2.2, the Lemmatizer is initialized with an instance of "
            "Lookups containing the lemmatization tables. See the docs for "
            "details: https://spacy.io/api/lemmatizer#init",
            "Architecture '{name}' not found in registry. Available "
            "names: {names}",
            "Can't remove rule for unknown match pattern ID: {key}",
            "Alias '{alias}' is not defined in the Knowledge Base.",
            "Ill-formed IOB input detected: {tag}",
            "Invalid pattern. Expected list of dicts but got: {pat}. Maybe you "
            "accidentally passed a single pattern to Matcher.add instead of a "
            "list of patterns? If you only want to add one pattern, make sure "
            "to wrap it in a list. For example: matcher.add('{key}', [pattern])",
            "Invalid pattern. Expected a list of Doc objects but got a single "
            "Doc. If you only want to add one pattern, make sure to wrap it "
            "in a list. For example: matcher.add('{key}', [doc])",
            "Span attributes can't be declared as required or assigned by "
            "components, since spans are only views of the Doc. Use Doc and "
            "Token attributes (or custom extension attributes) only and remove "
            "the following: {attrs}",
            "Received invalid attributes for unkown object {obj}: {attrs}. "
            "Only Doc and Token attributes are supported.",
            "Received invalid attribute declaration: {attr}\nDid you forget "
            "to define the attribute? For example: {attr}.???",
            "Received invalid attribute declaration: {attr}\nOnly top-level "
            "attributes are supported, for example: {solution}",
            "Only attributes without underscores are supported in component "
            "attribute declarations (because underscore and non-underscore "
            "attributes are connected anyways): {attr} -> {solution}",
            "Received invalid attribute in component attribute declaration: "
            "{obj}.{attr}\nAttribute '{attr}' does not exist on {obj}.",
            "'{tok_a}' and '{tok_b}' are different texts.",
            "Only unicode strings are supported as labels.",
            "Could not match the gold entity links to entities in the doc - "
            "make sure the gold EL data refers to valid results of the "
            "named entity recognizer in the `nlp` pipeline.",
            "Each argument to `get_doc` should be of equal length.",
            "Token head out of range in `Doc.from_array()` for token index "
            "'{index}' with value '{value}' (equivalent to relative head "
            "index: '{rel_head_index}'). The head indices should be relative "
            "to the current token index rather than absolute indices in the "
            "array.",
            "Invalid head: the head token must be from the same doc as the "
            "token itself.",
            "Unable to resize vectors in place with cupy.",
            "Unable to resize vectors in place if the resized vector dimension "
            "({new_dim}) is not the same as the current vector dimension "
            "({curr_dim}).",
            "Unable to aligned mismatched text '{text}' and words '{words}'.",
            "Matcher can be called on {good} only, got {got}.",
            "Refusing to write to token.is_sent_end. Sentence boundaries can "
            "only be fixed with token.is_sent_start.",
            "Row out of bounds, unable to add row {row} for key {key}."
        )
        dice = random.randint(0, len(all_error_messages) - 1)
        passing = (all_errors[dice], f"[{all_errors[dice]}] {all_error_messages[dice]}")
        failing = (all_errors[dice], f"[{all_errors[dice]}] error description")
        return passing, failing

    @staticmethod
    def spacy2_generate():
        random_string = SpaCyTestGenerator.generate_random_string()
        random_string_f = SpaCyTestGenerator.generate_random_string()
        passing = random_string, random_string
        failing = random_string, random_string_f
        return passing, failing

    @staticmethod
    def spacy3_generate():
        random_string = SpaCyTestGenerator.generate_random_string()
        new_format_text = """<text xml:space="preserve">[[Fil:Archäologie schichtengrabung.jpg|thumb|Arkæologisk [[udgravning]] med profil.]] '''Arkæologi''' er studiet af tidligere tiders [[menneske]]lige [[aktivitet]], primært gennem studiet af menneskets materielle levn.</text>"""
        old_format_text = """<text bytes="11456" xml:space="preserve">[[Fil:Archäologie schichtengrabung.jpg|thumb|Arkæologisk [[udgravning]] med profil.]] '''Arkæologi''' er studiet af tidligere tiders [[menneske]]lige [[aktivitet]], primært gennem studiet af menneskets materielle levn.</text>"""
        potential_future_format = """<text bytes="11456" xml:space="preserve">[[Fil:Archäologie schichtengrabung.jpg|thumb|Arkæologisk [[udgravning]] med profil.]] '''Arkæologi''' er studiet af tidligere tiders [[menneske]]lige [[aktivitet]], primært gennem studiet af menneskets materielle levn.</text>"""
        old_future_format = random.choice([old_format_text, potential_future_format])
        passing = (random_string, new_format_text, "new")
        failing = (random_string, old_future_format, "old/future")
        return passing, failing

    @staticmethod
    def spacy4_generate():
        noun_1 = SpaCyTestGenerator.generate_random_string()
        noun_2 = SpaCyTestGenerator.generate_random_string()

        failing = f"""
        1	[	PUNCT	-	-LRB-	_	_	punct	_	_
        2	This	_	DET	DT	_	_	det	_	_
        3	{noun_1}	_	NOUN	NN	_	_	nsubj	_	_
        4	of	_	ADP	IN	_	_	case	_	_
        5	a	_	DET	DT	_	_	det	_	_
        6	respected	_	ADJ	JJ	_	_	amod	_	_
        7	cleric	_	NOUN	NN	_	_	nmod	_	_
        8	will	_	AUX	MD	_	_	aux	_	_
        9	be	_	AUX	VB	_	_	aux	_	_
        10	causing	_	VERB	VBG	_	_	root	_	_
        11	us	_	PRON	PRP	_	_	iobj	_	_
        12	{noun_2}	_	NOUN	NN	_	_	dobj	_	_
        13	for	_	ADP	IN	_	_	case	_	_
        14	years	_	NOUN	NNS	_	_	nmod	_	_
        15	to	_	PART	TO	_	_	mark	_	_
        16	come	_	VERB	VB	_	_	acl	_	_
        17	.	_	PUNCT	.	_	_	punct	_	_
        18	]	_	PUNCT	-RRB-	_	_	punct	_	_
        """
        passing = f"""
1	[	_	PUNCT	-LRB-	_	10	punct	_	_
2	This	_	DET	DT	_	3	det	_	_
3	{noun_2}	_	NOUN	NN	_	10	nsubj	_	_
4	of	_	ADP	IN	_	7	case	_	_
5	a	_	DET	DT	_	7	det	_	_
6	respected	_	ADJ	JJ	_	7	amod	_	_
7	cleric	_	NOUN	NN	_	10	nmod	_	_
8	will	_	AUX	MD	_	10	aux	_	_
9	be	_	AUX	VB	_	10	aux	_	_
10	causing	_	VERB	VBG	_	0	root	_	_
11	us	_	PRON	PRP	_	10	iobj	_	_
12	{noun_1}	_	NOUN	NN	_	10	dobj	_	_
13	for	_	ADP	IN	_	14	case	_	_
14	years	_	NOUN	NNS	_	10	nmod	_	_
15	to	_	PART	TO	_	16	mark	_	_
16	come	_	VERB	VB	_	10	acl	_	_
17	.	_	PUNCT	.	_	10	punct	_	_
        """

        return passing, failing

    @staticmethod
    def spacy5_generate():
        random_string = SpaCyTestGenerator.generate_random_string()
        passing = random_string
        failing = random_string
        return passing, failing

    @staticmethod
    def spacy6_generate():
        return "", ""

    @staticmethod
    def spacy7_generate():
        return "", ""

    @staticmethod
    def spacy8_generate():
        return "", ""

    @staticmethod
    def spacy9_generate():
        return "", ""

    @staticmethod
    def spacy10_generate():
        return "", ""


class SpaCyUnittestGenerator1(
    python.PythonGenerator, UnittestGenerator, SpaCyTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.spacy1_generate)

    @staticmethod
    def _get_assert(
            err: str,
            code: str
    ) -> list[Call]:
        return [
            ast.Call(
                func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                args=[
                    ast.Attribute(
                        value=ast.Name(id='Errors'),
                        attr=err,
                    ),
                    ast.Constant(value=code)
                ],
                keywords=[],
            )
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="spacy.errors",
                names=[ast.alias(name="Errors")],
                level=0,
            ),
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, fail_ = self._generate_one()
        err, code = fail_
        test = self.get_empty_test()
        test.body = self._get_assert(err, code)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, _ = self._generate_one()
        err, code = pass_
        test = self.get_empty_test()
        test.body = self._get_assert(err, code)
        return test, TestResult.PASSING


class SpaCyUnittestGenerator2(
    python.PythonGenerator, UnittestGenerator, SpaCyTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.spacy2_generate)

    @staticmethod
    def _get_assert(value1: str, value2: str
                    ) -> list[Module]:
        return [
            ast.Module(
                body=[
                    ast.ClassDef(
                        name='MyComponent',
                        bases=[],
                        keywords=[],
                        body=[
                            ast.Assign(
                                targets=[ast.Name(id='name')],
                                value=ast.Constant(value=value1),
                                lineno=1
                            ),
                            ast.FunctionDef(
                                name='__init__',
                                args=ast.arguments(
                                    args=[
                                        ast.arg(arg='self', annotation=None),
                                        ast.arg(arg='nlp', annotation=None),
                                        ast.arg(arg='**cfg', annotation=None)
                                    ],
                                    vararg=None,
                                    kwonlyargs=[],
                                    posonlyargs=[],
                                    kw_defaults=[],
                                    kwarg=None,
                                    defaults=[]
                                ),
                                body=[
                                    ast.Assign(
                                        targets=[ast.Attribute(value=ast.Name(id='self'), attr='nlp')],
                                        value=ast.Name(id='nlp'),
                                        lineno=2
                                    ),
                                    ast.Assign(
                                        targets=[
                                            ast.Attribute(value=ast.Name(id='self'), attr='categories')],
                                        value=ast.Call(
                                            func=ast.Attribute(value=ast.Name(id='cfg'), attr='get'),
                                            args=[
                                                ast.Constant(value='categories'),
                                                ast.Constant(value='all_categories')
                                            ],
                                            keywords=[]
                                        ),
                                        lineno=3
                                    )
                                ],
                                decorator_list=[],
                                lineno=4
                            ),
                            ast.FunctionDef(
                                name='__call__',
                                args=ast.arguments(
                                    args=[
                                        ast.arg(arg='self', annotation=None),
                                        ast.arg(arg='doc', annotation=None)
                                    ],
                                    vararg=None,
                                    kwonlyargs=[],
                                    posonlyargs=[],
                                    kw_defaults=[],
                                    kwarg=None,
                                    defaults=[]
                                ),
                                body=[
                                    ast.Pass(),
                                ],
                                decorator_list=[],
                                lineno=7
                            ),
                            ast.FunctionDef(
                                name='to_disk',
                                args=ast.arguments(
                                    args=[
                                        ast.arg(arg='self', annotation=None),
                                        ast.arg(arg='path', annotation=None),
                                        ast.arg(arg='**kwargs', annotation=None)
                                    ],
                                    vararg=None,
                                    kwonlyargs=[],
                                    posonlyargs=[],
                                    kw_defaults=[],
                                    kwarg=None,
                                    defaults=[]
                                ),
                                body=[
                                    ast.Pass(),
                                ],
                                decorator_list=[],
                                lineno=10
                            ),
                            ast.FunctionDef(
                                name='from_disk',
                                args=ast.arguments(
                                    args=[
                                        ast.arg(arg='self', annotation=None),
                                        ast.arg(arg='path', annotation=None),
                                        ast.arg(arg='**cfg', annotation=None)
                                    ],
                                    vararg=None,
                                    kwonlyargs=[],
                                    posonlyargs=[],
                                    kw_defaults=[],
                                    kwarg=None,
                                    defaults=[]
                                ),
                                body=[
                                    ast.Pass(),
                                ],
                                decorator_list=[],
                                lineno=13
                            )
                        ],
                        decorator_list=[],
                        lineno=16
                    ),
                    ast.Assign(
                        targets=[ast.Subscript(
                            value=ast.Attribute(
                                value=ast.Name(id='Language'),
                                attr='factories'
                            ),
                            slice=ast.Index(value=ast.Constant(value=value1)),

                        )],
                        value=ast.Lambda(
                            args=ast.arguments(
                                posonlyargs=[],
                                args=[
                                    ast.arg(arg='nlp', annotation=None),
                                    ast.arg(arg='**cfg', annotation=None)
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[]
                            ),
                            body=ast.Call(
                                func=ast.Name(id='MyComponent'),
                                args=[
                                    ast.Name(id='nlp')
                                ],
                                keywords=[
                                    ast.keyword(arg=None, value=ast.Name(id='cfg'))
                                ]
                            )
                        ),
                        lineno=20
                    ),
                    ast.Assign(
                        targets=[ast.Name(id='nlp')],
                        value=ast.Call(func=ast.Name(id='English'), args=[], keywords=[]),
                        lineno=23
                    ),
                    ast.Expr(
                        value=ast.Call(
                            func=ast.Attribute(value=ast.Name(id='nlp'), attr='add_pipe'),
                            args=[
                                ast.Call(
                                    func=ast.Attribute(value=ast.Name(id='nlp'), attr='create_pipe'),
                                    args=[ast.Constant(value=value2)],
                                    keywords=[]
                                )
                            ],
                            keywords=[]
                        ),
                        lineno=24
                    ),
                    ast.Assert(
                        test=ast.Compare(
                            left=ast.Attribute(
                                value=ast.Call(
                                    func=ast.Attribute(
                                        value=ast.Name(id='nlp'),
                                        attr='get_pipe',

                                    ),
                                    args=[ast.Constant(value=value2)],
                                    keywords=[]
                                ),
                                attr='categories',

                            ),
                            ops=[ast.Eq()],
                            comparators=[ast.Constant(value='all_categories')]
                        ),
                        msg=None,
                        lineno=25
                    ),
                ],
                type_ignores=[]
            )
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="spacy.language",
                names=[ast.alias(name="Language")],
                level=0,
            ),
            ast.ImportFrom(
                module="spacy.lang.en",
                names=[ast.alias(name="English")],
                level=0,
            )
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, fail_ = self._generate_one()
        value1, value2 = fail_
        test = self.get_empty_test()
        test.body = self._get_assert(value1, value2)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, _ = self._generate_one()
        value1, value2 = pass_
        test = self.get_empty_test()
        test.body = self._get_assert(value1, value2)
        return test, TestResult.PASSING


class SpaCyUnittestGenerator3(
    python.PythonGenerator, UnittestGenerator, SpaCyTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.spacy3_generate)

    @staticmethod
    def _get_assert(
            random_string: str,
            format_: str
    ) -> list[Assign | Assert]:
        return [
            ast.Assign(
                targets=[ast.Name(id='title')],
                value=ast.Constant(value=random_string),
                lineno=1
            ),
            ast.Assign(
                targets=[ast.Name(id='text')],
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id='html'),
                        attr='unescape',

                    ),
                    args=[
                        ast.Constant(value=format_)
                    ],
                    keywords=[]
                ),
                lineno=2
            ),
            ast.Assign(
                targets=[ast.Tuple(
                    elts=[ast.Name(id='clean_text'), ast.Name(id='_')],
                )],
                value=ast.Call(
                    func=ast.Name(id='_process_wp_text'),
                    args=[
                        ast.Name(id='title'),
                        ast.Name(id="text"),
                        ast.Dict(keys=[], values=[])
                    ],
                    keywords=[]
                ),
                lineno=3
            ),
            ast.Assign(
                targets=[ast.Name(id='expected_text')],
                value=ast.Constant(
                    value='Arkæologi er studiet af tidligere tiders menneskelige aktivitet, primært gennem studiet af menneskets materielle levn.'),
                lineno=4
            ),
            ast.Expr(
                value=ast.Call(
                    func=ast.Attribute(value=ast.Name(id="self"), attr="assertEqual"),
                    args=[
                        ast.Call(
                            func=ast.Attribute(value=ast.Name(id='clean_text'), attr='strip',
                                               ),
                            args=[],
                            keywords=[]
                        ),
                        ast.Name(id='expected_text')
                    ],
                    keywords=[]
                ),
                lineno=5
            ),
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="bin.wiki_entity_linking.wikipedia_processor",
                names=[ast.alias(name="_process_wp_text")],
                level=0,
            ),
            ast.Import(
                module="html",
                names=[ast.alias(name="html")],
                level=0,
            ),
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, fail_ = self._generate_one()
        random_string, format_, _ = fail_
        test = self.get_empty_test()
        test.body = self._get_assert(random_string, format_)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, _ = self._generate_one()
        random_string, format_, _ = pass_
        test = self.get_empty_test()
        test.body = self._get_assert(random_string, format_)
        return test, TestResult.PASSING


class SpaCyUnittestGenerator4(
    python.PythonGenerator, UnittestGenerator, SpaCyTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.spacy4_generate)

    @staticmethod
    def _get_assert(input_value: str) -> list[Expr]:
        return [
            ast.Expr(
                value=ast.Call(
                    func=ast.Name(id='conllu2json'),
                    args=[
                        ast.Constant(value=input_value)
                    ],
                    keywords=[]
                ),
                lineno=1
            )
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="spacy.cli.converters.conllu2json",
                names=[ast.alias(name="conllu2json")],
                level=0,
            ),
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, fail_ = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert(fail_)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, _ = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert(pass_)
        return test, TestResult.PASSING


class SpaCyUnittestGenerator5(
    python.PythonGenerator, UnittestGenerator, SpaCyTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.spacy5_generate)

    @staticmethod
    def _get_assert(random_str: str
    ) -> list[Module]:
        return [
            ast.Module(
                body=[
                    ast.FunctionDef(
                        name='pipe',
                        args=ast.arguments(
                            args=[ast.arg(arg='doc', annotation=None)],
                            vararg=None,
                            kwonlyargs=[],
                            posonlyargs=[],
                            kw_defaults=[],
                            kwarg=None,
                            defaults=[]
                        ),
                        body=[
                            ast.Return(
                                value=ast.Name(id='doc')
                            )
                        ],
                        decorator_list=[],
                        returns=None,
                        lineno=1,
                        col_offset=0
                    ),
                    ast.Assign(
                        targets=[ast.Name(id='text')],
                        value=ast.Constant(value=random_str),
                        lineno=3,
                        col_offset=0
                    ),
                    ast.Assign(
                        targets=[ast.Name(id='annots')],
                        value=ast.Dict(
                            keys=[ast.Constant(value="cats")],
                            values=[ast.Dict(
                                keys=[ast.Constant(value="POSITIVE"), ast.Constant(value="NEGATIVE")],
                                values=[ast.Constant(value=1.0), ast.Constant(value=0.0)],
                                lineno=3,
                                col_offset=0
                            )],
                            lineno=3,
                            col_offset=0
                        ),
                        lineno=3,
                        col_offset=0
                    ),
                    ast.Assign(
                        targets=[ast.Name(id='nlp')],
                        value=ast.Call(
                            func=ast.Name(id='Language'),
                            args=[ast.Call(func=ast.Name(id='Vocab'), args=[], keywords=[])],
                            keywords=[],
                            lineno=4,
                            col_offset=0
                        ),
                        lineno=4,
                        col_offset=0
                    ),
                    ast.Expr(
                        value=ast.Call(
                            func=ast.Attribute(
                                value=ast.Name(id='nlp'),
                                attr='add_pipe',

                            ),
                            args=[ast.Name(id='pipe')],
                            keywords=[],
                            lineno=5,
                            col_offset=0
                        ),
                        lineno=5,
                        col_offset=0
                    ),
                    ast.Expr(
                        value=ast.Call(
                            func=ast.Attribute(
                                value=ast.Name(id='nlp'),
                                attr='evaluate',

                            ),
                            args=[
                                ast.List(
                                    elts=[
                                        ast.Tuple(
                                            elts=[
                                                ast.Name(id='text'),
                                                ast.Name(id='annots')
                                            ],

                                            lineno=6,
                                            col_offset=0
                                        )
                                    ],

                                    lineno=6,
                                    col_offset=0
                                )
                            ],
                            keywords=[],
                            lineno=6,
                            col_offset=0
                        ),
                        lineno=6,
                        col_offset=0
                    )
                ],
                type_ignores=[],
                lineno=1,
                col_offset=0
            )
        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="spacy.language",
                names=[ast.alias(name="Language")],
                level=0,
            ),
            ast.ImportFrom(
                module="spacy.vocab",
                names=[ast.alias(name="Vocab")],
                level=0,
            ),
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, fail_ = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert(fail_)
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, _ = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert(pass_)
        return test, TestResult.PASSING


class SpaCyUnittestGenerator6(
    python.PythonGenerator, UnittestGenerator, SpaCyTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.spacy6_generate)

    @staticmethod
    def _get_assert(
    ) -> list[Call]:
        return [

        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="spacy.errors",
                names=[ast.alias(name="Errors")],
                level=0,
            ),
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, fail_ = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert()
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, _ = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert()
        return test, TestResult.PASSING


class SpaCyUnittestGenerator7(
    python.PythonGenerator, UnittestGenerator, SpaCyTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.spacy7_generate)

    @staticmethod
    def _get_assert(
    ) -> list[Call]:
        return [

        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="spacy.errors",
                names=[ast.alias(name="Errors")],
                level=0,
            ),
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, fail_ = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert()
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, _ = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert()
        return test, TestResult.PASSING


class SpaCyUnittestGenerator8(
    python.PythonGenerator, UnittestGenerator, SpaCyTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.spacy8_generate)

    @staticmethod
    def _get_assert(
    ) -> list[Call]:
        return [

        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="spacy.errors",
                names=[ast.alias(name="Errors")],
                level=0,
            ),
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, fail_ = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert()
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, _ = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert()
        return test, TestResult.PASSING


class SpaCyUnittestGenerator9(
    python.PythonGenerator, UnittestGenerator, SpaCyTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.spacy9_generate)

    @staticmethod
    def _get_assert(
    ) -> list[Call]:
        return [

        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="spacy.errors",
                names=[ast.alias(name="Errors")],
                level=0,
            ),
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, fail_ = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert()
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, _ = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert()
        return test, TestResult.PASSING


class SpaCyUnittestGenerator10(
    python.PythonGenerator, UnittestGenerator, SpaCyTestGenerator
):
    def _generate_one(
            self,
    ) -> str:
        return self.generate_values(self.spacy10_generate)

    @staticmethod
    def _get_assert(
    ) -> list[Call]:
        return [

        ]

    def get_imports(self) -> list[ImportFrom]:
        return [
            ast.ImportFrom(
                module="spacy.errors",
                names=[ast.alias(name="Errors")],
                level=0,
            ),
        ]

    def generate_failing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        _, fail_ = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert()
        return test, TestResult.FAILING

    def generate_passing_test(self) -> Tuple[ast.FunctionDef, TestResult]:
        pass_, _ = self._generate_one()
        test = self.get_empty_test()
        test.body = self._get_assert()
        return test, TestResult.PASSING


class SpaCySystemtestGenerator1(SystemtestGenerator, SpaCyTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.spacy1_generate)
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.spacy1_generate)
        return f"{pass_}", TestResult.PASSING


class SpaCySystemtestGenerator2(SystemtestGenerator, SpaCyTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.spacy2_generate)
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.spacy2_generate)
        return f"{pass_}", TestResult.PASSING


class SpaCySystemtestGenerator3(SystemtestGenerator, SpaCyTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, failing = self.generate_values(self.spacy3_generate)
        random_string, _, info = failing
        fail_ = random_string, info
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        passing, _ = self.generate_values(self.spacy3_generate)
        random_string, _, info = passing
        pass_ = random_string, info
        return f"{pass_}", TestResult.PASSING


class SpaCySystemtestGenerator4(SystemtestGenerator, SpaCyTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.spacy4_generate)
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.spacy4_generate)
        return f"{pass_}", TestResult.PASSING


class SpaCySystemtestGenerator5(SystemtestGenerator, SpaCyTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.spacy5_generate)
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.spacy5_generate)
        return f"{pass_}", TestResult.PASSING


class SpaCySystemtestGenerator6(SystemtestGenerator, SpaCyTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.spacy6_generate)
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.spacy6_generate)
        return f"{pass_}", TestResult.PASSING


class SpaCySystemtestGenerator7(SystemtestGenerator, SpaCyTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.spacy7_generate)
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.spacy7_generate)
        return f"{pass_}", TestResult.PASSING


class SpaCySystemtestGenerator8(SystemtestGenerator, SpaCyTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.spacy8_generate)
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.spacy8_generate)
        return f"{pass_}", TestResult.PASSING


class SpaCySystemtestGenerator9(SystemtestGenerator, SpaCyTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.spacy9_generate)
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.spacy9_generate)
        return f"{pass_}", TestResult.PASSING


class SpaCySystemtestGenerator10(SystemtestGenerator, SpaCyTestGenerator):
    def generate_failing_test(self) -> Tuple[str, TestResult]:
        _, fail_ = self.generate_values(self.spacy10_generate)
        return f"{fail_}", TestResult.FAILING

    def generate_passing_test(self) -> Tuple[str, TestResult]:
        pass_, _ = self.generate_values(self.spacy10_generate)
        return f"{pass_}", TestResult.PASSING


grammar: Grammar = {
    "<start>": ["<structure_>"],
    "<structure_>": ["<str_int_sym_><structure_>"],
    "<str_int_sym_>": [
        "<string_><str_int_sym_>",
        "<integer_><str_int_sym_>",
        "<symbols_><str_int_sym_>",
        " ",
    ],
    "<string_>": ["<char_><string_>", "<char_>", ""],
    "<integer_>": ["<digit_><integer_>", "<digit_>", ""],
    "<symbols_>": ["<symbol_><symbols_>", "<symbol_>", ""],
    "<symbol_>": srange(string.punctuation),
    "<digit_>": srange(string.digits),
    "<char_>": srange(string.ascii_letters),
}
assert is_valid_grammar(grammar)

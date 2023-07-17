import ast
import json
from os import PathLike
from pathlib import Path

from tests4py import projects
from tests4py.framework.logger import LOGGER
from tests4py.framework.utils import __setup__, GrammarReport
from tests4py.grammars import antlr


def tests4py_grammar(
    project_name: str,
    bug_id: int,
    grammar_format: str = "python",
    output: PathLike = None,
):
    report = GrammarReport()
    try:
        __setup__()
        project_name = project_name.lower()
        LOGGER.info("Getting grammar for:")
        LOGGER.info(f"PROJECT_NAME: {project_name}")
        LOGGER.info(f"BUG_ID: {bug_id}")

        project = projects.get_project(project_name, bug_id)
        report.project = project

        grammar_format = grammar_format.lower()
        if grammar_format == "python":
            if output is None:
                output = Path("tests4py_grammar.py")
            value = ast.parse(repr(project.grammar)).body[0]
            if isinstance(value, ast.Expr):
                value = value.value
            else:
                raise ValueError("Grammar code does not have the correct format")
            tree = ast.Assign(
                targets=[ast.Name(id="grammar")],
                value=value,
                type_comment=None,
                lineno=0,
            )
            with open(output, "w") as fp:
                fp.write(ast.unparse(tree))
        elif grammar_format == "json":
            if output is None:
                output = Path("tests4py_grammar.json")
            with open(output, "w") as fp:
                json.dump(project.grammar, fp)
        elif grammar_format == "antlr":
            if output is None:
                output = Path("tests4py_grammar.g4")
            antlr.to_antlr4_file(
                output, project.grammar, name=f"{project.project_name}_{project.bug_id}"
            )
        else:
            raise ValueError(f"Unknown grammar format {grammar_format}")
        report.successful = True
    except BaseException as e:
        report.raised = e
        report.successful = False
    return report

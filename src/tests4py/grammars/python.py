import ast
import random
import string
from ast import *
from typing import Optional, Union

from fuzzingbook.GrammarFuzzer import GrammarFuzzer
from fuzzingbook.Grammars import Grammar, srange, is_valid_grammar
from isla.derivation_tree import DerivationTree

from tests4py.grammars.utils import GrammarVisitor, Generator


class PythonVisitor(GrammarVisitor):
    pass


# noinspection PyMethodMayBeStatic,PyUnusedLocal
class ToASTVisitor(PythonVisitor):
    def generic_visit(self, node: DerivationTree) -> AST:
        return self.visit(node.children[0])

    def visit_Module(self, node: DerivationTree) -> Module:
        return Module(
            body=self.visit(node.children[1]),
            type_ignores=self.visit(node.children[3]),
        )

    def visit_Interactive(self, node: DerivationTree) -> Interactive:
        return Interactive(body=self.visit(node.children[1]))

    def visit_Expression(self, node: DerivationTree) -> Expression:
        return Expression(body=self.visit(node.children[1]))

    def visit_FunctionType(self, node: DerivationTree) -> FunctionType:
        return FunctionType(
            argtypes=self.visit(node.children[1]),
            returns=self.visit(node.children[3]),
        )

    def visit_FunctionDef(self, node: DerivationTree) -> FunctionDef:
        return FunctionDef(
            name=self.visit(node.children[1]),
            args=self.visit(node.children[3]),
            body=self.visit(node.children[5]),
            decorator_list=self.visit(node.children[7]),
            returns=self.visit(node.children[9]),
            type_comment=self.visit(node.children[11]),
            lineno=0,
        )

    def visit_AsyncFunctionDef(self, node: DerivationTree) -> AsyncFunctionDef:
        return AsyncFunctionDef(
            name=self.visit(node.children[1]),
            args=self.visit(node.children[3]),
            body=self.visit(node.children[5]),
            decorator_list=self.visit(node.children[7]),
            returns=self.visit(node.children[9]),
            type_comment=self.visit(node.children[11]),
            lineno=0,
        )

    def visit_ClassDef(self, node: DerivationTree) -> ClassDef:
        return ClassDef(
            name=self.visit(node.children[1]),
            bases=self.visit(node.children[3]),
            keywords=self.visit(node.children[5]),
            body=self.visit(node.children[7]),
            decorator_list=self.visit(node.children[9]),
        )

    def visit_Return(self, node: DerivationTree) -> Return:
        return Return(
            value=self.visit(node.children[1]),
        )

    def visit_Delete(self, node: DerivationTree) -> Delete:
        return Delete(
            targets=self.visit(node.children[1]),
        )

    def visit_Assign(self, node: DerivationTree) -> Assign:
        return Assign(
            targets=self.visit(node.children[1]),
            value=self.visit(node.children[3]),
            type_comment=self.visit(node.children[5]),
            lineno=0,
        )

    def visit_AugAssign(self, node: DerivationTree) -> AugAssign:
        return AugAssign(
            target=self.visit(node.children[1]),
            op=self.visit(node.children[3]),
            value=self.visit(node.children[5]),
        )

    def visit_AnnAssign(self, node: DerivationTree) -> AnnAssign:
        return AnnAssign(
            target=self.visit(node.children[1]),
            annotation=self.visit(node.children[3]),
            value=self.visit(node.children[5]),
            simple=self.visit(node.children[7]),
        )

    def visit_For(self, node: DerivationTree) -> For:
        return For(
            target=self.visit(node.children[1]),
            iter=self.visit(node.children[3]),
            body=self.visit(node.children[5]),
            orelse=self.visit(node.children[7]),
            type_comment=self.visit(node.children[9]),
            lineno=0,
        )

    def visit_AsyncFor(self, node: DerivationTree) -> AsyncFor:
        return AsyncFor(
            target=self.visit(node.children[1]),
            iter=self.visit(node.children[3]),
            body=self.visit(node.children[5]),
            orelse=self.visit(node.children[7]),
            type_comment=self.visit(node.children[9]),
            lineno=0,
        )

    def visit_While(self, node: DerivationTree) -> While:
        return While(
            test=self.visit(node.children[1]),
            body=self.visit(node.children[3]),
            orelse=self.visit(node.children[5]),
        )

    def visit_If(self, node: DerivationTree) -> If:
        return If(
            test=self.visit(node.children[1]),
            body=self.visit(node.children[3]),
            orelse=self.visit(node.children[5]),
        )

    def visit_With(self, node: DerivationTree) -> With:
        return With(
            items=self.visit(node.children[1]),
            body=self.visit(node.children[3]),
            type_comment=self.visit(node.children[5]),
            lineno=0,
        )

    def visit_AsyncWith(self, node: DerivationTree) -> AsyncWith:
        return AsyncWith(
            items=self.visit(node.children[1]),
            body=self.visit(node.children[3]),
            type_comment=self.visit(node.children[5]),
            lineno=0,
        )

    def visit_Match(self, node: DerivationTree) -> Match:
        return Match(
            subject=self.visit(node.children[1]),
            cases=self.visit(node.children[3]),
        )

    def visit_Raise(self, node: DerivationTree) -> Raise:
        return Raise(
            exc=self.visit(node.children[1]),
            cause=self.visit(node.children[3]),
        )

    def visit_Try(self, node: DerivationTree) -> Try:
        return Try(
            body=self.visit(node.children[1]),
            handlers=self.visit(node.children[3]),
            orelse=self.visit(node.children[5]),
            finalbody=self.visit(node.children[7]),
        )

    # def visit_TryStar(self, node: DerivationTree) -> TryStar:
    #     return TryStar(
    #         body=self.visit(node.children[1]),
    #         handlers=self.visit(node.children[3]),
    #         orelse=self.visit(node.children[5]),
    #         finalbody=self.visit(node.children[7]),
    #     )

    def visit_Assert(self, node: DerivationTree) -> Assert:
        return Assert(
            test=self.visit(node.children[1]),
            msg=self.visit(node.children[3]),
        )

    def visit_Import(self, node: DerivationTree) -> Import:
        return Import(
            names=self.visit(node.children[1]),
        )

    def visit_ImportFrom(self, node: DerivationTree) -> ImportFrom:
        return ImportFrom(
            module=self.visit(node.children[1]),
            names=self.visit(node.children[3]),
            level=self.visit(node.children[5]),
        )

    def visit_Global(self, node: DerivationTree) -> Global:
        return Global(
            names=self.visit(node.children[1]),
        )

    def visit_Nonlocal(self, node: DerivationTree) -> Nonlocal:
        return Nonlocal(
            names=self.visit(node.children[1]),
        )

    def visit_Expr(self, node: DerivationTree) -> Expr:
        return Expr(
            value=self.visit(node.children[1]),
        )

    def visit_Pass(self, node: DerivationTree) -> Pass:
        return Pass()

    def visit_Break(self, node: DerivationTree) -> Break:
        return Break()

    def visit_Continue(self, node: DerivationTree) -> Continue:
        return Continue()

    def visit_BoolOp(self, node: DerivationTree) -> BoolOp:
        return BoolOp(
            op=self.visit(node.children[1]),
            values=self.visit(node.children[3]),
        )

    def visit_NamedExpr(self, node: DerivationTree) -> NamedExpr:
        return NamedExpr(
            target=self.visit(node.children[1]),
            value=self.visit(node.children[3]),
        )

    def visit_BinOp(self, node: DerivationTree) -> BinOp:
        return BinOp(
            left=self.visit(node.children[1]),
            op=self.visit(node.children[3]),
            right=self.visit(node.children[5]),
        )

    def visit_UnaryOp(self, node: DerivationTree) -> UnaryOp:
        return UnaryOp(
            op=self.visit(node.children[1]),
            operand=self.visit(node.children[3]),
        )

    def visit_Lambda(self, node: DerivationTree) -> Lambda:
        return Lambda(
            args=self.visit(node.children[1]),
            body=self.visit(node.children[3]),
        )

    def visit_IfExp(self, node: DerivationTree) -> IfExp:
        return IfExp(
            test=self.visit(node.children[1]),
            body=self.visit(node.children[3]),
            orelse=self.visit(node.children[5]),
        )

    def visit_Dict(self, node: DerivationTree) -> Dict:
        return Dict(
            keys=self.visit(node.children[1]),
            values=self.visit(node.children[3]),
        )

    def visit_Set(self, node: DerivationTree) -> Set:
        return Set(
            elts=self.visit(node.children[1]),
        )

    def visit_ListComp(self, node: DerivationTree) -> ListComp:
        return ListComp(
            elt=self.visit(node.children[1]),
            generators=self.visit(node.children[3]),
        )

    def visit_SetComp(self, node: DerivationTree) -> SetComp:
        return SetComp(
            elt=self.visit(node.children[1]),
            generators=self.visit(node.children[3]),
        )

    def visit_DictComp(self, node: DerivationTree) -> DictComp:
        return DictComp(
            key=self.visit(node.children[1]),
            value=self.visit(node.children[3]),
            generators=self.visit(node.children[5]),
        )

    def visit_GeneratorExp(self, node: DerivationTree) -> GeneratorExp:
        return GeneratorExp(
            elt=self.visit(node.children[1]),
            generators=self.visit(node.children[3]),
        )

    def visit_Await(self, node: DerivationTree) -> Await:
        return Await(
            value=self.visit(node.children[1]),
        )

    def visit_Yield(self, node: DerivationTree) -> Yield:
        return Yield(
            value=self.visit(node.children[1]),
        )

    def visit_YieldFrom(self, node: DerivationTree) -> YieldFrom:
        return YieldFrom(
            value=self.visit(node.children[1]),
        )

    def visit_Compare(self, node: DerivationTree) -> Compare:
        return Compare(
            left=self.visit(node.children[1]),
            ops=self.visit(node.children[3]),
            comparators=self.visit(node.children[5]),
        )

    def visit_Call(self, node: DerivationTree) -> Call:
        return Call(
            func=self.visit(node.children[1]),
            args=self.visit(node.children[3]),
            keywords=self.visit(node.children[5]),
        )

    def visit_FormattedValue(self, node: DerivationTree) -> FormattedValue:
        return FormattedValue(
            value=self.visit(node.children[1]),
            conversion=self.visit(node.children[3]),
            format_spec=self.visit(node.children[5]),
        )

    def visit_JoinedStr(self, node: DerivationTree) -> JoinedStr:
        return JoinedStr(
            values=self.visit(node.children[1]),
        )

    def visit_Constant(self, node: DerivationTree) -> Constant:
        return Constant(
            value=self.visit(node.children[1]),
            kind=self.visit(node.children[3]),
        )

    def visit_Attribute(self, node: DerivationTree) -> Attribute:
        return Attribute(
            value=self.visit(node.children[1]),
            attr=self.visit(node.children[3]),
        )

    def visit_Subscript(self, node: DerivationTree) -> Subscript:
        return Subscript(
            value=self.visit(node.children[1]),
            slice=self.visit(node.children[3]),
        )

    def visit_Starred(self, node: DerivationTree) -> Starred:
        return Starred(
            value=self.visit(node.children[1]),
        )

    def visit_Name(self, node: DerivationTree) -> Name:
        return Name(
            id=self.visit(node.children[1]),
        )

    def visit_List(self, node: DerivationTree) -> List:
        return List(
            elts=self.visit(node.children[1]),
        )

    def visit_Tuple(self, node: DerivationTree) -> Tuple:
        return Tuple(
            elts=self.visit(node.children[1]),
        )

    def visit_Slice(self, node: DerivationTree) -> Slice:
        return Slice(
            lower=self.visit(node.children[1]),
            upper=self.visit(node.children[3]),
            step=self.visit(node.children[5]),
        )

    def visit_And(self, node: DerivationTree) -> And:
        return And()

    def visit_Or(self, node: DerivationTree) -> Or:
        return Or()

    def visit_Add(self, node: DerivationTree) -> Add:
        return Add()

    def visit_Sub(self, node: DerivationTree) -> Sub:
        return Sub()

    def visit_Mult(self, node: DerivationTree) -> Mult:
        return Mult()

    def visit_MatMult(self, node: DerivationTree) -> MatMult:
        return MatMult()

    def visit_Div(self, node: DerivationTree) -> Div:
        return Div()

    def visit_Mod(self, node: DerivationTree) -> Mod:
        return Mod()

    def visit_Pow(self, node: DerivationTree) -> Pow:
        return Pow()

    def visit_LShift(self, node: DerivationTree) -> LShift:
        return LShift()

    def visit_RShift(self, node: DerivationTree) -> RShift:
        return RShift()

    def visit_BitOr(self, node: DerivationTree) -> BitOr:
        return BitOr()

    def visit_BitXor(self, node: DerivationTree) -> BitXor:
        return BitXor()

    def visit_BitAnd(self, node: DerivationTree) -> BitAnd:
        return BitAnd()

    def visit_FloorDiv(self, node: DerivationTree) -> FloorDiv:
        return FloorDiv()

    def visit_Invert(self, node: DerivationTree) -> Invert:
        return Invert()

    def visit_Not(self, node: DerivationTree) -> Not:
        return Not()

    def visit_UAdd(self, node: DerivationTree) -> UAdd:
        return UAdd()

    def visit_USub(self, node: DerivationTree) -> USub:
        return USub()

    def visit_Eq(self, node: DerivationTree) -> Eq:
        return Eq()

    def visit_NotEq(self, node: DerivationTree) -> NotEq:
        return NotEq()

    def visit_Lt(self, node: DerivationTree) -> Lt:
        return Lt()

    def visit_LtE(self, node: DerivationTree) -> LtE:
        return LtE()

    def visit_Gt(self, node: DerivationTree) -> Gt:
        return Gt()

    def visit_GtE(self, node: DerivationTree) -> GtE:
        return GtE()

    def visit_Is(self, node: DerivationTree) -> Is:
        return Is()

    def visit_IsNot(self, node: DerivationTree) -> IsNot:
        return IsNot()

    def visit_In(self, node: DerivationTree) -> In:
        return In()

    def visit_NotIn(self, node: DerivationTree) -> NotIn:
        return NotIn()

    def visit_comprehension(self, node: DerivationTree) -> comprehension:
        return comprehension(
            target=self.visit(node.children[1]),
            iter=self.visit(node.children[3]),
            ifs=self.visit(node.children[5]),
            is_async=self.visit(node.children[7]),
        )

    def visit_ExceptHandler(self, node: DerivationTree) -> ExceptHandler:
        return ExceptHandler(
            type=self.visit(node.children[1]),
            name=self.visit(node.children[3]),
            body=self.visit(node.children[5]),
        )

    def visit_arguments(self, node: DerivationTree) -> arguments:
        return arguments(
            posonlyargs=self.visit(node.children[1]),
            args=self.visit(node.children[3]),
            vararg=self.visit(node.children[5]),
            kwonlyargs=self.visit(node.children[7]),
            kw_defaults=self.visit(node.children[9]),
            kwarg=self.visit(node.children[11]),
            defaults=self.visit(node.children[13]),
        )

    def visit_arg(self, node: DerivationTree) -> arg:
        return arg(
            arg=self.visit(node.children[1]),
            annotation=self.visit(node.children[3]),
            type_comment=self.visit(node.children[5]),
        )

    def visit_keyword(self, node: DerivationTree) -> keyword:
        return keyword(
            arg=self.visit(node.children[1]),
            value=self.visit(node.children[3]),
        )

    def visit_alias(self, node: DerivationTree) -> alias:
        return alias(
            name=self.visit(node.children[1]),
            asname=self.visit(node.children[3]),
        )

    def visit_withitem(self, node: DerivationTree) -> withitem:
        return withitem(
            context_expr=self.visit(node.children[1]),
            optional_vars=self.visit(node.children[3]),
        )

    def visit_match_case(self, node: DerivationTree) -> match_case:
        return match_case(
            pattern=self.visit(node.children[1]),
            guard=self.visit(node.children[3]),
            body=self.visit(node.children[5]),
        )

    def visit_MatchValue(self, node: DerivationTree) -> MatchValue:
        return MatchValue(
            value=self.visit(node.children[1]),
        )

    def visit_MatchSingleton(self, node: DerivationTree) -> MatchSingleton:
        return MatchSingleton(
            value=self.visit(node.children[1]),
        )

    def visit_MatchSequence(self, node: DerivationTree) -> MatchSequence:
        return MatchSequence(
            patterns=self.visit(node.children[1]),
        )

    def visit_MatchMapping(self, node: DerivationTree) -> MatchMapping:
        return MatchMapping(
            keys=self.visit(node.children[1]),
            patterns=self.visit(node.children[3]),
            rest=self.visit(node.children[5]),
        )

    def visit_MatchClass(self, node: DerivationTree) -> MatchClass:
        return MatchClass(
            cls=self.visit(node.children[1]),
            patterns=self.visit(node.children[3]),
            kwd_attrs=self.visit(node.children[5]),
            kwd_patterns=self.visit(node.children[7]),
        )

    def visit_MatchStar(self, node: DerivationTree) -> MatchStar:
        return MatchStar(
            name=self.visit(node.children[1]),
        )

    def visit_MatchAs(self, node: DerivationTree) -> MatchAs:
        return MatchAs(
            pattern=self.visit(node.children[1]),
            name=self.visit(node.children[3]),
        )

    def visit_MatchOr(self, node: DerivationTree) -> MatchOr:
        return MatchOr(
            patterns=self.visit(node.children[1]),
        )

    def visit_TypeIgnore(self, node: DerivationTree) -> TypeIgnore:
        return TypeIgnore(
            lineno=self.visit(node.children[1]),
            tag=self.visit(node.children[3]),
        )

    def visit_list(self, node: DerivationTree) -> list:
        if len(node.children) > 1:
            return self.visit(node.children[1])
        else:
            return list()

    def visit_elts(self, node: DerivationTree) -> list:
        if len(node.children) == 1:
            return [self.visit(node.children[0])]
        else:
            return self.visit(node.children[0]) + [self.visit(node.children[2])]

    def visit_stmt_list(self, node: DerivationTree) -> list:
        return self.visit_list(node)

    def visit_stmts(self, node: DerivationTree) -> list:
        return self.visit_elts(node)

    def visit_expr_list(self, node: DerivationTree) -> list:
        return self.visit_list(node)

    def visit_exprs(self, node: DerivationTree) -> list:
        return self.visit_elts(node)

    def visit_type_ignore_list(self, node: DerivationTree) -> list:
        return self.visit_list(node)

    def visit_type_ignores(self, node: DerivationTree) -> list:
        return self.visit_elts(node)

    def visit_keyword_list(self, node: DerivationTree) -> list:
        return self.visit_list(node)

    def visit_keywords(self, node: DerivationTree) -> list:
        return self.visit_elts(node)

    def visit_withitem_list(self, node: DerivationTree) -> list:
        return self.visit_list(node)

    def visit_withitems(self, node: DerivationTree) -> list:
        return self.visit_elts(node)

    def visit_match_case_list(self, node: DerivationTree) -> list:
        return self.visit_list(node)

    def visit_match_cases(self, node: DerivationTree) -> list:
        return self.visit_elts(node)

    def visit_excepthandler_list(self, node: DerivationTree) -> list:
        return self.visit_list(node)

    def visit_excepthandlers(self, node: DerivationTree) -> list:
        return self.visit_elts(node)

    def visit_alias_list(self, node: DerivationTree) -> list:
        return self.visit_list(node)

    def visit_aliases(self, node: DerivationTree) -> list:
        return self.visit_elts(node)

    def visit_identifier_list(self, node: DerivationTree) -> list:
        return self.visit_list(node)

    def visit_identifiers(self, node: DerivationTree) -> list:
        return self.visit_elts(node)

    def visit_comprehension_list(self, node: DerivationTree) -> list:
        return self.visit_list(node)

    def visit_comprehensions(self, node: DerivationTree) -> list:
        return self.visit_elts(node)

    def visit_cmpop_list(self, node: DerivationTree) -> list:
        return self.visit_list(node)

    def visit_cmpops(self, node: DerivationTree) -> list:
        return self.visit_elts(node)

    def visit_arg_list(self, node: DerivationTree) -> list:
        return self.visit_list(node)

    def visit_args(self, node: DerivationTree) -> list:
        return self.visit_elts(node)

    def visit_pattern_list(self, node: DerivationTree) -> list:
        return self.visit_list(node)

    def visit_patterns(self, node: DerivationTree) -> list:
        return self.visit_elts(node)

    def visit_optional(self, node: DerivationTree) -> Optional[AST]:
        if node.children:
            return self.visit(node.children[0])
        else:
            return None

    def visit_optional_expr(self, node: DerivationTree) -> Optional[AST]:
        return self.visit_optional(node)

    def visit_optional_string(self, node: DerivationTree) -> Optional[AST]:
        return self.visit_optional(node)

    def visit_optional_identifier(self, node: DerivationTree) -> Optional[AST]:
        return self.visit_optional(node)

    def visit_optional_int(self, node: DerivationTree) -> Optional[AST]:
        return self.visit_optional(node)

    def visit_optional_arg(self, node: DerivationTree) -> Optional[AST]:
        return self.visit_optional(node)

    def visit_optional_pattern(self, node: DerivationTree) -> Optional[AST]:
        return self.visit_optional(node)

    def visit_int(self, node: DerivationTree) -> int:
        return int(node.to_string())

    def visit_string(self, node: DerivationTree) -> str:
        return node.children[0].to_string()

    def visit_identifier(self, node: DerivationTree) -> str:
        return node.to_string()


# noinspection PyTypeChecker
class ToGrammarVisitor(NodeVisitor):
    def visit_list(self, elements, visit=True):
        if visit:
            return f'[{",".join(self.visit(e) for e in elements)}]'.replace(" ", "")
        else:
            return f'[{",".join(elements)}]'.replace(" ", "")

    def visit_Module(self, node: Module) -> str:
        return (
            f"Module({self.visit_list(node.body)},"
            f"{self.visit_list(node.type_ignores)})"
        )

    def visit_Interactive(self, node: Interactive) -> str:
        return f"Interactive({self.visit_list(node.body)})"

    def visit_Expression(self, node: Expression) -> str:
        return f"Expression({self.visit(node.body)})"

    def visit_FunctionType(self, node: FunctionType) -> str:
        return (
            f"FunctionType({self.visit_list(node.argtypes)},"
            f"{self.visit(node.returns)})"
        )

    def visit_FunctionDef(self, node: FunctionDef) -> str:
        return (
            f"FunctionDef({node.name},"
            f"{self.visit(node.args)},"
            f"{self.visit_list(node.body)},"
            f"{self.visit_list(node.decorator_list)},"
            f'{"" if node.returns is None else self.visit(node.returns)},'
            f'{"" if node.type_comment is None else self.visit(node.type_comment)})'
        )

    def visit_AsyncFunctionDef(self, node: AsyncFunctionDef) -> str:
        return (
            f"AsyncFunctionDef({node.name},"
            f"{self.visit(node.args)},"
            f"{self.visit_list(node.body)},"
            f"{self.visit_list(node.decorator_list)},"
            f'{"" if node.returns is None else self.visit(node.returns)},'
            f'{"" if node.type_comment is None else self.visit(node.type_comment)})'
        )

    def visit_ClassDef(self, node: ClassDef) -> str:
        return (
            f"ClassDef({node.name},"
            f"{self.visit_list(node.bases)},"
            f"{self.visit_list(node.keywords)},"
            f"{self.visit_list(node.body)},"
            f"{self.visit_list(node.decorator_list)})"
        )

    def visit_Return(self, node: Return) -> str:
        return f'Return({"" if node.value is None else self.visit(node.value)})'

    def visit_Delete(self, node: Delete) -> str:
        return f"Delete({self.visit_list(node.targets)})"

    def visit_Assign(self, node: Assign) -> str:
        return (
            f"Assign({self.visit_list(node.targets)},"
            f"{self.visit(node.value)},"
            f'{"" if node.type_comment is None else self.visit(node.type_comment)})'
        )

    def visit_AugAssign(self, node: AugAssign) -> str:
        return (
            f"AugAssign({self.visit(node.target)},"
            f"{self.visit(node.op)},"
            f"{self.visit(node.value)})"
        )

    def visit_AnnAssign(self, node: AnnAssign) -> str:
        return (
            f"AnnAssign({self.visit(node.target)},"
            f"{self.visit(node.annotation)},"
            f'{"" if node.value is None else self.visit(node.value)},'
            f"{node.simple})"
        )

    def visit_For(self, node: For) -> str:
        return (
            f"For({self.visit(node.target)},"
            f"{self.visit(node.iter)},"
            f"{self.visit_list(node.body)},"
            f"{self.visit_list(node.orelse)},"
            f'{"" if node.type_comment is None else self.visit(node.type_comment)})'
        )

    def visit_AsyncFor(self, node: AsyncFor) -> str:
        return (
            f"AsyncFor({self.visit(node.target)},"
            f"{self.visit(node.iter)},"
            f"{self.visit_list(node.body)},"
            f"{self.visit_list(node.orelse)},"
            f'{"" if node.type_comment is None else self.visit(node.type_comment)})'
        )

    def visit_While(self, node: While) -> str:
        return (
            f"While({self.visit(node.test)},"
            f"{self.visit_list(node.body)},"
            f"{self.visit_list(node.orelse)})"
        )

    def visit_If(self, node: If) -> str:
        return (
            f"If({self.visit(node.test)},"
            f"{self.visit_list(node.body)},"
            f"{self.visit_list(node.orelse)})"
        )

    def visit_With(self, node: With) -> str:
        return (
            f"With({self.visit_list(node.items)},"
            f"{self.visit_list(node.body)},"
            f'{"" if node.type_comment is None else self.visit(node.type_comment)})'
        )

    def visit_AsyncWith(self, node: AsyncWith) -> str:
        return (
            f"AsyncWith({self.visit_list(node.items)},"
            f"{self.visit_list(node.body)},"
            f'{"" if node.type_comment is None else self.visit(node.type_comment)})'
        )

    def visit_Match(self, node: Match) -> str:
        return f"Match({self.visit(node.subject)}," f"{self.visit_list(node.cases)})"

    def visit_Raise(self, node: Raise) -> str:
        return (
            f'Raise({"" if node.exc is None else self.visit(node.exc)},'
            f'{"" if node.cause is None else self.visit(node.cause)})'
        )

    def visit_Try(self, node: Try) -> str:
        return (
            f"Try({self.visit_list(node.body)},"
            f"{self.visit_list(node.handlers)},"
            f"{self.visit_list(node.orelse)},"
            f"{self.visit_list(node.finalbody)})"
        )

    def visit_Assert(self, node: Assert) -> str:
        return (
            f"Assert({self.visit(node.test)},"
            f'{"" if node.msg is None else self.visit(node.msg)})'
        )

    def visit_Import(self, node: Import) -> str:
        return f"Import({self.visit_list(node.names)})"

    def visit_ImportFrom(self, node: ImportFrom) -> str:
        return (
            f'ImportFrom({"" if node.module is None else node.module},'
            f"{self.visit_list(node.names)},"
            f'{"" if node.level is None else node.level})'
        )

    def visit_Global(self, node: Global) -> str:
        return f"Global({self.visit_list(node.names, visit=False)})"

    def visit_Nonlocal(self, node: Nonlocal) -> str:
        return f"Nonlocal({self.visit_list(node.names)})"

    def visit_Expr(self, node: Expr) -> str:
        return f"Expr({self.visit(node.value)})"

    def visit_Pass(self, node: Pass) -> str:
        return f"Pass()"

    def visit_Break(self, node: Break) -> str:
        return f"Break()"

    def visit_Continue(self, node: Continue) -> str:
        return f"Continue()"

    def visit_BoolOp(self, node: BoolOp) -> str:
        return f"BoolOp({self.visit(node.op)}," f"{self.visit_list(node.values)})"

    def visit_NamedExpr(self, node: NamedExpr) -> str:
        return f"NamedExpr({self.visit(node.target)}," f"{self.visit(node.value)})"

    def visit_BinOp(self, node: BinOp) -> str:
        return (
            f"BinOp({self.visit(node.left)},"
            f"{self.visit(node.op)},"
            f"{self.visit(node.right)})"
        )

    def visit_UnaryOp(self, node: UnaryOp) -> str:
        return f"UnaryOp({self.visit(node.op)}," f"{self.visit(node.operand)})"

    def visit_Lambda(self, node: Lambda) -> str:
        return f"Lambda({self.visit(node.args)}," f"{self.visit(node.body)})"

    def visit_IfExp(self, node: IfExp) -> str:
        return (
            f"IfExp({self.visit(node.test)},"
            f"{self.visit(node.body)},"
            f"{self.visit(node.orelse)})"
        )

    def visit_Dict(self, node: Dict) -> str:
        return f"Dict({self.visit_list(node.keys)}," f"{self.visit_list(node.values)})"

    def visit_Set(self, node: Set) -> str:
        return f"Set({self.visit_list(node.elts)})"

    def visit_ListComp(self, node: ListComp) -> str:
        return (
            f"ListComp({self.visit(node.elt)}," f"{self.visit_list(node.generators)})"
        )

    def visit_SetComp(self, node: SetComp) -> str:
        return f"SetComp({self.visit(node.elt)}," f"{self.visit_list(node.generators)})"

    def visit_DictComp(self, node: DictComp) -> str:
        return (
            f"ListComp({self.visit(node.key)},"
            f"{self.visit(node.value)},"
            f"{self.visit_list(node.generators)})"
        )

    def visit_GeneratorExp(self, node: GeneratorExp) -> str:
        return (
            f"GeneratorExp({self.visit(node.elt)},"
            f"{self.visit_list(node.generators)})"
        )

    def visit_Await(self, node: Await) -> str:
        return f"Await({self.visit(node.value)})"

    def visit_Yield(self, node: Yield) -> str:
        return f'Yield({"" if node.value is None else self.visit(node.value)})'

    def visit_YieldFrom(self, node: YieldFrom) -> str:
        return f"YieldFrom({self.visit(node.value)})"

    def visit_Compare(self, node: Compare) -> str:
        return (
            f"Compare({self.visit(node.left)},"
            f"{self.visit_list(node.ops)},"
            f"{self.visit_list(node.comparators)})"
        )

    def visit_Call(self, node: Call) -> str:
        return (
            f"Call({self.visit(node.func)},"
            f"{self.visit_list(node.args)},"
            f"{self.visit_list(node.keywords)})"
        )

    def visit_FormattedValue(self, node: FormattedValue) -> str:
        return (
            f"FormattedValue({self.visit(node.value)},"
            f"{node.conversion},"
            f'{"" if node.format_spec is None else self.visit(node.format_spec)})'
        )

    def visit_JoinedStr(self, node: JoinedStr) -> str:
        return f"JoinedStr({self.visit_list(node.values)})"

    def visit_Constant(self, node: Constant) -> str:
        return (
            f"Constant({repr(node.value)}," f'{"" if node.kind is None else node.kind})'
        )

    def visit_Attribute(self, node: Attribute) -> str:
        return f"Attribute({self.visit(node.value)}," f"{node.attr})"

    def visit_Subscript(self, node: Subscript) -> str:
        return f"Subscript({self.visit(node.value)}," f"{self.visit(node.slice)})"

    def visit_Starred(self, node: Starred) -> str:
        return f"Starred({self.visit(node.value)}," f"{self.visit(node.ctx)})"

    def visit_Name(self, node: Name) -> str:
        return f"Name({node.id})"

    def visit_List(self, node: List) -> str:
        return f"List({self.visit_list(node.elts)})"

    def visit_Tuple(self, node: Tuple) -> str:
        return f"Tuple({self.visit_list(node.elts)})"

    def visit_Slice(self, node: Slice) -> str:
        return (
            f'Slice({"" if node.lower is None else self.visit(node.lower)},'
            f'{"" if node.upper is None else self.visit(node.upper)},'
            f'{"" if node.step is None else self.visit(node.step)})'
        )

    # def visit_Load(self, node: Load) -> str:
    #     return 'Load()'
    #
    # def visit_Store(self, node: Store) -> str:
    #     return 'Store()'

    def visit_Del(self, node: Del) -> str:
        return "Del()"

    def visit_And(self, node: And) -> str:
        return "And()"

    def visit_Or(self, node: Or) -> str:
        return "Or()"

    def visit_Add(self, node: Add) -> str:
        return "Add()"

    def visit_Sub(self, node: Sub) -> str:
        return "Sub()"

    def visit_Mult(self, node: Mult) -> str:
        return "Mult()"

    def visit_MatMult(self, node: MatMult) -> str:
        return "MatMult()"

    def visit_Div(self, node: Div) -> str:
        return "Div()"

    def visit_Mod(self, node: Mod) -> str:
        return "Mod()"

    def visit_Pow(self, node: Pow) -> str:
        return "Pow()"

    def visit_LShift(self, node: LShift) -> str:
        return "LShift()"

    def visit_RShift(self, node: RShift) -> str:
        return "RShift()"

    def visit_BitOr(self, node: BitOr) -> str:
        return "BitOr()"

    def visit_BitXor(self, node: BitXor) -> str:
        return "BitXor()"

    def visit_BitAnd(self, node: BitAnd) -> str:
        return "BitAnd()"

    def visit_FloorDiv(self, node: FloorDiv) -> str:
        return "FloorDiv()"

    def visit_Invert(self, node: Invert) -> str:
        return "Invert()"

    def visit_Not(self, node: Not) -> str:
        return "Not()"

    def visit_UAdd(self, node: UAdd) -> str:
        return "UAdd()"

    def visit_USub(self, node: USub) -> str:
        return "USub()"

    def visit_Eq(self, node: Eq) -> str:
        return "Eq()"

    def visit_NotEq(self, node: NotEq) -> str:
        return "NotEq()"

    def visit_Lt(self, node: Lt) -> str:
        return "Lt()"

    def visit_LtE(self, node: LtE) -> str:
        return "LtE()"

    def visit_Gt(self, node: Gt) -> str:
        return "Gt()"

    def visit_GtE(self, node: GtE) -> str:
        return "GtE()"

    def visit_Is(self, node: Is) -> str:
        return "Is()"

    def visit_IsNot(self, node: IsNot) -> str:
        return "IsNot()"

    def visit_In(self, node: In) -> str:
        return "In()"

    def visit_NotIn(self, node: NotIn) -> str:
        return "NotIn()"

    def visit_comprehension(self, node: comprehension) -> str:
        return (
            f"comprehension({self.visit(node.target)},"
            f"{self.visit(node.iter)},"
            f"{self.visit_list(node.ifs)},"
            f"{node.is_async})"
        )

    def visit_ExceptHandler(self, node: ExceptHandler) -> str:
        return (
            f'ExceptHandler({"" if node.type is None else self.visit(node.type)},'
            f'{"" if node.name is None else node.name},'
            f"{self.visit_list(node.body)})"
        )

    def visit_arguments(self, node: arguments) -> str:
        return (
            f"arguments({self.visit_list(node.posonlyargs)},"
            f"{self.visit_list(node.args)},"
            f'{"" if node.vararg is None else self.visit(node.vararg)},'
            f"{self.visit_list(node.kwonlyargs)},"
            f"{self.visit_list(node.kw_defaults)},"
            f'{"" if node.kwarg is None else self.visit(node.kwarg)},'
            f"{self.visit_list(node.defaults)})"
        )

    def visit_arg(self, node: arg) -> str:
        return (
            f"arg({node.arg},"
            f'{"" if node.annotation is None else self.visit(node.annotation)},'
            f'{"" if node.type_comment is None else self.visit(node.type_comment)})'
        )

    def visit_keyword(self, node: keyword) -> str:
        return (
            f'keyword({"" if node.arg is None else node.arg},'
            f"{self.visit(node.value)})"
        )

    def visit_alias(self, node: alias) -> str:
        return (
            f"alias({node.name},"
            f'{"" if node.asname is None else self.visit(node.asname)})'
        )

    def visit_withitem(self, node: withitem) -> str:
        return (
            f"withitem({self.visit(node.context_expr)},"
            f'{"" if node.optional_vars is None else self.visit(node.optional_vars)})'
        )

    def visit_match_case(self, node: match_case) -> str:
        return (
            f"match_case({self.visit(node.pattern)},"
            f'{"" if node.guard is None else self.visit(node.guard)},'
            f"{self.visit_list(node.body)})"
        )

    def visit_MatchValue(self, node: MatchValue) -> str:
        return f"MatchValue({self.visit(node.value)})"

    def visit_MatchSingleton(self, node: MatchSingleton) -> str:
        return f"MatchSingleton({self.visit(node.value)})"

    def visit_MatchSequence(self, node: MatchSequence) -> str:
        return f"Await({self.visit_list(node.patterns)})"

    def visit_MatchMapping(self, node: MatchMapping) -> str:
        return (
            f"MatchMapping({self.visit_list(node.keys)},"
            f"{self.visit_list(node.patterns)},"
            f'{"" if node.rest is None else self.visit(node.rest)})'
        )

    def visit_MatchClass(self, node: MatchClass) -> str:
        return (
            f"Await({self.visit(node.cls)},"
            f"{self.visit_list(node.patterns)},"
            f"{self.visit_list(node.kwd_attrs)},"
            f"{self.visit_list(node.kwd_patterns)})"
        )

    def visit_MatchStar(self, node: MatchStar) -> str:
        return f'MatchStar({"" if node.name is None else self.visit(node.name)})'

    def visit_MatchAs(self, node: MatchAs) -> str:
        return (
            f'MatchAs({"" if node.pattern is None else self.visit(node.pattern)},'
            f'{"" if node.name is None else self.visit(node.name)})'
        )

    def visit_MatchOr(self, node: MatchOr) -> str:
        return f"MatchOr({self.visit_list(node.patterns)})"

    @staticmethod
    def visit_TypeIgnore(node: TypeIgnore) -> str:
        return f"TypeIgnore({node.lineno}," f'"{node.tag}")'


class PythonGenerator(Generator):
    class Scope:
        def __init__(self, parent=None):
            self.variables = set()
            self.functions = dict()
            self.parent = parent

        def enter(self):
            return PythonGenerator.Scope(self)

        def exit(self):
            return self.parent if self.parent else self

        def add_variable(self, variable: str):
            self.variables.add(variable)

        def add_function(self, function: str, args: int):
            self.functions[function] = args

        def get_variables(self) -> set:
            return (
                self.variables.union(self.parent.get_variables())
                if self.parent
                else self.variables
            )

        def get_variable(self) -> Optional[str]:
            variables = self.get_variables()
            if variables:
                return random.choice(tuple(variables))
            else:
                return None

        def get_functions(self) -> dict:
            if self.parent:
                functions = self.parent.get_functions()
                functions.update(self.functions)
                return functions
            else:
                return dict(self.functions)

        def get_function(self) -> tuple[Optional[str], int]:
            functions = self.get_functions()
            if functions:
                selection = random.choice(tuple(functions.keys()))
                return selection, functions[selection]
            else:
                return None, 0

        def get_args(self, function: str) -> Optional[int]:
            functions = self.get_functions()
            if function in functions:
                return functions[function]
            else:
                return None

    def __init__(
        self,
        limit_stmt_per_block=10,
        limit_stmt_depth=4,
        limit_expr_depth=4,
        limit_args_per_function=4,
        limit_assign_target=1,
    ):
        self.limit_expr_depth = limit_expr_depth
        self.limit_stmt_depth = limit_stmt_depth
        self.limit_assign_target = limit_assign_target
        self.limit_stmt_per_block = limit_stmt_per_block
        self.limit_args_per_function = limit_args_per_function
        self.is_in_function = False
        self.stmt_depth = 0
        self.expr_depth = 0
        self.scope = PythonGenerator.Scope()
        self.identifier_fuzzer = GrammarFuzzer(
            GENERATIVE_GRAMMAR, start_symbol="<identifier>"
        )

    def reset(self):
        self.scope = PythonGenerator.Scope()
        self.is_in_function = False
        self.stmt_depth = 0
        self.expr_depth = 0

    def enter_scope(self):
        self.scope = self.scope.enter()

    def exit_scope(self):
        self.scope = self.scope.exit()

    def generate(self):
        return ast.unparse(self.generate_ast())

    def _generate_Module(self) -> Module:
        return Module(body=self._generate_stmt_list(), type_ignores=[])

    def _generate_stmt_list(self) -> list[stmt]:
        stmts = [
            self._generate_stmt()
            for _ in range(random.randint(0, self.limit_stmt_per_block))
        ]
        if len(stmts) > 0:
            return stmts
        else:
            return [self._generate_Pass()]

    def _generate_stmt(self) -> stmt:
        choices = [
            self._generate_Assign,
            self._generate_Expr,
            self._generate_Pass,
        ]
        if self.stmt_depth < self.limit_stmt_depth:
            choices += [
                self._generate_FunctionDef,
                self._generate_If,
            ]
        if self.is_in_function:
            choices.append(self._generate_Return)
        self.stmt_depth += 1
        stmt_ = random.choice(choices)()
        self.stmt_depth -= 1
        return stmt_

    def _generate_FunctionDef(self, num_args: Optional[int] = None) -> FunctionDef:
        name = self._generate_identifier()
        self.enter_scope()
        args = self._generate_arguments(num_args)
        prev = self.is_in_function
        self.is_in_function = True
        body = self._generate_stmt_list()
        self.is_in_function = prev
        return_ = self._generate_Return()
        self.exit_scope()
        self.scope.add_function(name, len(args.args))
        return FunctionDef(
            name=name,
            args=args,
            body=body + [return_],
            decorator_list=[],
            lineno=0,
        )

    def _generate_If(self) -> If:
        self.enter_scope()
        body = self._generate_stmt_list()
        self.exit_scope()
        self.enter_scope()
        orelse = self._generate_stmt_list()
        self.exit_scope()
        return If(
            test=self._generate_expr(),
            body=body,
            orelse=orelse,
        )

    def _generate_Assign(self) -> Assign:
        targets = self._generate_targets()
        if len(targets) > 1:
            value = Tuple(elts=[self._generate_expr() for _ in range(len(targets))])
        else:
            value = self._generate_expr()
        return Assign(
            targets=targets,
            value=value,
            lineno=0,
        )

    def _generate_Expr(self) -> Expr:
        return Expr(value=self._generate_expr())

    @staticmethod
    def _generate_Pass() -> Pass:
        return Pass()

    def _generate_Return(self) -> Return:
        return Return(value=self._generate_expr())

    def _generate_identifier(self) -> str:
        identifier = self.identifier_fuzzer.fuzz()
        while identifier in [
            "as",
            "def",
            "in",
            "is",
            "not",
            "if",
            "match",
            "case",
            "class",
            "while",
            "for",
            "else",
            "try",
            "finally",
            "except",
            "or",
            "and",
        ]:
            identifier = self.identifier_fuzzer.fuzz()
        return identifier

    def _generate_arguments(self, num_args: Optional[int] = None) -> arguments:
        return arguments(
            args=[
                self._generate_arg()
                for _ in range(
                    random.randint(0, self.limit_args_per_function)
                    if num_args is None
                    else num_args
                )
            ],
            posonlyargs=[],
            defaults=[],
            kwonlyargs=[],
            kw_defaults=[],
        )

    def _generate_expr(self) -> expr:
        choices = [
            self._generate_Constant,
            self._generate_Name,
        ]
        if self.expr_depth < self.limit_expr_depth:
            choices += [
                self._generate_BoolOp,
                self._generate_BinOp,
                self._generate_UnaryOp,
                self._generate_Compare,
                self._generate_Call,
            ]
        self.expr_depth += 1
        expr_ = random.choice(choices)()
        self.expr_depth -= 1
        return expr_

    def _generate_targets(self) -> list[Name]:
        return [
            Name(id=self._generate_identifier())
            for _ in range(0, 1 + random.randrange(0, self.limit_assign_target))
        ]

    def _generate_arg(self) -> arg:
        identifier = self._generate_identifier()
        while identifier in self.scope.variables:
            identifier = self._generate_identifier()
        self.scope.add_variable(identifier)
        return arg(arg=identifier)

    def _generate_BoolOp(self) -> BoolOp:
        return BoolOp(
            op=random.choice((And(), Or())),
            values=[self._generate_expr(), self._generate_expr()],
        )

    def _generate_BinOp(self) -> BinOp:
        return BinOp(
            left=self._generate_expr(),
            op=random.choice((Add(), Sub(), Mult())),
            right=self._generate_expr(),
        )

    def _generate_UnaryOp(self) -> UnaryOp:
        return UnaryOp(
            op=random.choice((Not(), UAdd(), USub())), operand=self._generate_expr()
        )

    def _generate_Compare(self) -> Compare:
        return Compare(
            left=self._generate_expr(),
            ops=[random.choice((Eq(), NotEq(), Lt(), LtE(), Gt(), GtE()))],
            comparators=[self._generate_expr()],
        )

    def _generate_Call(self, function: Optional[str] = None) -> Union[Call | expr]:
        num_args = None
        if function:
            num_args = self.scope.get_args(function)
        if num_args is None:
            function, num_args = self.scope.get_function()
        if function:
            return Call(
                func=Name(id=function),
                args=[self._generate_expr() for _ in range(num_args)],
                keywords=[],
            )
        else:
            return self._generate_expr()

    @staticmethod
    def _generate_Constant() -> Constant:
        return Constant(value=random.randint(0, 10))

    def _generate_Name(self) -> Union[Name | Constant]:
        variable = self.scope.get_variable()
        if variable:
            return Name(id=variable)
        else:
            return self._generate_Constant()

    def generate_ast(self) -> AST:
        return self._generate_Module()


GRAMMAR: Grammar = {
    "<start>": ["<mod>"],
    "<mod>": ["<Module>", "<Interactive>", "<Expression>", "<FunctionType>"],
    "<Module>": ["Module(<stmt_list>,<type_ignore_list>)"],
    "<Interactive>": ["Interactive(<stmt_list>)"],
    "<Expression>": ["Expression(<expr>)"],
    "<FunctionType>": ["FunctionType(<expr_list>,<expr>)"],
    # Lists
    "<stmt_list>": ["[]", "[<stmts>]"],
    "<stmts>": ["<stmt>", "<stmts>,<stmt>"],
    "<expr_list>": ["[]", "[<exprs>]"],
    "<exprs>": ["<expr>", "<exprs>,<expr>"],
    "<type_ignore_list>": ["[]", "[<type_ignores>]"],
    "<type_ignores>": ["<type_ignore>", "<type_ignores>,<type_ignore>"],
    "<keyword_list>": ["[]", "[<keywords>]"],
    "<keywords>": ["<keyword>", "<keywords>,<keyword>"],
    "<withitem_list>": ["[]", "[<withitems>]"],
    "<withitems>": ["<withitem>", "<withitems>,<withitem>"],
    "<match_case_list>": ["[]", "[<match_cases>]"],
    "<match_cases>": ["<match_case>", "<match_cases>,<match_case>"],
    "<excepthandler_list>": ["[]", "[<excepthandlers>]"],
    "<excepthandlers>": ["<excepthandler>", "<excepthandlers>,<excepthandler>"],
    "<alias_list>": ["[]", "[<aliases>]"],
    "<aliases>": ["<alias>", "<aliases>,<alias>"],
    "<identifier_list>": ["[]", "[<identifiers>]"],
    "<identifiers>": ["<identifier>", "<identifiers>,<identifier>"],
    "<comprehension_list>": ["[]", "[<comprehensions>]"],
    "<comprehensions>": ["<comprehension>", "<comprehensions>,<comprehension>"],
    "<cmpop_list>": ["[]", "[<cmpops>]"],
    "<cmpops>": ["<cmpop>", "<cmpops>,<cmpop>"],
    "<arg_list>": ["[]", "[<args>]"],
    "<args>": ["<arg>", "<args>,<arg>"],
    "<pattern_list>": ["[]", "[<patterns>]"],
    "<patterns>": ["<pattern>", "<patterns>,<pattern>"],
    # Optionals
    "<optional_expr>": ["", "<expr>"],
    "<optional_string>": ["", "<string>"],
    "<optional_identifier>": ["", "<identifier>"],
    "<optional_int>": ["", "<int>"],
    "<optional_arg>": ["", "<arg>"],
    "<optional_pattern>": ["", "<pattern>"],
    # Statements
    "<stmt>": [
        "<FunctionDef>",
        "<AsyncFunctionDef>",
        "<ClassDef>",
        "<Return>",
        "<Delete>",
        "<Assign>",
        "<AugAssign>",
        "<AnnAssign>",
        "<For>",
        "<AsyncFor>",
        "<While>",
        "<If>",
        "<With>",
        "<AsyncWith>",
        "<Match>",
        "<Raise>",
        "<Try>",
        # '<TryStar>',
        "<Assert>",
        "<Import>",
        "<ImportFrom>",
        "<Global>",
        "<Nonlocal>",
        "<Expr>",
        "<Pass>",
        "<Break>",
        "<Continue>",
    ],
    "<FunctionDef>": [
        "FunctionDef(<identifier>,<arguments>,<stmt_list>,<expr_list>,<optional_expr>,<optional_string>)",
    ],
    "<AsyncFunctionDef>": [
        "AsyncFunctionDef(<identifier>,<arguments>,<stmt_list>,<expr_list>,<optional_expr>,<optional_string>)",
    ],
    "<ClassDef>": [
        "ClassDef(<identifier>,<expr_list>,<keyword_list>,<stmt_list>,<expr_list>)",
    ],
    "<Return>": [
        "Return(<optional_expr>)",
    ],
    "<Delete>": [
        "Delete(<expr_list>)",
    ],
    "<Assign>": [
        "Assign(<expr_list>,<expr>,<optional_string>)",
    ],
    "<AugAssign>": [
        "AugAssign(<expr>,<operator>,<expr>)",
    ],
    "<AnnAssign>": [
        "AnnAssign(<expr>,<expr>,<optional_expr>,<int>)",
    ],
    "<For>": [
        "For(<expr>,<expr>,<stmt_list>,<stmt_list>,<optional_string>)",
    ],
    "<AsyncFor>": [
        "AsyncFor(<expr>,<expr>,<stmt_list>,<stmt_list>,<optional_string>)",
    ],
    "<While>": ["While(<expr>,<stmt_list>,<stmt_list>)"],
    "<If>": ["If(<expr>,<stmt_list>,<stmt_list>)"],
    "<With>": [
        "With(<withitem_list>,<stmt_list>,<optional_string>)",
    ],
    "<AsyncWith>": [
        "AsyncWith(<withitem_list>,<stmt_list>,<optional_string>)",
    ],
    "<Match>": ["Match(<expr>,<match_case_list>)"],
    "<Raise>": [
        "Raise(<optional_expr>,<optional_expr>)",
    ],
    "<Try>": ["Try(<stmt_list>,<excepthandler_list>,<stmt_list>,<stmt_list>)"],
    # '<TryStar>': [
    #     'TryStar(<stmt_list>,<excepthandler_list>,<stmt_list>,<stmt_list>)'
    # ],
    "<Assert>": [
        "Assert(<expr>,<optional_expr>)",
    ],
    "<Import>": [
        "Import(<alias_list>)",
    ],
    "<ImportFrom>": [
        "ImportFrom(<optional_identifier>,<alias_list>,<optional_int>)",
    ],
    "<Global>": [
        "Global(<identifier_list>)",
    ],
    "<Nonlocal>": [
        "Nonlocal(<identifier_list>)",
    ],
    "<Expr>": [
        "Expr(<expr>)",
    ],
    "<Pass>": [
        "Pass()",
    ],
    "<Break>": [
        "Break()",
    ],
    "<Continue>": [
        "Continue()",
    ],
    # Expressions
    "<expr>": [
        "<BoolOp>",
        "<NamedExpr>",
        "<BinOp>",
        "<UnaryOp>",
        "<Lambda>",
        "<IfExp>",
        "<Dict>",
        "<Set>",
        "<ListComp>",
        "<SetComp>",
        "<DictComp>",
        "<GeneratorExp>",
        "<Await>",
        "<Yield>",
        "<YieldFrom>",
        "<Compare>",
        "<Call>",
        "<FormattedValue>",
        "<JoinedStr>",
        "<Constant>",
        "<Attribute>",
        "<Subscript>",
        "<Starred>",
        "<Name>",
        "<List>",
        "<Tuple>",
    ],
    "<BoolOp>": ["BoolOp(<boolop>,<expr_list>)"],
    "<NamedExpr>": ["NamedExpr(<expr>,<expr>)"],
    "<BinOp>": ["BinOp(<expr>,<operator>,<expr>)"],
    "<UnaryOp>": ["UnaryOp(<unaryop>,<expr>)"],
    "<Lambda>": ["Lambda(<arguments>,<expr>)"],
    "<IfExp>": ["IfExp(<expr>,<expr>,<expr>)"],
    "<Dict>": ["Dict(<expr_list>,<expr_list>)"],
    "<Set>": ["Set(<expr_list>)"],
    "<ListComp>": ["ListComp(<expr>,<comprehension_list>)"],
    "<SetComp>": ["SetComp(<expr>,<comprehension_list>)"],
    "<DictComp>": ["DictComp(<expr>,<expr>,<comprehension_list>)"],
    "<GeneratorExp>": ["GeneratorExp(<expr>,<comprehension_list>)"],
    "<Await>": ["Await(<expr>)"],
    "<Yield>": [
        "Yield(<optional_expr>)",
    ],
    "<YieldFrom>": [
        "YieldFrom(<optional_expr>)",
    ],
    "<Compare>": ["Compare(<expr>,<cmpop_list>,<expr_list>)"],
    "<Call>": ["Call(<expr>,<expr_list>,<keyword_list>)"],
    "<FormattedValue>": ["FormattedValue(<expr>,<int>,<optional_expr>)"],
    "<JoinedStr>": ["JoinedStr(<expr_list>)"],
    "<Constant>": [
        "Constant(<constant>,<optional_string>)",
    ],
    "<Attribute>": ["Attribute(<expr>,<identifier>)"],
    "<Subscript>": ["Subscript(<expr>,<expr>)", "Subscript(<expr>,<Slice>)"],
    "<Starred>": ["Starred(<expr>)"],
    "<Name>": ["Name(<identifier>)"],
    "<List>": ["List(<expr_list>)"],
    "<Tuple>": ["Tuple(<expr_list>)"],
    "<Slice>": [
        "Slice(<optional_expr>,<optional_expr>,<optional_expr>)",
    ],
    # Contexts
    # '<expr_context>': [
    #    '<Load>',
    #    '<Store>',
    #    '<Del>',
    # ],
    # '<Load>': ['Load()'],
    # '<Store>': ['Store()'],
    # '<Del>': ['Del()'],
    # Operators
    "<boolop>": [
        "<And>",
        "<Or>",
    ],
    "<And>": ["And()"],
    "<Or>": ["Or()"],
    "<operator>": [
        "<Add>",
        "<Sub>",
        "<Mult>",
        "<MatMult>",
        "<Div>",
        "<Mod>",
        "<Pow>",
        "<LShift>",
        "<RShift>",
        "<BitOr>",
        "<BitXor>",
        "<BitAnd>",
        "<FloorDiv>",
    ],
    "<Add>": ["Add()"],
    "<Sub>": ["Sub()"],
    "<Mult>": ["Mult()"],
    "<MatMult>": ["MatMult()"],
    "<Div>": ["Div()"],
    "<Mod>": ["Mod()"],
    "<Pow>": ["Pow()"],
    "<LShift>": ["LShift()"],
    "<RShift>": ["RShift()"],
    "<BitOr>": ["BitOr()"],
    "<BitXor>": ["BitXor()"],
    "<BitAnd>": ["BitAnd()"],
    "<FloorDiv>": ["FloorDiv()"],
    "<unaryop>": [
        "<Invert>",
        "<Not>",
        "<UAdd>",
        "<USub>",
    ],
    "<Invert>": ["Invert()"],
    "<Not>": ["Not()"],
    "<UAdd>": ["UAdd()"],
    "<USub>": ["USub()"],
    "<cmpop>": [
        "<Eq>",
        "<NotEq>",
        "<Lt>",
        "<LtE>",
        "<Gt>",
        "<GtE>",
        "<Is>",
        "<IsNot>",
        "<In>",
        "<NotIn>",
    ],
    "<Eq>": ["Eq()"],
    "<NotEq>": ["NotEq()"],
    "<Lt>": ["Lt()"],
    "<LtE>": ["LtE()"],
    "<Gt>": ["Gt()"],
    "<GtE>": ["GtE()"],
    "<Is>": ["Is()"],
    "<IsNot>": ["IsNot()"],
    "<In>": ["In()"],
    "<NotIn>": ["NotIn()"],
    "<comprehension>": ["<comprehension>(<expr>,<expr>,<expr_list>,<int>)"],
    # Exception Handling
    "<excepthandler>": ["<ExceptHandler>"],
    "<ExceptHandler>": [
        "ExceptHandler(<optional_expr>,<optional_identifier>,<stmt_list>)",
    ],
    # Arguments
    "<arguments>": [
        "arguments(<arg_list>,<arg_list>,<optional_arg>,<arg_list>,<expr_list>,<optional_arg>,<expr_list>)",
    ],
    "<arg>": [
        "arg(<identifier>,<optional_expr>,<optional_string>)",
    ],
    "<keyword>": [
        "keyword(<optional_identifier>,<expr>)",
    ],
    "<alias>": [
        "alias(<identifier>,<optional_identifier>)",
    ],
    "<withitem>": [
        "withitem(<expr>,<optional_expr>)",
    ],
    "<match_case>": [
        "match_case(<pattern>,<optional_expr>,<stmt_list>)",
    ],
    "<pattern>": [
        "<MatchValue>",
        "<MatchSingleton>",
        "<MatchSequence>",
        "<MatchMapping>",
        "<MatchClass>",
        "<MatchStar>",
        "<MatchAs>",
        "<MatchOr>",
    ],
    "<MatchValue>": ["MatchValue(<expr>)"],
    "<MatchSingleton>": ["MatchValue(<constant>)"],
    "<MatchSequence>": ["MatchSequence(<pattern_list>)"],
    "<MatchMapping>": [
        "MatchMapping(<expr_list>,<expr_list>,<optional_identifier>)",
    ],
    "<MatchClass>": [
        "MatchClass(<expr>,<pattern_list>,<identifier_list>,<pattern_list>)"
    ],
    "<MatchStar>": [
        "MatchStar(<optional_identifier>)",
    ],
    "<MatchAs>": [
        "MatchAs(<optional_pattern>,<optional_identifier>)",
    ],
    "<MatchOr>": ["MatchOr(<pattern_list>)"],
    "<type_ignore>": ["<TypeIgnore>"],
    "<TypeIgnore>": ["TypeIgnore(<int>,<string>)"],
    # Basics
    "<int>": [
        "<digits>",
        "-<digits>",
    ],
    "<digits>": [
        "<zeros>",
        "<non_zero_digit>",
        "<non_zero_digit><all_digits>",
    ],
    "<zeros>": [
        "0",
        "0<zeros>",
    ],
    "<all_digits>": [
        "<digit>",
        "<digit><all_digits>",
    ],
    "<digit>": [
        "0",
        "<non_zero_digit>",
    ],
    "<non_zero_digit>": ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
    "<identifier>": ["<id_start><ids>"],
    "<id_start>": srange(string.ascii_letters + "_"),
    "<ids>": ["", "<id><ids>"],
    "<id>": srange(string.ascii_letters + string.digits + "_"),
    "<constant>": [
        "<int>",
        "<string>",
    ],
    "<string>": [
        '"<chars>"',
        "'<chars>'",
    ],
    "<chars>": ["", "<chars><char>"],
    "<char>": (
        srange(string.digits + string.ascii_letters + string.punctuation)
        + [" ", "\\t", "\\n", "\\r", "\\v", "\\f"]
    ),
}

assert is_valid_grammar(GRAMMAR)

GENERATIVE_GRAMMAR: Grammar = dict(GRAMMAR)

GENERATIVE_GRAMMAR["<mod>"] = ["<Module>"]
del GENERATIVE_GRAMMAR["<Interactive>"]
del GENERATIVE_GRAMMAR["<Expression>"]
del GENERATIVE_GRAMMAR["<FunctionType>"]
del GENERATIVE_GRAMMAR["<Yield>"]
del GENERATIVE_GRAMMAR["<Match>"]
del GENERATIVE_GRAMMAR["<AugAssign>"]
del GENERATIVE_GRAMMAR["<YieldFrom>"]
del GENERATIVE_GRAMMAR["<GeneratorExp>"]
del GENERATIVE_GRAMMAR["<ListComp>"]
del GENERATIVE_GRAMMAR["<Try>"]
del GENERATIVE_GRAMMAR["<DictComp>"]
del GENERATIVE_GRAMMAR["<AnnAssign>"]
del GENERATIVE_GRAMMAR["<Break>"]
del GENERATIVE_GRAMMAR["<With>"]
del GENERATIVE_GRAMMAR["<Await>"]
del GENERATIVE_GRAMMAR["<Global>"]
del GENERATIVE_GRAMMAR["<Lambda>"]
del GENERATIVE_GRAMMAR["<ClassDef>"]
del GENERATIVE_GRAMMAR["<Assert>"]
del GENERATIVE_GRAMMAR["<AsyncWith>"]
del GENERATIVE_GRAMMAR["<Starred>"]
# del generative_grammar['<TryStar>']
del GENERATIVE_GRAMMAR["<Raise>"]
del GENERATIVE_GRAMMAR["<JoinedStr>"]
del GENERATIVE_GRAMMAR["<Dict>"]
del GENERATIVE_GRAMMAR["<NamedExpr>"]
del GENERATIVE_GRAMMAR["<Delete>"]
del GENERATIVE_GRAMMAR["<AsyncFor>"]
del GENERATIVE_GRAMMAR["<FormattedValue>"]
del GENERATIVE_GRAMMAR["<excepthandler_list>"]
del GENERATIVE_GRAMMAR["<match_case_list>"]
del GENERATIVE_GRAMMAR["<Set>"]
del GENERATIVE_GRAMMAR["<Continue>"]
del GENERATIVE_GRAMMAR["<Nonlocal>"]
del GENERATIVE_GRAMMAR["<withitem_list>"]
del GENERATIVE_GRAMMAR["<While>"]
del GENERATIVE_GRAMMAR["<AsyncFunctionDef>"]
del GENERATIVE_GRAMMAR["<SetComp>"]
del GENERATIVE_GRAMMAR["<identifier_list>"]
del GENERATIVE_GRAMMAR["<MatchSequence>"]
del GENERATIVE_GRAMMAR["<MatchStar>"]
del GENERATIVE_GRAMMAR["<ExceptHandler>"]
del GENERATIVE_GRAMMAR["<pattern>"]
del GENERATIVE_GRAMMAR["<identifiers>"]
del GENERATIVE_GRAMMAR["<match_cases>"]
del GENERATIVE_GRAMMAR["<MatchSingleton>"]
del GENERATIVE_GRAMMAR["<MatchValue>"]
del GENERATIVE_GRAMMAR["<comprehension_list>"]
del GENERATIVE_GRAMMAR["<match_case>"]
del GENERATIVE_GRAMMAR["<MatchMapping>"]
del GENERATIVE_GRAMMAR["<MatchOr>"]
del GENERATIVE_GRAMMAR["<MatchClass>"]
del GENERATIVE_GRAMMAR["<MatchAs>"]
del GENERATIVE_GRAMMAR["<pattern_list>"]
del GENERATIVE_GRAMMAR["<comprehension>"]
del GENERATIVE_GRAMMAR["<excepthandler>"]
del GENERATIVE_GRAMMAR["<withitem>"]
del GENERATIVE_GRAMMAR["<patterns>"]
del GENERATIVE_GRAMMAR["<withitems>"]
del GENERATIVE_GRAMMAR["<excepthandlers>"]
del GENERATIVE_GRAMMAR["<comprehensions>"]
del GENERATIVE_GRAMMAR["<optional_pattern>"]
GENERATIVE_GRAMMAR["<stmt>"] = [
    "<FunctionDef>",
    "<Return>",
    "<Assign>",
    # '<For>',
    "<If>",
    "<Import>",
    "<ImportFrom>",
    "<Expr>",
    "<Pass>",
]
GENERATIVE_GRAMMAR["<expr>"] = [
    "<BoolOp>",
    "<BinOp>",
    "<UnaryOp>",
    # '<IfExp>',
    "<Compare>",
    "<Call>",
    "<Constant>",
    "<Attribute>",
    # '<Subscript>',
    "<Name>",
    # '<List>',
    "<Tuple>",
]
del GENERATIVE_GRAMMAR["<For>"]
del GENERATIVE_GRAMMAR["<IfExp>"]
del GENERATIVE_GRAMMAR["<Subscript>"]
del GENERATIVE_GRAMMAR["<List>"]
del GENERATIVE_GRAMMAR["<Slice>"]

assert is_valid_grammar(GENERATIVE_GRAMMAR)

GENERATOR = PythonGenerator()

grammar pysnooper_2;

start : options ;

options :  | option_list ;

option_list : option | option_list '\n' option ;

option : output | variables | depth | prefix | watch | custom_repr | OVERWRITE | THREAD_INFO ;

output : '-o' | '-o' path ;

variables : '-v' variable_list ;

depth : '-d' int ;

prefix : '-p' str ;

watch : '-w' variable_list ;

custom_repr : '-c' predicate_list ;

OVERWRITE : '-O' ;

THREAD_INFO : '-T' ;

path : location | location '.' str ;

location : str | path '/' str ;

variable_list : variable | variable_list ',' variable ;

variable : name | variable '.' name ;

name : LETTER chars ;

chars :  | chars char ;

LETTER : 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k' | 'l' | 'm' | 'n' | 'o' | 'p' | 'q' | 'r' | 's' | 't' | 'u' | 'v' | 'w' | 'x' | 'y' | 'z' | 'A' | 'B' | 'C' | 'D' | 'E' | 'F' | 'G' | 'H' | 'I' | 'J' | 'K' | 'L' | 'M' | 'N' | 'O' | 'P' | 'Q' | 'R' | 'S' | 'T' | 'U' | 'V' | 'W' | 'X' | 'Y' | 'Z' ;

DIGIT : '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' ;

char : LETTER | DIGIT | '_' ;

int : NONZERO digits | '0' ;

digits :  | digits DIGIT ;

NONZERO : '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' ;

str : char chars ;

predicate_list : predicate | predicate_list ',' predicate ;

predicate : P_FUNCTION '=' T_FUNCTION ;

P_FUNCTION : 'int' | 'str' | 'float' | 'bool' ;

T_FUNCTION : 'repr' | 'str' | 'int' ;
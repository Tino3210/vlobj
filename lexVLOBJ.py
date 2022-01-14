'''
lexVLOBJ.py
Authors : Izzo Valentino, Loïc Frossard
Python version : 3.9.2
'''
import sys
import ply.lex as lex

reserved_words = (
    'xD',
    'xS',
    'else',
    'Square',
    'Pyramid',
    'Color'
)

tokens = (
    'WHILE',
    'IF',
    'NUMBER',
    'ADD_OP',
    'MUL_OP',
    'PAR_START',
    'PAR_END',
    'IDENTIFIER',
    'EQUALS',
    'ACOL_START',
    'ACOL_END',
    'COMMA',
    'CONDITION',
    'DOTCOMMA',
    'UNDERSCORE',
    'APO'
) + tuple(map(lambda s: s.upper(), reserved_words))

t_ADD_OP = r'(\+)|(-)'
t_MUL_OP = r'(/)|(\*)'
t_PAR_START = r'\('
t_PAR_END = r'\)'
t_EQUALS = r'\=\)'
t_ACOL_START = r'\:\('
t_ACOL_END = r'\):'
t_COMMA = r'\,'
t_APO = r'\''
t_CONDITION = r'(>)|(<)|(\=\=)'
t_DOTCOMMA = r';'
t_UNDERSCORE = r'\_'

t_ignore = '\t '


def t_WHILE(t):
    r'\^\^'
    return t


def t_IF(t):
    r':\/'
    return t


def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t


def t_IDENTIFIER(t):
    r'[a-zA-Z]\w*'
    if t.value in reserved_words:
        t.type = t.value.upper()
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegalcharacter'%s ' " % t.value[0])
    t.lexer.skip(1)


lex.lex()

if __name__ == "__main__":
    prog = open(sys.argv[1]).read()

    lex.input(prog)

    while 1:
        tok = lex.token()
        if not tok:
            break
        print("line %d : %s (%s)" % (tok.lineno, tok.type, tok.value))

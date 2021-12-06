import sys
import ply.yacc as yacc
import AST
from lex import tokens
import os

operations = {
    '+': lambda x, y: x+y,
    '-': lambda x, y: x-y,
    '*': lambda x, y: x*y,
    '/': lambda x, y: x/y,
}

vars = {}


def p_expression_op(p):
    '''expression : expression ADD_OP expression 
                    | expression MUL_OP expression'''
    p[0] = AST.OpNode(p[2], [p[1], p[3]])


def p_expression_uminus(p):
    'expression : ADD_OP expression %prec UMINUS'
    p[0] = AST.OpNode(p[1], [p[2]])


def p_expression_num(p):
    '''expression : NUMBER'''
    p[0] = AST.TokenNode(p[1])


def p_expression_IDENTIFIER(p):
    '''expression : IDENTIFIER'''
    try:
        p[0] = AST.TokenNode(p[1])
    except LookupError:
        print(f"Undefined name {p[1]!r}")
        p[0] = AST.TokenNode(0)


def p_assignation(p):
    'assignation : IDENTIFIER EQUALS expression'
    p[0] = AST.AssignNode([AST.TokenNode(p[1]), p[3]])


def p_error(p):
    print("Syntax errorinline %d" % p.lineno)
    yacc.errok()


def parse(program):
    return yacc.parse(program)


yacc.yacc(outputdir='generated')


if __name__ == "__main__":
    prog = open(sys.argv[1]).read()
    result = yacc.parse(prog)
    print(result)

    graph = result.makegraphicaltree()
    name = os.path.splitext(sys.argv[1])[0]+'-ast.pdf'
    graph.write_pdf(name)
    print("wrote ast to", name)

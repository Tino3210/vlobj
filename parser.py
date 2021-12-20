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
precedence = (
    ('left', 'ADD_OP'),
    ('left', 'MUL_OP'),
    ('right', 'UMINUS'),
)


vars = {}


def p_programme_statement(p):
    'programme : statement'
    #p[0] = p[1]
    p[0] = AST.ProgramNode(p[1])

def p_programme_recursive(p):
    '''programme : statement DOTCOMMA programme'''
    #p[0] = p[3]
    p[0] = AST.ProgramNode([p[1]] + p[3].children)


def p_statement(p):
    '''statement : assignation
                    | structure
                    | square
                    | pyramid
                    | color'''
    try:
        p[0] = AST.PrintNode(p[2])
    except:
        p[0] = p[1]

def p_assignation(p):
    'assignation : IDENTIFIER EQUALS expression'    
    p[0] = AST.AssignNode([AST.TokenNode(p[1]), p[3]])

def p_square(p):
    '''square : SQUARE PAR_START expression COMMA expression COMMA expression COMMA expression PAR_END'''
    p[0] = AST.SquareNode([AST.TokenNode(p[3]),AST.TokenNode(p[5]),AST.TokenNode(p[7]),AST.TokenNode(p[9])])

def p_pyramid(p):
    '''pyramid : PYRAMID PAR_START expression COMMA expression COMMA expression COMMA expression PAR_END
                | PYRAMID PAR_START expression COMMA expression COMMA expression COMMA expression COMMA expression PAR_END'''
    try: 
        p[0] = AST.PyramidNode([AST.TokenNode(p[3]), AST.TokenNode(p[5]), AST.TokenNode(p[7]), AST.TokenNode(p[9]), AST.TokenNode(p[11])])
    except: 
        p[0] = AST.PyramidNode([AST.TokenNode(p[3]), AST.TokenNode(p[5]), AST.TokenNode(p[7]), AST.TokenNode(p[9])])

def p_color(p):
    '''color : COLOR PAR_START expression COMMA expression COMMA expression COMMA expression PAR_END'''
    p[0] = AST.ColorNode([AST.TokenNode(p[3]),AST.TokenNode(p[5]),AST.TokenNode(p[7]),AST.TokenNode(p[9])])

def p_while(p):
    '''structure : WHILE expression ACOL_START programme ACOL_END'''
    p[0] = AST.WhileNode([p[2], p[4]])

def p_expression_op(p):
    '''expression : expression ADD_OP expression 
                    | expression MUL_OP expression'''
    p[0] = AST.OpNode(p[2], [p[1], p[3]])

def p_expression_uminus(p):
    'expression : ADD_OP expression %prec UMINUS'
    p[0] = AST.OpNode(p[1], [p[2]])

def p_expression_num(p):
    '''expression : NUMBER
                    | STRING'''
    p[0] = AST.TokenNode(p[1])


def p_expression_IDENTIFIER(p):
    '''expression : IDENTIFIER'''
    try:
        p[0] = AST.TokenNode(p[1])
    except LookupError:
        print(f"Undefined name {p[1]!r}")
        p[0] = AST.TokenNode(0)

def p_error(p):
    print("Syntax errorinline %d" % p.lineno)
    yacc.errok()

def parse(program):
    return yacc.parse(program)


yacc.yacc(outputdir='generated')


if __name__ == "__main__":
    prog = open(sys.argv[1]).read()
    result = yacc.parse(prog,debug=1)
    print(result)

    graph = result.makegraphicaltree()
    name = os.path.splitext(sys.argv[1])[0]+'-ast.pdf'
    graph.write_pdf(name)
    print("wrote ast to", name)

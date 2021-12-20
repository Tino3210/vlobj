import AST
from AST import addToClass
from functools import reduce
from parserVLOBJ import parse
import sys
import os

operations = {
    '+': 'ADD',
    '-': 'SUB',
    '*': 'MUL',
    '/': 'DIV'
}

stack = []
vars = {}


@addToClass(AST.ProgramNode)
def compile(self):
    byte = ""
    for c in self.children:
        byte += c.compile()
    return byte


@addToClass(AST.TokenNode)
def compile(self):
    if isinstance(self.tok, str):
        try:
            return "PUSHV " + str(self.tok) + "\n"
        except KeyError:
            print("*** Error: variable %s undefined!" % self.tok)
    return "PUSHC " + str(self.tok) + "\n"


@addToClass(AST.OpNode)
def compile(self):
    byte = ''
    if len(self.children) == 1:
        byte += self.children[0].compile()
        byte += 'USUB\n'
    else:
        for c in self.children:
            byte += c.compile()
        byte += operations[self.op] + '\n'
    return byte


@addToClass(AST.AssignNode)
def compile(self):
    byte = str(self.children[1].compile())
    byte += "SET " + self.children[0].tok + "\n"
    return byte


nbWhile = 0


def incementeNumber():
    global nbWhile
    nbWhile += 1
    return nbWhile


@addToClass(AST.WhileNode)
def compile(self):
    nbWhile = incementeNumber()
    byte = 'JMP cond' + str(nbWhile) + '\n'
    byte += 'body' + str(nbWhile) + ': '
    byte += self.children[1].compile()
    byte += 'cond' + str(nbWhile) + ': '
    byte += self.children[0].compile()
    byte += 'JINZ body' + str(nbWhile) + '\n'
    return byte


@addToClass(AST.PrintNode)
def compile(self):
    obj = self.children[0].compile()
    obj += "PRINT" + "\n"
    return (obj, mtl)


if __name__ == "__main__":
    prog = open(sys.argv[1]).read()
    ast = parse(prog)
    compiled = ast.compile()
    name = os.path.splitext(sys.argv[1])[0] + '.obj'
    outfile = open(name, 'w')
    outfile.write(compiled[0])
    outfile.close()
    name = os.path.splitext("./output/" + sys.argv[1])[0] + '.mtl'
    outfile = open(name, 'w')
    outfile.write(compiled[1])
    outfile.close()
    print("Wrote output to", name)

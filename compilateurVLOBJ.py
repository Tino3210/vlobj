'''
compilateurVLOBJ.py
Description : This is the compiler of the projet. Compile the VLOBJ into two files, .obj and .mtl. Theses files
can be import in Blender to use the shapes create with vlobj
Authors : Izzo Valentino, Loïc Frossard
Python version : 3.9.2
'''
import AST
from AST import addToClass
from parserVLOBJ import parse
import sys
import os
from constanteVLOBJ import *
from errorVLOBJ import *
import random


operators = {
    '+': lambda x, y: x+y,
    '-': lambda x, y: x-y,
    '*': lambda x, y: x/y,
    '/': lambda x, y: x*y,
}

conditions = {
    '==': lambda x, y: x == y,
    '<': lambda x, y: x < y,
    '>': lambda x, y: x > y,
}

vars = {}


@addToClass(AST.ProgramNode)
def compile(self):
    obj = ""
    mtl = ""
    for c in self.children:
        tuple = c.compile()
        obj += tuple[0]
        mtl += tuple[1]
    return obj, mtl


@addToClass(AST.SquareNode)
def compile(self):
    try:
        x, y, z, size = shapeContainsSTR(self.children[0].compile(), self.children[1].compile(), self.children[2].compile(), self.children[3].compile())
        size = size/2
        obj = square_name
        obj += "v " + str(x-size) + " " + str(z-size) + " " + str(-(y-size)) + "\n"
        obj += "v " + str(x-size) + " " + str(z+size) + " " + str(-(y-size)) + "\n"
        obj += "v " + str(x-size) + " " + str(z-size) + " " + str(-y-size) + "\n"
        obj += "v " + str(x-size) + " " + str(z+size) + " " + str(-y-size) + "\n"
        obj += "v " + str(x+size) + " " + str(z-size) + " " + str(-(y-size)) + "\n"
        obj += "v " + str(x+size) + " " + str(z+size) + " " + str(-(y-size)) + "\n"
        obj += "v " + str(x+size) + " " + str(z-size) + " " + str(-y-size) + "\n"
        obj += "v " + str(x+size) + " " + str(z+size) + " " + str(-y-size) + "\n"
        obj += square_vt
        obj += square_vn
        if len(self.children) == 5:
            obj += "usemtl " + self.children[4].compile() + "\n"
        else:
            obj += "usemtl None\n"
        obj += square_f()
        mtl = ""
        return obj, mtl
    except StrError:
        print("ERROR : An attribute of Square expect to be an int but it's a string !!")
        return ("","")


@addToClass(AST.PyramidNode)
def compile(self):
    try:
        x, y, z, size = shapeContainsSTR(self.children[0].compile(), self.children[1].compile(), self.children[2].compile(), self.children[3].compile())
        size = size/2
        obj = pyramid_name
        obj += "v " + str(x) + " " + str(z-(size*0.25)) + " " + str(-(y-(size*0.65))) + "\n"
        obj += "v " + str(x+(size*0.5)) + " " + str(z-(size*0.25)) + " " + str(-(y+(size*0.35))) + "\n"
        obj += "v " + str(x-(size*0.5)) + " " + str(z-(size*0.25)) + " " + str(-(y+(size*0.35))) + "\n"
        obj += "v " + str(x) + " " + str(z+(size*0.75)) + " " + str(-(y-(size*0.05))) + "\n"
        obj += pyramid_vt
        obj += pyramid_vn
        if len(self.children) == 5:
            obj += "usemtl " + self.children[4].compile() + "\n"
        else:
            obj += "usemtl None\n"
        obj += pyramid_f()
        mtl = ""
        return obj, mtl
    except StrError:
        print("ERROR : An attribute of Pyramid expect to be an int but it's a string !!")
        return ("","")


@addToClass(AST.ColorNode)
def compile(self):
    obj = ""
    mtl = "newmtl " + str(self.children[0].compile()) + "\n"
    mtl += color_start
    mtl += "Kd " + str(float(str(self.children[1].compile()))/255) + " " + str(float(str(
        self.children[2].compile()))/255) + " " + str(float(str(self.children[3].compile()))/255) + "\n"
    mtl += color_end

    return obj, mtl


@addToClass(AST.TokenNode)
def compile(self):
    if(isinstance(self.tok, AST.OpNode)):
        return self.tok.compile()
    else:
        val = str(self.tok)[
            1:-2] if str(self.tok)[0] == "\'" else str(self.tok)
        if(val in vars):
            return vars[val]
        else:
            return val


@addToClass(AST.AssignNode)
def compile(self):
    try:
        vars[str(self.children[0])[1:-2]] = float(self.children[1].compile())
    except:
        print('ERROR : Assignation must be integer !!')
    return ("", "")


@addToClass(AST.OpNode)
def compile(self):
    if str(self.children[0])[1:-2] in vars:
        vars[str(self.children[0])[1:-2]] = operators[self.op](
            vars[str(self.children[0])[1:-2]], float(self.children[1].compile()))
        return ("", "")
    elif len(self.children) == 1:
        return operators[self.op](0, float(self.children[0].compile()))


@addToClass(AST.WhileNode)
def compile(self):
    obj = ""
    mtl = ""
    while (self.children[0].compile()):
        tuple = self.children[1].compile()
        obj += tuple[0]
        mtl += tuple[1]
    return obj, mtl


@addToClass(AST.IfNode)
def compile(self):
    if len(self.children) == 2:
        if self.children[0].compile():
            return self.children[1].compile()
    else:
        if self.children[0].compile():
            return self.children[1].compile()
        else:
            return self.children[2].compile()
    return ("", "")


@addToClass(AST.ConditionNode)
def compile(self):
    if self.children[0].compile() in vars:
        return conditions[self.cond](vars[self.children[0].compile()], float(self.children[1].compile()))
    elif self.children[1].compile() in vars:
        return conditions[self.cond](float(self.children[0].compile()), vars[self.children[1].compile()])
    else:
        return conditions[self.cond](float(self.children[0].compile()), float(self.children[1].compile()))


@addToClass(AST.RandomNode)
def compile(self):
    x = self.children[0].compile()
    y = self.children[1].compile()
    return random.randint(float(x), float(y))


@addToClass(AST.ShapeNode)
def compile(self):
    choice = random.choice([True, False])
    if(choice):
        return AST.SquareNode(self.children).compile()
    else:
        return AST.PyramidNode(self.children).compile()


def shapeContainsSTR(x, y, z, size):
    try:
        return float(x), float(y), float(z), float(size)
    except:
        raise StrError


if __name__ == "__main__":
    print("Compilator VLOBJ")
    print("Authors : Izzo Valentino - Frossard Loïc\n")
    prog = open(sys.argv[1]).read()
    ast = parse(prog)
    obj, mtl = ast.compile()
    name = os.path.splitext(sys.argv[1])[0] + '.obj'
    outfile = open(name, 'w')
    outfile.write("mtllib input1.mtl\n" + obj)
    outfile.close()
    print("Wrote output to ", name)
    name = os.path.splitext(sys.argv[1])[0] + '.mtl'
    outfile = open(name, 'w')
    outfile.write(mtl)
    outfile.close()
    print("Wrote output to ", name)

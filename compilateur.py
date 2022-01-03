import AST
from AST import addToClass
from functools import reduce
from parserVLOBJ import parse
import sys
import os
from constanteVLOBJ import *
import random


operators = {
    '+': lambda x, y: x+y,
    '-': lambda x, y: x-y,
    '*': lambda x, y: x/y,
    '/': lambda x, y: x*y,
}

conditions = {
    '==': lambda x, y: x==y,
    '<': lambda x, y:x < y,
    '>': lambda x, y:x > y,
}

stack = []
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
    x = float(self.children[0].compile())
    y = float(self.children[1].compile())
    z = float(self.children[2].compile())
    size = float(self.children[3].compile())/2
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
    if len(self.children) == 5 :
        obj += "usemtl " + self.children[4].compile() + "\n"
    else :
        obj += "usemtl None\n"
    obj += square_f
    mtl = "Color"
    return obj,mtl

@addToClass(AST.PyramidNode)
def compile(self):
    x = float(self.children[0].compile())
    y = float(self.children[1].compile())
    z = float(self.children[2].compile())
    size = float(self.children[3].compile())/2
    obj = pyramid_name
    obj += "v " + str(x) + " " + str(z-(size*0.25)) + " " + str(y-(size*0.65)) + "\n"
    obj += "v " + str(x+(size*0.5)) + " " + str(z-(size*0.25)) + " " + str(y+(size*0.35)) + "\n"
    obj += "v " + str(x-(size*0.5)) + " " + str(z-(size*0.25)) + " " + str(y+(size*0.35)) + "\n"
    obj += "v " + str(x) + " " + str(z+(size*0.75)) + " " + str(y-(size*0.05)) + "\n"   
    obj += pyramid_vt
    obj += pyramid_vn
    if len(self.children) == 5 :
        obj += "usemtl " + self.children[4].compile() + "\n"
    else :
        obj += "usemtl None\n"
    obj += pyramid_f
    mtl = ""
    return obj,mtl

@addToClass(AST.ColorNode)
def compile(self):
    obj = ""
    mtl = "newmtl " + str(self.children[0].compile()) + "\n"
    mtl += color_start
    mtl += "Kd " + str(float(str(self.children[1].compile()))/255) + " " + str(float(str(self.children[2].compile()))/255) + " " + str(float(str(self.children[3].compile()))/255) + "\n"
    mtl += color_end    

    return obj,mtl

@addToClass(AST.TokenNode)
def compile(self):
    if(isinstance(self.tok,AST.OpNode)):
        return self.tok.compile()
    else :
        if(str(self.tok)[0] == "\""):
            return str(self.tok)[2:-3]
        else:        
            return str(self.tok)

@addToClass(AST.AssignNode)
def compile(self):
    vars[self.children[0].compile()] = float(self.children[1].compile())
    return ("","")

@addToClass(AST.OpNode)
def compile(self):
    if self.children[0].compile() in vars:
        vars[self.children[0].compile()] = operators[self.op](vars[self.children[0].compile()],float(self.children[1].compile()))
        return ("","")
    elif len(self.children) == 1:
        return float(str(self.children[0].compile()))
        
            

@addToClass(AST.WhileNode)
def compile(self):
    obj = ""
    mtl = ""
    while (self.children[0].compile()):
        tuple = self.children[1].compile()
        obj += tuple[0]
        mtl += tuple[1]
    return obj,mtl

@addToClass(AST.IfNode)
def compile(self):
    if self.children[0].compile():
        return self.children[1].compile()

@addToClass(AST.ConditionNode)
def compile(self):
    if self.children[0].compile() in vars:
        return conditions[self.cond](vars[self.children[0].compile()],float(self.children[1].compile()))
    elif self.children[1].compile() in vars:
        return conditions[self.cond](float(self.children[0].compile()),vars[self.children[1].compile()])
    else :
        return conditions[self.cond](float(self.children[0].compile()),float(self.children[1].compile()))

@addToClass(AST.RandomNode)
def compile(self):
    return random.randint(self.children[0].compile(),self.children[1].compile())

@addToClass(AST.ShapeNode)
def compile(self):
    choice = random.choice([True,False])
    if(choice):
        return AST.SquareNode([1,1,1,1]).compile()
    else:
        return AST.PyramidNode([1,1,1,1]).compile()

if __name__ == "__main__":
    prog = open(sys.argv[1]).read()
    ast = parse(prog)
    obj, mtl = ast.compile()
    name = os.path.splitext(sys.argv[1])[0] + '.obj'
    outfile = open(name, 'w')
    outfile.write("mtllib input1.mtl\n" + obj)
    outfile.close()
    name = os.path.splitext(sys.argv[1])[0] + '.mtl'
    outfile = open(name, 'w')
    outfile.write(mtl)
    outfile.close()
    print("Wrote output to", name)

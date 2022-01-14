'''
constanteVLOBJ.py
Authors : Izzo Valentino, Loïc Frossard
Python version : 3.9.2
'''
# VARIABLE GLOBAL

v = 1  # Index vertices
vt = 1  # Index texture
vn = 1  # Index normal


def incrementeSquare():
    '''
    Increment after creation of a square
    '''
    global v
    global vt
    global vn
    v += 8  # 8 vertice per square
    vt += 14  # 14 texture per square
    vn += 6  # 6 normal per square (Face)
    return v, vt, vn


def incrementePiramid():
    ''''
    Increment after creation of a square
    '''
    global v
    global vt
    global vn
    v += 4  # 4 vertice per square
    vt += 7  # 7 texture per square
    vn += 4  # 4 normal per square (Face)
    return v, vt, vn

# CONSTANTE - Use in the .obj file


square_name = 'o Cube\n'  # Name of the shape

# Constante for texture
# We don't use any texture so this will not change the output
square_vt = """vt 0.625000 0.500000
vt 0.875000 0.500000
vt 0.875000 0.750000
vt 0.625000 0.750000
vt 0.375000 0.750000
vt 0.625000 1.000000
vt 0.375000 1.000000
vt 0.375000 0.000000
vt 0.625000 0.000000
vt 0.625000 0.250000
vt 0.375000 0.250000
vt 0.125000 0.500000
vt 0.375000 0.500000
vt 0.125000 0.750000
"""

# Constante for the normals
# The normal for each cube is the same
square_vn = """vn 0.0000 1.0000 0.0000
vn 0.0000 0.0000 1.0000
vn -1.0000 0.0000 0.0000
vn 0.0000 -1.0000 0.0000
vn 1.0000 0.0000 0.0000
vn 0.0000 0.0000 -1.0000
"""


def square_f():
    '''
    Return the text of the Square's face with the right index in the right spot
    '''
    square_f = "s off\n"
    square_f += "f {}/{}/{} {}/{}/{} {}/{}/{} {}/{}/{}\n".format(
        v, vt, vn, v+1, vt+1, vn, v+3, vt+2, vn, v+2, vt+3, vn)
    square_f += "f {}/{}/{} {}/{}/{} {}/{}/{} {}/{}/{}\n".format(
        v+2, vt+3, vn+1, v+3, vt+2, vn+1, v+7, vt+4, vn+1, v+6, vt+5, vn+1)
    square_f += "f {}/{}/{} {}/{}/{} {}/{}/{} {}/{}/{}\n".format(
        v+6, vt+5, vn+2, v+7, vt+4, vn+2, v+5, vt+6, vn+2, v+4, vt+7, vn+2)
    square_f += "f {}/{}/{} {}/{}/{} {}/{}/{} {}/{}/{}\n".format(
        v+4, vt+7, vn+3, v+5, vt+6, vn+3, v+1, vt+8, vn+3, v, vt+9, vn+3)
    square_f += "f {}/{}/{} {}/{}/{} {}/{}/{} {}/{}/{}\n".format(
        v+2, vt+10, vn+4, v+6, vt+5, vn+4, v+4, vt+7, vn+4, v, vt+11, vn+4)
    square_f += "f {}/{}/{} {}/{}/{} {}/{}/{} {}/{}/{}\n".format(
        v+7, vt+4, vn+5, v+3, vt+12, vn+5, v+1, vt+13, vn+5, v+5, vt+6, vn+5)
    incrementeSquare()
    return square_f


pyramid_name = 'o Pyramid\n'  # Name of the shape

# Constante for texture
# We don't use any texture so this will not change the output
pyramid_vt = """vt 0.250000 0.490000
vt 0.250000 0.250000
vt 0.457846 0.130000
vt 0.750000 0.490000
vt 0.957846 0.130000
vt 0.542154 0.130000
vt 0.042154 0.130000
"""

# Constante for the normals
# The normal for each pyramid is the same
pyramid_vn = """vn 0.8639 0.2592 -0.4319
vn 0.0000 -1.0000 0.0000
vn -0.0000 0.3714 0.9285
vn -0.8639 0.2592 -0.4319
"""


def pyramid_f():
    '''
    Return the text of the Pyramid's face with the right index in the right spot
    '''
    pyramid_f = "s off\n"
    pyramid_f += "f {}/{}/{} {}/{}/{} {}/{}/{}\n".format(
        v, vt, vn, v+3, vt+1, vn, v+1, vt+2, vn)
    pyramid_f += "f {}/{}/{} {}/{}/{} {}/{}/{}\n".format(
        v, vt+3, vn+1, v+1, vt+4, vn+1, v+2, vt+5, vn+1)
    pyramid_f += "f {}/{}/{} {}/{}/{} {}/{}/{}\n".format(
        v+1, vt+2, vn+2, v+3, vt+1, vn+2, v+2, vt+6, vn+2)
    pyramid_f += "f {}/{}/{} {}/{}/{} {}/{}/{}\n".format(
        v+2, vt+6, vn+3, v+3, vt+1, vn+3, v, vt, vn+3)
    incrementePiramid()
    return pyramid_f

# Constante for the colors in .mtl
# Specular highlights
# Ka : ambiant color
color_start = """Ns 225.000000
Ka 1.000000 1.000000 1.000000
"""

# Ks : specular color
# Ni : optical dansity
# d : disolve
# illum : Illumination model
color_end = """Ks 0.500000 0.500000 0.500000
Ke 0.000000 0.000000 0.000000
Ni 1.450000
d 1.000000
illum 2
"""

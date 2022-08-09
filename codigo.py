#!/bin/python3

codigo = "(YO) (RB) (RO) (GB) (RY) (YO) (RY) (RB) (GY) (GY) (YB) (YB) (YO) (YO) (YB) Y R (RY) R Y O"

def substituir(codigo):
    codigo = codigo.replace("R","L1 ")
    codigo = codigo.replace("Y","R1 ")
    codigo = codigo.replace("O","X ")
    codigo = codigo.replace("G","L2 ")
    codigo = codigo.replace("B","R2 ")
    print(codigo)

substituir(codigo)

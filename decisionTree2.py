import math

class dataset:
    salario: bool #alto ou baixo
    localizacao: bool #perto ou longe
    funcao: bool #interessante ou desinteressante
    decisao: bool #sim ou não

dt = []
dt.append(True, True, False, True)
dt.append(False, False, True, False)
dt.append(True, True, False, False)
dt.append(False, False, False, True)
dt.append(True, True, True, True)
dt.append(False, False, False, False)

def peso(label: str, column: list):
    countLabel = 0
    for x in column:
        if(x == label):
            countLabel+=1

    return countLabel/column.count()

def entropia(peso:int):
    entrop = 0
    for x in peso:
        entrop += x* math.log2(x)

    return entrop

def ganhoInfo(columPai: list, columnFilho:list):
    return entropia(columPai) - peso("label",columnFilho) * entropia(columnFilho)
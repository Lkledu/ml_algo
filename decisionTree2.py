import math

class dataset():
    def __init__(self, salario:str, localizacao:str, funcao:str, decisao:str):
        self.salario = salario  #alto ou baixo
        self.localizacao = localizacao  #perto ou longe
        self.funcao = funcao  #interessante ou desinteressante
        self.decisao = decisao  #sim ou não

dt = []
dt.append(dataset('alto', 'perto', 'desinteressante', 'sim'))
dt.append(dataset('baixo', 'longe', 'interessante', 'não'))
dt.append(dataset('alto', 'perto', 'desinteressante', 'não'))
dt.append(dataset('baixo', 'longe', 'desinteressante', 'sim'))
dt.append(dataset('alto', 'perto', 'interessante', 'sim'))
dt.append(dataset('baixo', 'longe', 'desinteressante', 'não'))

def organize(attrib:str, objArray: []):
    listOrganized = []
    if hasattr(objArray[0], attrib):
        for x in objArray:
            listOrganized.append(getattr(x, attrib))
    
    return listOrganized

def peso(label: str, column: list):
    countLabel = 0
    for x in column:
        if(x == label):
            countLabel+=1

    return countLabel/len(column)

def entropia(peso:int):
    entrop = -(peso * math.log2(peso))

    return entrop

def ganhoInfo(columPai: list, columnFilho:list):
    return entropia(columPai) - peso("label",columnFilho) * entropia(columnFilho)

target = organize('decisao', dt)

entropiaTarget = entropia(peso('sim', target)) + entropia(peso('não', target))

print(entropiaTarget)
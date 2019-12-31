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
#dt.append(dataset('alto', 'perto', 'interessante', 'sim'))

#retorna lista com apenas um atributo de cada objeto
def organize(attrib:str, objArray: []):
    listOrganized = []
    if hasattr(objArray[0], attrib):
        for x in objArray:
            listOrganized.append(getattr(x, attrib))
    return listOrganized


#retorna lista com labels aplicando distinct
def getLabels(column: [], attr:str):
    labels = []
    count = 0
    if hasattr(column[0], attr):
        labels.append(getattr(column[0], attr))
        for x in column:
            for y in labels:
                if  getattr(x, attr) == y:
                    count +=1
            if count == 0:
                labels.append(getattr(x, attr))
            count = 0
            
    return labels


#calcula peso da coluna
def peso(label: str, labelTarget: str, column: list, attr:str):
    countLabel = 0
    for x in column:
        if(x.decisao == labelTarget) and getattr(x, attr) == label:
            countLabel+=1
    return countLabel/len(column)


#calcula entropia de uma coluna especifica
def entropia(column: [], dt: [], attr:str):
    entrop = 0
    labels = getLabels(dt, attr)
    labelTarget = getLabels(dt, 'decisao')
    for x in labels:
        for y in labelTarget:
            if(peso(str(x), str(y), dt, attr) != 0):
                entrop += -(peso(str(x), str(y) ,dt, attr) * math.log2(peso(str(x), str(y), dt, attr)))
    return entrop


#calcula ganho de info de coluna especifica
def ganhoInfo(entroT: float, entroC: float, dt: [], attr: str):
    gi = 0
    label = getLabels(dt, attr)
    labelTarget = getLabels(dt, 'decisao')
    var = 0
    for x in label:
        for y in labelTarget:
            var += peso(x, y, dt, attr) * entroC
    gi = entroT - var
    return gi

target = organize('decisao', dt)
salarioList = organize('salario', dt)
localizacaoList = organize('localizacao', dt)
funcaoList = organize('funcao', dt)


entropiaTarget = entropia(target, dt, 'decisao')
entropiaSalario = entropia(salarioList, dt, 'salario')
entropiaLocal = entropia(localizacaoList, dt, 'localizacao')
entropiaFuncao = entropia(funcaoList, dt, 'funcao')

giSalario = ganhoInfo(entropiaTarget, entropiaSalario, dt, 'salario')
giLocal = ganhoInfo(entropiaTarget, entropiaLocal, dt, 'localizacao')
giFuncao = ganhoInfo(entropiaTarget, entropiaFuncao, dt, 'funcao')


print(entropiaTarget)
print(giSalario)
print(giLocal)
print(giFuncao)
import math

class dataset():
    def __init__(self, salario:str, localizacao:str, funcao:str, decisao:str):
        self.salario = salario  #alto ou baixo
        self.localizacao = localizacao  #perto ou longe
        self.funcao = funcao  #interessante ou desinteressante
        self.decisao = decisao  #sim ou não

dt = []
dt.append(dataset('alto', 'perto', 'interessante', 'sim'))
dt.append(dataset('baixo', 'longe', 'interessante', 'sim'))
dt.append(dataset('alto', 'perto', 'desinteressante', 'não'))
dt.append(dataset('baixo', 'longe', 'desinteressante', 'não'))
dt.append(dataset('alto', 'perto', 'interessante', 'sim'))
dt.append(dataset('baixo', 'longe', 'desinteressante', 'não'))
dt.append(dataset('alto', 'perto', 'interessante', 'sim'))
dt.append(dataset('alto', 'perto', 'desinteressante', 'não'))

def getLabel(dt:[], attr: str):
    labels = []
    count = 0
    if hasattr(dt[0], attr):
        labels.append(getattr(dt[0], attr))
        for x in dt:
            for y in labels:
                if  getattr(x, attr) == y:
                    count +=1
            if count == 0:
                labels.append(getattr(x, attr))
            count = 0
    return labels

def pesoTarget(dt: []):
    labels = getLabel(dt, 'decisao')
    peso = [0,0]
    for i in range(len(labels)):
        for y in dt:
            if y.decisao == labels[i]:
                peso[i] +=1
        peso[i] = peso[i] / len(dt)

    return peso #retorna variavel com o peso de "sim" e "não" para a coluna decisão

def entropia(peso: []):
    entropia = 0
    for x in peso:
        entropia += -(x* math.log2(x))
    
    return entropia #retorna entropia da coluna decisão

#####################################################################
def encontraRamo(dt:[], column: str):
    labels = []
    count = 0
    if hasattr(dt[0], column):
        labels.append(getattr(dt[0], column))
        for x in dt:
            for y in labels:
                if  getattr(x, column) == y:
                    count +=1
            if count == 0:
                labels.append(getattr(x, column))
            count = 0
            
    return labels

def pesoFilho(dt:[], column: str):
    pesoF = [0,0]
    keys = encontraRamo(dt, column)

    for i in range(len(keys)):
        for x in dt:
            if getattr(x, column) == keys[i]:
                pesoF[i] += 1
        pesoF[i] = pesoF[i] / len(dt)
   
    return pesoF


def ganhoInform(dt:[], filho: str):
    somatoriaPesoFilho = 0
    for x in pesoFilho(dt, filho):
        somatoriaPesoFilho += x

    ganhoInfo = entropia(pesoTarget(dt)) - somatoriaPesoFilho * entropia(pesoFilho(dt, filho))
    return ganhoInfo

print('\n')

print(pesoFilho(dt, 'salario'))
print(pesoFilho(dt, 'localizacao'))
print(pesoFilho(dt, 'funcao'))


print('\n')
print('\n')

print(ganhoInform(dt, 'salario'))
print(ganhoInform(dt, 'localizacao'))
print(ganhoInform(dt, 'funcao'))

print('\n')
print(entropia(pesoTarget(dt)))
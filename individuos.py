import random

def crearIndividuos(pI, dC):
    individuos_list = []
    
    for i in range(pI):
        pc =[randomFun(len(dC[0])), randomFun(len(dC[1])), randomFun(len(dC[2])), randomFun(len(dC[3])), randomFun(len(dC[4])), randomFun(len(dC[5])), randomFun(len(dC[6])), randomFun(len(dC[7]))]
        individuos_list.append(pc)
        #print(pc)

    return individuos_list

def randomFun(rango):
    return random.randint(1, rango)
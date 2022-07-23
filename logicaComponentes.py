
from numpy import true_divide
from individuos import crearIndividuos


def verificarCompatibilidad(individuos, datosComponenetes, precio):
    print("\n\n--------------------------------  Compatibilidad ")
    individuosVerificados = []

    for i in range( len(individuos) ):        

        cpuN = individuos[i][0] -1
        tarN = individuos[i][1] -1        
        ramN = individuos[i][3] -1
 
        cpuV = datosComponenetes[0][ cpuN ]['compatible']
        tarjV = datosComponenetes[1][ tarN ]['compatible']        
        ramV = datosComponenetes[3][ ramN ]['compatible']

        if cpuV != tarjV or ramV != tarjV:
            #print(" > incompatible")
            indi= compatibilizar(datosComponenetes, precio)
            individuosVerificados.append(indi)
        else:
            #print(" > compatible")
            individuosVerificados.append(individuos[i])        

    return individuosVerificados

def compatibilizar(dC, precio):    
    
    verificando = True
    while verificando:
        indi = crearIndividuos(1, dC, precio)[0]               

        cpuN = indi[0] -1
        tarN = indi[1] -1        
        ramN = indi[3] -1
 
        cpuV = dC[0][ cpuN ]['compatible']
        tarjV = dC[1][ tarN ]['compatible']        
        ramV = dC[3][ ramN ]['compatible']

        if cpuV != tarjV or ramV != tarjV:
            verificando = True
        else:
            verificando = False    

    return indi


    
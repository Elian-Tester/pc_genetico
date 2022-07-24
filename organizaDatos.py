from math import comb
import random
from individuos import crearIndividuos, desagruparDatos

from logicaComponentes import verificarCompatibilidad
from logicaGenetico import PODA, combinacion, cruzarLista, limpieza, mutarIndividuos, seleccion, verificarDecendencia

PROCESADORES = 0
TARJETAS = 0
DISIPADOR = 0
RAM = 0
GRAFICA = 0
ALMACENAMIENTO = 0
GABINETE = 0
FUENTE_PODER = 0


def llenarGlobales(datosComponenetes):
    global PROCESADORES
    PROCESADORES = datosComponenetes[0]
    global TARJETAS
    TARJETAS = datosComponenetes[1]    
    global DISIPADOR
    DISIPADOR = datosComponenetes[2]
    global RAM
    RAM = datosComponenetes[3]
    global GRAFICA
    GRAFICA = datosComponenetes[4]
    global ALMACENAMIENTO
    ALMACENAMIENTO = datosComponenetes[5]
    global GABINETE
    GABINETE = datosComponenetes[6]
    global FUENTE_PODER
    FUENTE_PODER = datosComponenetes[7]

def normalizarDatos(pI, PMaxima,datosComponenetes, presupuesto, nuevaGeneracion):
    print("Normalizando... ")
    llenarGlobales(datosComponenetes)    

    pcCompatible = nuevaGeneracion
    if ( len(nuevaGeneracion) == 0 ):
        individuos = crearIndividuos(pI, datosComponenetes, presupuesto)

        pcCompatible =verificarCompatibilidad(individuos, datosComponenetes, presupuesto)

    print("PC compatible: ")
    listaPc = []
    
    contaId = 1
    for pc_ in pcCompatible:        
        listaPc.append( [contaId, pc_] )
        contaId+=1
    
    """ for idCon in listaPc:
        print("> ",idCon) """

    seleccionTcT_list = seleccion( len(pcCompatible) )

    print("\nSeleccion TcT:")
    """ for x in seleccionTcT_list:
        print(x) """

    combinacion_list = combinacion(seleccionTcT_list, listaPc)

    print("\nCombinacion: ")
    """ for combi in combinacion_list:
        print(combi) """

    print("\nLista a cruzar")
    cruzar_list = verificarDecendencia(combinacion_list, 60)
    """ for cruz in cruzar_list[0]:
        print(cruz) """
    
    lista_cruzado = cruzarLista(cruzar_list[0])

    print("\nCruzados lista")
    """ for cruzadoIndi in lista_cruzado:
        print(cruzadoIndi) """
    #cruzaCompleta = cruzar_list[1] + lista_cruzado

    lista_cruzado_individual = desagruparDatos( lista_cruzado )
    lista_cruzado_individual_mutado = mutarIndividuos(lista_cruzado_individual, 15, 10, datosComponenetes)

    noCruzar_list_individual = desagruparDatos( cruzar_list[1] )

    cruzaCompleta = noCruzar_list_individual + lista_cruzado_individual_mutado

    print("\nLista cruzada individual completa: ")
    """ for indiCruzados in cruzaCompleta:
        print(indiCruzados) """

    print("\nLimpieza .... (detalles)")    
    lista_limpia = limpieza(cruzaCompleta, datosComponenetes, presupuesto)

    
    print("Inicia PODA -------------***********-----------")
    return PODA(lista_limpia, datosComponenetes, PMaxima)





def lenVariablesGlobales():
    print("core: ", len(PROCESADORES))
    print("tarjeta : ", len(TARJETAS))
    print("disipador : ", len(DISIPADOR))
    print("ram : ", len(RAM))
    print("grafica : ", len(GRAFICA))
    print("almacenemiento : ", len(ALMACENAMIENTO))
    print("gabinete : ", len(GABINETE))
    print("fuente poder : ", len(FUENTE_PODER))
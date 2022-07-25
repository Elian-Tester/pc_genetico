import random

def seleccion(pI):
    print("\nSeleccion todos con todos")
    seleccion=[]            

    auxDisminuir=2
    for x in range(1,pI):

        for j in range(auxDisminuir, pI+1):
            
            combinacion=[x, j]
            seleccion.append(combinacion)        
            print(combinacion)
        auxDisminuir+=1
        
    return seleccion

def combinacion(seleccion, individuos):
        parejas = []        
        for pareja in seleccion:
            decendencia = ( random.randint(1, 100) ) / 100
            
            parejas.append({
                "id1":individuos[ int(pareja[0])-1 ][1],
                "id2":individuos[ int(pareja[1])-1 ][1],
                "decendencia": decendencia
                })            
            #print(parejas)

        return parejas

def verificarDecendencia(parejas_list, decendencia):
    cruzar = []    
    origin = []
    decendencia = decendencia/100
    #print(str(decendencia), "%")

    for pareja in parejas_list:
        #print( str(pareja['decendencia']) +" <= "+ str(decendencia))
        if( float( pareja['decendencia'] ) <= decendencia):
            cruzar.append(pareja)
        else:
            origin.append(pareja)

    return [cruzar, origin]

def cruzarLista(cruza_list):    
    cruzados = []

    puntos_corte_disponible = len( cruza_list[0]['id1'] )-1

    for indice in range( len(cruza_list) ):

        indi_1 = cruza_list[indice]['id1']
        indi_2 = cruza_list[indice]['id2']

        corte = random.randint(1, puntos_corte_disponible)

        cruza_A1 = indi_1[:corte]
        cruza_A2 = indi_1[corte:]

        cruza_B1 = indi_2[:corte]
        cruza_B2 = indi_2[corte:]

        nuevoIndividuo_1 = cruza_A1 + cruza_B2
        nuevoIndividuo_2 = cruza_B1 + cruza_A2        

        cruza_list[indice]['id1'] = nuevoIndividuo_1
        cruza_list[indice]['id2'] = nuevoIndividuo_2

        cruzados.append(cruza_list[indice])

    return cruzados


def mutarIndividuos(individuos_mutar, mutGen, mutIndividuo, datosComponenetes):    

    mutIndividuo = mutIndividuo/100        

    mutados_list = []
    for individuo in individuos_mutar:        
        probabilidadMutacionIndi = (random.randint(1, 100)) / 100        

        if (probabilidadMutacionIndi < mutIndividuo ):            
            individuo_mutado = mutarGenes(individuo, mutGen, datosComponenetes)
            mutados_list.append(individuo_mutado)
        else:
            mutados_list.append(individuo)

    return mutados_list

def mutarGenes(individuo, mutGen, datosComponenetes):    
    
    cpu = datosComponenetes[0]
    tarj = datosComponenetes[1]        
    disi = datosComponenetes[2]    
    ram = datosComponenetes[3]    
    graf = datosComponenetes[4]    
    almac = datosComponenetes[5]    
    gabi = datosComponenetes[6]    
    fuentePoder = datosComponenetes[7]
    
    mutGen = mutGen / 100
    
    for idArticulo in range( len(individuo) ):        
        lenArti = len(datosComponenetes[idArticulo])        

        mutGenProb = ( random.randint(1, 100) ) / 100
        if mutGenProb <= mutGen:
            encontrado = True
            while encontrado:                
                idArti = random.randint(1, lenArti)

                if idArticulo==0 or idArticulo==1 or idArticulo==3:                    
                    idDelProducto = int(individuo[idArticulo]) -1
                    idArti = obtenerRangos(idArticulo, idDelProducto, datosComponenetes)                                  
                    
                if( idArti != individuo[idArticulo] ):
                    individuo[idArticulo] = idArti
                    encontrado = False

    return individuo

def obtenerRangos(idArticulo, idDelProducto, dC):    
    
    #print(dC[idArticulo][ idDelProducto ])
    compatible = dC[idArticulo][ idDelProducto ]['compatible']    
    #print( "Compatible: ", compatible )

    lista_id_compatibles = []
    for x in range( len( dC[idArticulo] ) ):
        if ( dC[idArticulo][ x ]['compatible'] == compatible):
            #print( dC[idArticulo][ x ]['id'] )
            lista_id_compatibles.append( int( dC[idArticulo][ x ]['id'] ) )
    len_id = len(lista_id_compatibles) -1

    id_random = lista_id_compatibles[ random.randint( 0, len_id ) ]
    #print( "> id return: ", id_random )
    
    #print("\n ************ -----------")

    return id_random


def limpieza(lista, dC, presupuesto):

    listPc_limpia = []    

    for pc in lista:
        
        precioTotal = 0
        for idArticulo in range( len(pc) ):
            idArt = pc[idArticulo]            
            precioTotal += int(dC[idArticulo][idArt-1]['precio'])
        
        if(precioTotal <= presupuesto):        
            listPc_limpia.append(pc)        
        
    return listPc_limpia


def PODA(lista_pc, dC, PMaxima):
    print("PODA... ")

    list_aptitud = obtenerAptitudTotal(lista_pc, dC)
    
    list_aptitud = sorted(list_aptitud, key=lambda individuo: individuo["aptitud"], reverse=True)

    dataGraficar = datosGraficar(list_aptitud)

    list_aptitud = list_aptitud[:PMaxima]
    
    return [obtenerPc(list_aptitud), dataGraficar]

def datosGraficar(list_aptitud):
    print("Datos graficar... ")

    totalAptitud = 0
    for x in list_aptitud:
        totalAptitud += x["aptitud"]
    
    mejor = list_aptitud[0]["aptitud"]
    promedio = totalAptitud / len(list_aptitud)
    peor = list_aptitud[-1]["aptitud"]

    return {"mejor":mejor, "promedio":promedio, "peor":peor}


def obtenerPc(list_aptitud):
    print("\nobtener PC ... **** ")
    lista_podada = []
    for pc in list_aptitud:
        lista_podada.append(pc["pc"])

    return lista_podada


def obtenerAptitudTotal(lista_pc, dC):
    print("Aptitud total")    
    pc_aptitud = []
    for pc in lista_pc:
        
        aptitudTotal = 0
        precioTotal = 0

        for idArticulo in range( len(pc) ):
            idArt = pc[idArticulo]            
            #print( dC[idArticulo][idArt-1] )
            aptitudTotal += float( dC[idArticulo][idArt-1]['aptitud'] )
            precioTotal += float( dC[idArticulo][idArt-1]['precio'] )
            #print( dC[idArticulo][idArt-1]['aptitud'] )
        
        pc_aptitud.append( {'pc': pc, 'aptitud': aptitudTotal, 'precio':precioTotal } )

    return pc_aptitud


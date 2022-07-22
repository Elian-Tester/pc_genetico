import random

def seleccion(pI):
    
    seleccion=[]            

    auxDisminuir=2
    for x in range(1,pI):

        for j in range(auxDisminuir, pI+1):
            
            combinacion=[x, j]
            seleccion.append(combinacion)        
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
    print(str(decendencia), "%")

    for pareja in parejas_list:
        print( str(pareja['decendencia']) +" <= "+ str(decendencia))
        if( float( pareja['decendencia'] ) <= decendencia):
            cruzar.append(pareja)
        else:
            origin.append(pareja)

    return [cruzar, origin]

def cruzarLista(cruza_list):
    print("\nCruzar: ")
    cruzados = []

    puntos_corte_disponible = len( cruza_list[0]['id1'] )-1
    print(f'\nPuntos dispobibles: {puntos_corte_disponible}')

    for indice in range( len(cruza_list) ):
        print(cruza_list[indice])

        indi_1 = cruza_list[indice]['id1']
        indi_2 = cruza_list[indice]['id2']

        corte = random.randint(1, puntos_corte_disponible)

        cruza_A1 = indi_1[:corte]
        cruza_A2 = indi_1[corte:]

        cruza_B1 = indi_2[:corte]
        cruza_B2 = indi_2[corte:]

        nuevoIndividuo_1 = cruza_A1 + cruza_B2
        nuevoIndividuo_2 = cruza_B1 + cruza_A2
        

        print("Corte: ", corte)
        print("cz_1: ", nuevoIndividuo_1)
        print("cz_2: ", nuevoIndividuo_2,"\n")

        cruza_list[indice]['id1'] = nuevoIndividuo_1
        cruza_list[indice]['id2'] = nuevoIndividuo_2

        cruzados.append(cruza_list[indice])

    return cruzados


def mutarIndividuos(individuos_mutar, mutGen, mutIndividuo, datosComponenetes):
    print("\nIniciando mutacion:\n")

    mutIndividuo = mutIndividuo/100        

    mutados_list = []
    for individuo in individuos_mutar:        
        probabilidadMutacionIndi = (random.randint(1, 100)) / 100
        print("mutara ?? ", probabilidadMutacionIndi, " < ", mutIndividuo)

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

    print("\ngenes  { --------------------------  }")
    mutGen = mutGen / 100
    print("mut gen: ",mutGen,"%")
    print(individuo, "\n")
    for idArticulo in range( len(individuo) ):
        #print("id: ", individuo[idArticulo] )
        lenArti = len(datosComponenetes[idArticulo])
        #print("cant:", lenArti )        

        if idArticulo!=0 and idArticulo!=1 and idArticulo!=3:

            mutGenProb = ( random.randint(1, 100) ) / 100
            if mutGenProb <= mutGen:
                encontrado = True
                while encontrado:
                    idArti = random.randint(1, lenArti)
                    
                    if( idArti != individuo[idArticulo] ):
                        individuo[idArticulo] = idArti
                        encontrado = False
    
    print("\n---------------- >>> Individuo mutado: --------------------->>")
    print(individuo)
    print("{ --------------------------  }\n")

    return individuo





    
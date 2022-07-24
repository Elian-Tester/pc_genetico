import random


def crearIndividuos(pI, dC, rangoPrecio):
    print("Entra crear individuos !!!!!")
    individuos_list = []

    pcCant = len(dC[0])
    tarjMad = len(dC[1])
    disip = len(dC[2])
    ramCant = len(dC[3])
    grafCant = len(dC[4])
    almac = len(dC[5])
    gabiCant = len(dC[6])
    fuentPod = len(dC[7])

    for i in range(pI):
        pcC=-1
        tjC=-1
        dsi=-1
        ramC=-1
        grC=-1
        almC=-1
        gabC=-1
        fuentC=-1        

        pcValida = True
        print("\n\nCrea individuos >>>>>> ********************* <<<<<< ")
        while pcValida:
            pcC = reducirCalidad(pcC, pcCant)
            tjC = reducirCalidad(tjC, tarjMad)
            dsi = reducirCalidad(dsi, disip)
            ramC = reducirCalidad(ramC, ramCant)
            grC = reducirCalidad(grC, grafCant)
            almC = reducirCalidad(almC, almac)
            gabC = reducirCalidad(gabC, gabiCant)
            fuentC = reducirCalidad(fuentC, fuentPod)
            """ print("\n\npc: ",pcC)
            print("tarj: ",pcC)
            print("disip: ",pcC)
            print("ram: ",pcC)
            print("grafica: ",pcC)
            print("almacen: ",pcC)
            print("gabinet: ",pcC)
            print("fuente pod: ",pcC) """

            pc =[randomFun(pcCant-pcC), randomFun(tarjMad-tjC), randomFun(disip-dsi), randomFun(ramCant-ramC), randomFun(grafCant-grC), randomFun(almac-almC), randomFun(gabiCant-gabC), randomFun(fuentPod-fuentC)]
            
            if esCompatible(pc, dC):
                pcValida = verificarCostos(pc, dC, rangoPrecio)

        individuos_list.append(pc)
        #print(pc)

    return individuos_list

def reducirCalidad(numReducir, numMaximo):
    print("\nreducir: ", numReducir, " <==> num Maxio: ",numMaximo )
    if(numReducir != numMaximo-1):
        numReducir+=1
    return numReducir

def aumentarCalidad(numAumentar, numMaximo):
    print("\nreducir: ", numAumentar, " <==> num Maxio: ",numMaximo )
    if(numAumentar != numMaximo-1):
        numAumentar+=1
    return numAumentar


def verificarCostos(pc, dC, rangoPrecio):
    print("\n\n\nVerificando costos -------------")

    sumaPrecio = 0
    for idArticulo in range( len(pc) ):
        
        precio = float( dC[idArticulo][ pc[idArticulo] -1]['precio'] )
        #print( " precio: ", precio)
        sumaPrecio += precio

    print("Costo total de la pc: ", sumaPrecio, " <<<<***********************")
    if sumaPrecio <= rangoPrecio:
        #print("false... precio: ", sumaPrecio, " de rango: ", rangoPrecio)
        return False
    else:
        #print("true")
        return True
        




def randomFun(rango):
    return random.randint(1, rango)


def desagruparDatos(parejas):
    print("\nDesagrupando <---------")
    lista_separada = []

    for individuos in parejas:
        #print(individuos)
        lista_separada.append(individuos['id1'])
        lista_separada.append(individuos['id2'])
    
    return lista_separada

def esCompatible(individuo, datosComponenetes):
    print("\n\n--------------------------------  verificar compatible ")    

    cpuN = individuo[0] -1
    tarN = individuo[1] -1        
    ramN = individuo[3] -1
 
    cpuV = int(datosComponenetes[0][ cpuN ]['compatible'])
    tarjV = int(datosComponenetes[1][ tarN ]['compatible'])
    ramV = int(datosComponenetes[3][ ramN ]['compatible'])
    
    if cpuV != tarjV and ramV != tarjV:
        #print(" > incompatible")
        return False
    else:
        #print(" > compatible")
        return True
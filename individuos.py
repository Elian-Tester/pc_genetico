import random

def crearIndividuos(pI, dC):
    individuos_list = []
    
    for i in range(pI):
        
        pc =[randomFun(len(dC[0])), randomFun(len(dC[1])), randomFun(len(dC[2])), randomFun(len(dC[3])), randomFun(len(dC[4])), randomFun(len(dC[5])), randomFun(len(dC[6])), randomFun(len(dC[7]))]
        
        verificarCostos(pc, dC)
        individuos_list.append(pc)
        #print(pc)

    return individuos_list

def verificarCostos(pc, dC):
    print("\n\n\nVerificando costos -------------")

    sumaPrecio = 0
    for idArticulo in range( len(pc) ):
        #print( "tipo componente: ",idArticulo )

        #print("pc: ",pc[idArticulo])
        #print("component: ",dC[idArticulo][ pc[idArticulo] -1] )
        precio = float( dC[idArticulo][ pc[idArticulo] -1]['precio'] )
        print( " precio: ", precio)
        sumaPrecio += precio
    print("Costo total de la pc: ", sumaPrecio, " <<<<***********************")
        




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

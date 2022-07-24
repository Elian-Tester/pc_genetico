import matplotlib.pyplot as plt

from leerCSV import leerTodo
from organizaDatos import normalizarDatos


def controlEventos():
    print("Control eventos: \n")
    datosComponenetes = leerTodo()
    dataGraficarMax = []
    dataGraficarProm = []
    dataGraficarMin = []

    nuevaGeneracion = []
    for iterar in range(10):
        data = normalizarDatos(20, 20, datosComponenetes, 112300, nuevaGeneracion)
        nuevaGeneracion = data[0]

        dataGraficarMax.append(data[1]["mejor"])
        dataGraficarProm.append(data[1]["promedio"])
        dataGraficarMin.append(data[1]["peor"])

    print("\nUltima generacion: ")
    for x in nuevaGeneracion:
        print(x)

    print("\n\nGraficando coordenada **********")
    graficarHistorico(dataGraficarMax, dataGraficarMin, dataGraficarProm)
    #for grafi in dataGraficar:
    #    print(grafi)

def graficarHistorico(xMax, xMin, xPro):    
    print("\nGrafica Historico: ")

    print("\nMejor")

    yMax =  [x for x in xMax]
    yMin =  [x for x in xMin]
    yProm = [x for x in xPro]

    xGen = [x for x in range( len(xMax) )]

        #plt.figure(figsize=(10,5))
        #fig.tight_layout()
    plt.subplot(1, 1, 1)
    plt.plot(xGen,yMax, label='Mejor')
    plt.plot(xGen,yMin, label='Peor')
    plt.plot(xGen,yProm, label='Promedio')

    plt.legend()        
    plt.show()



if __name__ == "__main__":
    controlEventos() 
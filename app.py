import matplotlib.pyplot as plt
from flask import Flask, request
from flask_cors import CORS, cross_origin
import json

from leerCSV import leerTodo
from organizaDatos import normalizarDatos

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def index():
    return 'Creado'

@app.route('/get_pc', methods=['POST'])
def controlEventos():
    presupuesto = float(request.get_json())
    #presupuesto = 21300
    print("Presupuesto usuario: ", presupuesto)

    print("Control eventos: \n")
    datosComponenetes = leerTodo()
    

    
    seleccionMejores = []
    for i in range(5):
        dataGraficarMax = []
        dataGraficarProm = []
        dataGraficarMin = []

        nuevaGeneracion = []

        for iterar in range(5):
            data = normalizarDatos(10, 10, datosComponenetes, presupuesto, nuevaGeneracion)
            nuevaGeneracion = data[0]

            dataGraficarMax.append(data[1]["mejor"])
            dataGraficarProm.append(data[1]["promedio"])
            dataGraficarMin.append(data[1]["peor"])
        
        seleccionMejores.append( nuevaGeneracion[0] )
        #print(nuevaGeneracion[0])
    
    print("\nMejores: ")
    pc_detalles = []
    for pc_select in seleccionMejores:
        pc_datos = []
        for tipo in range( len(pc_select)):
            idProducto = pc_select[tipo]
            pc_datos.append( datosComponenetes[tipo][idProducto-1] )
        pc_detalles.append(pc_datos)


    print("\n\nGraficando coordenada **********")    

    return json.dumps(['pcs', pc_detalles ])
    #graficarHistorico(dataGraficarMax, dataGraficarMin, dataGraficarProm)
    #for grafi in dataGraficar:
        #print(grafi)

def graficarHistorico(xMax, xMin, xPro):    
    print("\nGrafica Historico: ")

    print("\nMejor")

    yMax =  [x for x in xMax]
    yMin =  [x for x in xMin]
    yProm = [x for x in xPro]

    xGen = [x for x in range( len(xMax) )]

    plt.subplot(1, 1, 1)
    plt.plot(xGen,yMax, label='Mejor')
    plt.plot(xGen,yMin, label='Peor')
    plt.plot(xGen,yProm, label='Promedio')

    plt.legend()        
    plt.show()



if __name__ == "__main__":
    app.run(port = 3001, debug = True)
    #controlEventos() 
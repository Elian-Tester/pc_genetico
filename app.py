from leerCSV import leerProcesador, leerTodo
from organizaDatos import normalizarDatos


def controlEventos():
    print("Control eventos: \n")
    datosComponenetes = leerTodo()

    normalizarDatos(4, datosComponenetes)



if __name__ == "__main__":
    controlEventos() 
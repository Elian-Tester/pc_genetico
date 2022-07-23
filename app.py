from leerCSV import leerTodo
from organizaDatos import normalizarDatos


def controlEventos():
    print("Control eventos: \n")
    datosComponenetes = leerTodo()

    normalizarDatos(4, datosComponenetes, 20400)


if __name__ == "__main__":
    controlEventos() 
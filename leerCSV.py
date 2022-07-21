import csv

def leerTodo(): 

    return [leerProcesador(), leerTarjetaMadre(), leerDisipador(), leerRAM(), leerGrafica(), leerAlmacenamiento(), leerGabinete(), leerFuentePoder()]

def leerProcesador():            
    results = []
    with open('csv\intel.csv') as File:
        reader = csv.DictReader(File)
        for row in reader:
            results.append(row)
            #print(row)
        #print (results)        
    return results

def leerTarjetaMadre():            
    results = []
    with open('csv\\tarjeta madre.csv') as File:
        reader = csv.DictReader(File)
        for row in reader:
            results.append(row)
            #print(row)
        #print (results)        
    return results

def leerDisipador():            
    results = []
    with open('csv\Disipador.csv') as File:
        reader = csv.DictReader(File)
        for row in reader:
            results.append(row)
            #print(row)
        #print (results)        
    return results

def leerRAM():            
    results = []
    with open('csv\RAM.csv') as File:
        reader = csv.DictReader(File)
        for row in reader:
            results.append(row)
            #print(row)
        #print (results)        
    return results

def leerGrafica():            
    results = []
    with open('csv\grafica.csv') as File:
        reader = csv.DictReader(File)
        for row in reader:
            results.append(row)
            #print(row)
        #print (results)        
    return results

def leerAlmacenamiento():            
    results = []
    with open('csv\Almacenamiento.csv') as File:
        reader = csv.DictReader(File)
        for row in reader:
            results.append(row)
            #print(row)
        #print (results)        
    return results

def leerGabinete():            
    results = []
    with open('csv\gabinete.csv') as File:
        reader = csv.DictReader(File)
        for row in reader:
            results.append(row)
            #print(row)
        #print (results)        
    return results

def leerFuentePoder():
    results = []
    with open('csv\\fuente de poder.csv') as File:
        reader = csv.DictReader(File)
        for row in reader:
            results.append(row)
            #print(row)
        #print (results)        
    return results
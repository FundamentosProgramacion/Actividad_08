#encoding: UTF-8
#Sergio Hernandez
#Tarea 08: Diccionarios

from Myro import beep

def crearDiccionarioFrecuencias() :
    d = {}
    ent = open ("notasMusicales.txt", "r")
    lista = ent.readlines()
    ent.close()
    
    #Procesar cada linea
    for linea in lista:
        datos = linea.split("-")
        #print (datos)
        nota = datos[0]
        frecuencia = float(datos[1])
        d[nota]= frecuencia
    
    return d
      
       
def crearDiccionarioDuracion(archivo):
    d = {}
    ent = open(archivo, "r")
    linea = ent.readline()
    ent.close()
    strValor = linea [6:]
    negra = float(strValor)

    
    #Crear Diccionario 
    dFiguras = { "redonda":4*negra, "blanca":2*negra, "negra":negra,  "corchea":negra/2, "semicorchea":negra/4, "blancaPuntillo":3*negra, "negraPuntillo":3*negra/2, "cambioNota":0.00001}
    return dFiguras

def tocarCancion(frecuencias, duracion, archivoCancion):
    ent = open (archivoCancion, "r")
    ent.readline() #Desechar primera linea
    lineas = ent.readlines()
    ent.close()
    
    for compas in lineas: 
        compas = compas.rstrip("\n")
        notas = compas.split(",")
        for nota in notas:
            datos = nota.split()
            print datos
            nombre = datos[0]
            figura = datos[1]
            
            beep(duracion[figura], frecuencias[nombre])
    
    

def main():
    dFrecuencias = crearDiccionarioFrecuencias()
    print (dFrecuencias)
    
    
    opcion = int (input("¿Que desas hacer? \n1. Reproducir cancion uno \n2. Reproducir cancion 2 (Scientist - Coldplay) \n0. Salir"))
    while opcion != 0 :
        if opcion == 1:
            dDuracion = crearDiccionarioDuracion("cancionUno.txt")
            tocarCancion(dFrecuencias, dDuracion, "cancionUno.txt")
        elif opcion == 2:
            dDuracion = crearDiccionarioDuracion("cancionDos.txt")
            tocarCancion(dFrecuencias, dDuracion, "cancionDos.txt")
        else: 
            print ("Opcion invalida. Intenta nuevamente")
        opcion = int (input("¿Que desas hacer? \n1. Reproducir cancion uno \n2. Reproducir cancion 2 (Scientist - Coldplay) \n0. Salir"))

            
   
main()

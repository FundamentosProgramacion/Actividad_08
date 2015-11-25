#encoding: UTF-8
#Autor: Astrid M. Villegas Berdejo
#diccionario

from Myro import beep


def crearDiccionarioFrecuencias ():
    d = {} #diccionario vacio
    ent = open ("notasMusicales.txt","r")
    lista = ent.readlines()
    ent.close()
    
    #Procesar cada linea
    for linea in lista:
        datos = linea.split("-")
        #print(datos)
        nota = datos[0]
        frecuencia = float(datos[1])
        d[nota] = frecuencia
        
    return d
    
def crearDiccionarioDuracion (archivo):
    
    ent = open (archivo,"r")
    linea = ent.readline() #primer linea
    ent.close()

    print (linea)
    strValor = linea[6:]
    negra = float(strValor) 

    #crear el diccionario    
    figuras = { "negra":negra, "blanca":2*negra, "redonda":4*negra, "corchea":negra/2,  "semicorchea":negra/4, "negraPuntillo":3*negra/2, "blancaPuntillo":3*negra}
    return figuras


def reproducirMelodia (dF, dD, archivo):
    entrada = open (archivo, "r")
    entrada.readline() #se desecha
    lista = entrada.readlines()
    entrada.close()
    
    for compas in lista:
        compas = compas.rstrip("\n")
        notas = compas.split (",") #["si5 negra","la4 corchea"]
        for nota in notas:
            datos = nota.split (" ")         #["si5","negra"]
            #print (datos)
            #print (datos [1:])
            print("*",datos[0],"*",datos[1],"*")
            frecuencia = datos [0]
            duracion = datos [1]
            beep (dD[duracion], dF[frecuencia])
            
    #entrada.close()
            
    
def main ():

    #cancion = int(input("¿Qué canción quieres escuchar (1,2)?"))
    
    dFrecuencias = crearDiccionarioFrecuencias()
    #print(dFrecuencias)
    
    cancion = int(input("Qué canción quieres reproducir(1,2)?"))
    
    while cancion != 0:
        if cancion == 1:
            dDuracion = crearDiccionarioDuracion ("cancionUno.txt")
            reproducirMelodia(dFrecuencias, dDuracion, "cancionUno.txt")
            #print (dDuracion)
            cancion = 0
            
        elif cancion == 2:
            dDuracion = crearDiccionarioDuracion ("cancionDos.txt")
            reproducirMelodia(dFrecuencias, dDuracion, "cancionDos.txt")
            cancion = 0
        
        else:
            cancion = int( input( "Canción no valida. Qué canción quieres reproducir?"))    
    
        
    
main()
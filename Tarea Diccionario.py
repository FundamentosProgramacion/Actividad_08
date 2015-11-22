#encoding:UTF-8
#Autor:Hector Manuel Takami Flores
#Listas y diccionarios

from Myro import*

def reproducirMelodia(dF,dD,archivo):
    entrada =open(archivo,"r")
    entrada.readline() #Se desecha la primer linea
    cancion=entrada.readlines()
    for compas in cancion:
        compas = compas.rstrip("\n")#Eliminamos caracteres ocultos al final de la linea
        #Debemos hacer una doble separacion la 1ra (Nota duracion) de (Nota duracion)
        notas = compas.split(",") #OJO AQUI ES NOTASSSSS
        
        for nota in notas: #OJO AQUI ES NOTA
            #nota -> "Nota duracion" ----- Separacion por un espacio " " 
            datos = nota.split(" ") #["Nota","duracion"]
            print("*",datos[0],"*",datos[1],"*")
            #beep (duracion, frecuencia)
            beep(dD[datos[1]],dF[datos[0]])
    entrada.close()
    


def crearDiccionarioDuracion():
    #Primero leemos solo el valor ´negra´ que sera la base de nuestro tiempo 
    entrada=open("Cancion.txt", "r")
    linea=entrada.readline()
    entrada.close()
    print(linea)
    strValor=linea[6:]
    negra=float(strValor)
     
    #Creamos diccionario
    figuras={"negra":negra,"blanca":negra*2,"redonda":4*negra, "corchea":negra/2, "semiCorchea":negra/4, "negraPuntillo":3*negra/2, "blancaPuntillo":3*negra}
    return figuras
    
    

def crearDiccionarioFrecuencias():
    d={} #Creamos un diccionario definido por {}
    entrada=open("notasMusicales.txt","r")
    lista = entrada.readlines() #Creamos una lista que va a leer cada linea del texto
    entrada.close()
    
    #Procesamos cada linea
    for linea in lista:
        datos=linea.split("-")
        #print(datos)
        
        nota=datos[0]
        frecuencia=float(datos[1])
        d[nota]=frecuencia #Agregamos a cada valor de nota que leemos un valor de frecuencia y lo agrega al diccionario
    return d #Regresamos el valor total del diccionario con los valores de las parejas = d{re#0:19.44, re#1:38.89....} nota:frecuencia
    #print(d) #Entonces cuando llamemos al diccionario en busca de una nota, nos genera su frecuencia automaticamente


def main():
    dFrecuencias=crearDiccionarioFrecuencias()
    dDuracion=crearDiccionarioDuracion()
    
    #print(dFrecuencias)
    print(dDuracion)
    reproducirMelodia(dFrecuencias,dDuracion,"Cancion.txt")
    
main()

#encoding:UTF-8
#Autor:Ernesto Cruz López A01169052
#Musica

from Myro import beep 

def crearDiccionarioFrecuencias():
    d={}#diccionario vacio
    ent=open("notasMusicales.txt","r")
    lista=ent.readlines()
    ent.close()
    #Procesar cada linea
    
    for linea in lista:
        datos=linea.split("-")
        #print(datos)
        nota=datos[0]
        frecuencia=float(datos[1])
        d[nota]=frecuencia
    return d
    
def crearDiccionarioDuracion(cancion):
    
    if cancion==2:
        ent=open("spyde.txt","r")
        linea=ent.readline() #Primer linea
        ent.close()
    else:
        ent=open("cancionUno.txt","r")
        linea=ent.readline()
        ent.close()
    
    strValor=linea[6:]
    negra=float(strValor)
    #cREAR DICCIONATIO
    figuras={ "negra":negra, "blanca":2*negra, "redonda":4*negra, "corchea":negra/2,  "semicorchea":negra/4, "negraPuntillo":3*negra/2, "blancaPuntillo":3*negra }
            
    return figuras

def reproducirMelodia(dF,dD,archivo):
    entrada= open (archivo,"r")
    entrada.readline() #se desecha
    lista=entrada.readlines()
    for compas in lista:
        compas=compas.rstrip("\n")
        notas= compas.split(",") #["si5 negra", ]
        for nota in notas:
            datos=nota.split(" ")
            #print("*",datos[0],"*",datos[1]"*")
            beep(dD[datos[1]],dF[datos[0]])
    entrada.close()
            
        
def main():
    cancion=int(input("Cancion 1 o 2"))
    if cancion==1:
        dFrecuencias=crearDiccionarioFrecuencias()
        print(dFrecuencias)
        dDuracion=crearDiccionarioDuracion(cancion)
        print(dDuracion)
        reproducirMelodia(dFrecuencias,dDuracion,"cancionUno.txt")
    else:
        dFrecuencias=crearDiccionarioFrecuencias()
        print(dFrecuencias)
        dDuracion=crearDiccionarioDuracion(cancion)
        print(dDuracion)
        reproducirMelodia(dFrecuencias,dDuracion,"spyde.txt")
    
    
main()
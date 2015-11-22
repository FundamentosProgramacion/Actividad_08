 #encoding:UTF-8
 #Jorge Daniel Juárez Ruiz
 #Intérprete de música
 
from Myro import*
 
def crearDiccionarioFrecuencias():
    d={}
    ent=open("notasMusicales.txt","r")
    lista=ent.readlines()
    ent.close()
    
    #procesar cada linea
    for linea in lista:
        datos=linea.split("-")
        nota=datos[0]
        frecuencia=float(datos[1])
        d[nota]=frecuencia #al Diccionario
    return d
   
def crearDiccionarioDuracion(archivo):
    ent=open(archivo,"r")
    linea=ent.readline()
    ent.close()
    strValor=linea[6:] #despues del espacio
    negra=float(strValor)
    #crear el diccionario
    figuras={"negra":negra, "blanca":2*negra,"redonda":4*negra,"corchea":negra/2,"semicorchea":negra/4,"negraPuntillo":negra*1.5,"blancaPuntillo":3*negra}
    return figuras

def reproducirMelodia(dF, dD, archivo):
    ent=open(archivo,"r")
    ent.readline()
    lista=ent.readlines()
    for compas in lista:
        compas=compas.rstrip("\n")
        notas=compas.split(",") #["si5 negra", "la6 corchea"
        for nota in notas:
            datos=nota.split(" ") #["si5","negra"]
            print("*",datos[0],"*",datos[1],"*")
            beep(dD[datos[1]],dF[datos[0]])
    ent.close()  
        


def main():
    dFrecuencias=crearDiccionarioFrecuencias()
    print(dFrecuencias)
    melodia=int(input("1. Cancion Uno\n2. Cancion Dos"))
    if melodia==1:
        dDuracion=crearDiccionarioDuracion("cancionUno.txt")
        print(dDuracion)
        reproducirMelodia(dFrecuencias,dDuracion,"cancionUno.txt")
    if melodia==2:
        dDuracion=crearDiccionarioDuracion("cancionDos.txt")
        print(dDuracion)
        reproducirMelodia(dFrecuencias,dDuracion,"cancionDos.txt")
    
main()
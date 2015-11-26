#Encoding:UTF-8
#Autor: Abraham Gandaría Alonso
#Tarea 8

from Myro import beep

def crearDiccionarioFrecuencias():
    d={} #Diccionario vacio
    ent=open("notasMusicales.txt","r")
    lista=ent.readlines()
    ent.close
    
    #Procesar cada linea
    for linea in lista:
        datos=linea.split("-")
        #print (datos)
        nota=datos[0]
        frecuencia=float(datos[1])
        d[nota]=frecuencia
    return d
                
def crearDiccionarioDuracion(archivo):
    ent=open(archivo,"r")
    linea=ent.readline() #Primer linea
    ent.close
    
    print(linea)
    strValor=linea[6:]
    negra=float(strValor)
    #Crear diccionario
    figuras={"negra":negra,"blanca":2*negra,"redonda":4*negra,"corchea":negra/2,"semicorchea":negra/4,"negraPuntillo":3*negra/2,"blancaPuntillo":3*negra}
    return figuras
    
def reproducirMelodia(dF,dD,archivo):
    entrada=open(archivo,"r")
    entrada.readline() #Se desecha
    lista=entrada.readlines()
    for compas in lista:
        compas=compas.rstrip("\n")
        notas=compas.split(",") #["si5 negra","la4 corchea"]
        for nota in notas:
            #nota-> "si5 negra"
            print("*",nota,"*")
            datos=nota.split(" ") #["si5","negra"]
            print("*",datos[0],"*",datos[1],"*")
            beep(dD[datos[1]],dF[datos[0]])
    entrada.close    
    
def main():
    dFrecuencias=crearDiccionarioFrecuencias()
    print(dFrecuencias)
    cancion=int(input("1.Cancion 1\n2.Cancion 2"))
    if cancion==1:
        dDuracion=crearDiccionarioDuracion("cancionUno.txt")
        print(dDuracion)
        reproducirMelodia(dFrecuencias,dDuracion,"cancionUno.txt")
    if cancion==2:
        dDuracion=crearDiccionarioDuracion("cancionDos.txt")
        print(dDuracion)
        reproducirMelodia(dFrecuencias,dDuracion,"cancionDos.txt")
main()
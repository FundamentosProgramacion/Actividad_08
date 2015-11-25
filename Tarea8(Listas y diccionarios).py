# encoding:UTF-8
# Autor: Humberto Serra Mendieta
# Tarea 8: Listas y diccionarios 

from Myro import*

def crearDiccionarioFrecuencias() :
    d={} 
    ent=open("notasMusicales.txt","r")
    lista=ent.readlines()
    ent.close()

    for linea in lista :
        datos=linea.split("-")
        nota=datos[0]
        frecuencia=float(datos[1])
        d[nota]=frecuencia
    return d
   
def crearDiccionarioDuracion():
    ent=open("song.txt","r")
    linea=ent.readline()
    ent.close()
    
    print(linea)
    strValor=linea[6:]
    negra=float(strValor) 
    
    figuras={"negra":negra, "blanca":2*negra, "redonda":4*negra, "corchea":negra/2, "semiCorchea":negra/4, "negraPuntillo":3*negra/2, "blancaPuntillo":3*negra}
    return figuras

def reproducirMelodia(dF,dD,archivo):
    entrada=open(archivo,"r")
    entrada.readline()  
    lista=entrada.readlines()
    for compas in lista:
        compas=compas.rstrip("\n")
        notas=compas.split(",")
        for nota in notas:
            datos=nota.split(" ")
            print("*",datos[0],"*",datos[1],"*")
            beep(dD[datos[1]],dF[datos[0]])
    entrada.close()

def main():
    dFrecuencias=crearDiccionarioFrecuencias()
    print(dFrecuencias)
    dDuracion=crearDiccionarioDuracion()
    print(dDuracion)
    reproducirMelodia(dFrecuencias,dDuracion,"song.txt")
main()
#encoding: UTF-8
#David Salvador Ruiz Roa
#diccionarios y tarea 8

from Myro import*

def crearDiccionarioFrecuencias():
    d = {} #Diccionario vacio
    ent = open("notasMusicales.txt","r")
    lista = ent.readlines()
    ent.close
    
    #Procesar cada línea
    for linea in lista:
        datos = linea.split("-")
        
        #print(datos)
        nota = datos[0]
        frecuencia = float(datos[1])
        d[nota] = frecuencia
        
    return d
    
def crearDiccionarioDuracion():
    ent = open("Titanic.txt","r")
    linea = ent.readline() #PrimerLinea
    ent.close()
    
    print(linea)
    strValor = linea[6:]
    negra = float(strValor)
    figuras = {"negra":negra, "blanca":2*negra, "redonda":4*negra, "corchea":negra/2, "semicorchea":negra/4, "negraPuntillo":3*negra/2, "blancaPuntillo":3*negra}
    return figuras

def reproducirMelodia(dF,dD,archivo):
    entrada = open(archivo,"r")
    entrada.readline() #Se desecha
    lista = entrada.readlines()
    for compas in lista:
        compas = compas.rstrip("\n")
        notas = compas.split(",") #["si 5 negra","la4 corchea"]
        for nota in notas: 
            #nota -> "si5 megra"
            datos = nota.split(" ") # ["si5","negra"]
            print("*",datos[0],"*",datos[1],"*")
            beep(dD[datos[1]],dF[datos[0]])
    entrada.close()            

def main():

    dFrecuencias = crearDiccionarioFrecuencias()
    print(dFrecuencias)
    dDuracion = crearDiccionarioDuracion()
    print(dDuracion)
    reproducirMelodia(dFrecuencias,dDuracion,"Titanic.txt")
    
main()
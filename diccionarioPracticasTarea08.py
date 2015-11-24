#encoding: UTF-8

from Myro import * 

def crearDiccionarioFrecuencias () : 
    d = {} # Diccionario Vacio 
    ent = open("notasMusicales.txt","r") 
    lista = ent.readlines()
    ent.close()
    
    # Procesar cada linea 
    for linea in lista : 
        datos = linea.split("-") 
        #print(datos)
        nota = datos[0]
        frecuencia = float(datos[1]) 
        d[nota] = frecuencia
    
    return d 
    
def crearDiccionarioDuracion() : 
    ent = open("cancionUno.txt","r")
    linea = ent.readline()  # Primer linea 
    ent.close()
    
    print(linea)
    strValor = linea[6:]
    negra = float(strValor)
    figuras = { "negra":negra, "blanca":2*negra, "redonda":4*negra, "corchea":negra/2, "semicorchea":negra/4, "negraPuntillo":3*negra/2, "blancaPuntillo":3*negra }
    return figuras 
    
def reproducirMelodia(dF,dD, archivo) :     
    entrada = open(archivo,"r") 
    entrada.readline() # Se desecha 
    lista = entrada.readlines()
    for compas in lista : 
        compas = compas.rstrip("\n")
        notas = compas.split(",") #["si5 negra", "la4 corchea"]
        for nota in notas : 
            # nota -> "si5 negra" 
            datos = nota.split(" ") #["si5","nega"]
            print("*",datos[0],"*",datos[1],"*")
            beep(dD[datos[1]],dF[datos[0]])
    entrada.close()
    
def crearDiccionarioFrecuenciasDos () : 
    d = {} # Diccionario Vacio 
    ent = open("notasMusicales.txt","r") 
    lista = ent.readlines()
    ent.close()
    
    # Procesar cada linea 
    for linea in lista : 
        datos = linea.split("-") 
        #print(datos)
        nota = datos[0]
        frecuencia = float(datos[1]) 
        d[nota] = frecuencia
    
    return d 

def crearDiccionarioDuracionDos() : 
    ent = open("cancionDos.txt","r")
    linea = ent.readline()  # Primer linea 
    ent.close()
    
    print(linea)
    strValor = linea[6:]
    negra = float(strValor)
    figuras = { "negra":negra, "blanca":2*negra, "redonda":4*negra, "corchea":negra/2, "semicorchea":negra/4, "negraPuntillo":3*negra/2, "blancaPuntillo":3*negra }
    return figuras 
      
    
    
    
    
    
    
def main () :
    opciones = int(input("Teclea la melodia que quieras escuchar: 1 o 2")) 
        while opciones != 3:   
                if opciones == 1 : 
                    dFrecuencias = crearDiccionarioFrecuencias() 
                    print(dFrecuencias)
                    dDuracion = crearDiccionarioDuracion()
                    print(dDuracion)
                    reproducirMelodia(dFrecuencias,dDuracion,"cancionUno.txt")
                elif opciones == 2 : 
                    dFrecuenciasDos = crearDiccionarioFrecuenciasDos()
                    print(dFrecuenciasDos) 
                    dDuracion = crearDiccionarioDuracionDos()
                    print(dDuracionDos) 
                    reproducirMelodia2(dFrecuenciasDos,dDuracionDos,"cancionDos.txt") 
main() 
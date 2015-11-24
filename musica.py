#encoding: utf-8
#Autor: Brian Saggiante A01377511
#Melodia

from Myro import*

def crearDiccionarioFrecuencias():
    d={} #Diccionario vacio
    ent=open('notasMusicales.txt','r')
    lista=ent.readlines()
    ent.close()
    
    for linea in lista:
        datos=linea.split('-')
        nota=datos[0]
        frecuencia=float(datos[1])
        d[nota]=frecuencia
    return d
        
def crearDiccionarioDuracion():
    ent=open('Clocks.txt','r')
    linea=ent.readline()
    ent.close()
    
    print(linea)
    strValor=linea[6:]
    negra=float(strValor) 
    #Crear el diccionario
    figuras={'negra':negra, 'blanca':2*negra, 'corchea':negra/2, 'semicorche':negra/4, 'negraPuntillo':3*negra/2, 'blancaPuntillo':3*negra}
    return figuras

def reproducirMelodia(dF,dD,archivo):
    entrada=open(archivo,'r')
    entrada.readline()  #se desecha
    lista=entrada.readlines()
    for compas in lista:
        compas=compas.rstrip('\n')
        notas=compas.split(',')
        for nota in notas:
            datos=nota.split(' ')
            print('*',datos[0],'*',datos[1],'*')
            beep(dD[datos[1]],dF[datos[0]])
    entrada.close

def main():
    dFrecuencias=crearDiccionarioFrecuencias()
    print(dFrecuencias)
    dDuracion=crearDiccionarioDuracion()
    print(dDuracion)
    reproducirMelodia(dFrecuencias,dDuracion,'Clocks.txt')
main()
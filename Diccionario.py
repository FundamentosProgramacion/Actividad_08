#Encoding: UTF-8
#Pablo Sanchez
#Diccionario

from Myro import beep

def crearDiccionarioFrecuencias() :
	d = {} # diccionario vacio
	ent = open("notasMusicales.txt","r")
	lista = ent.readlines()
	ent.close

	#Procesar cada linea
	for linea in lista :
		datos = linea.split("-")
		nota = datos[0]
		frec = float(datos[1])
		d[nota] = frec
	return d

def crearDiccionarioDuracion(archivo) :
	ent = open(archivo,"r")
	linea = ent.readline()
	ent.close()
	#procesar linea
	#leer linea a partir de la posicion 6
	strValor = linea[6:]
	negra = float(strValor)
	#print(negra)
	#crear diccionario
	figuras = { "negra":negra, "blanca":2*negra, "redonda":4*negra, "corchea":negra/2,  "semicorchea":negra/4, "negraPuntillo":3*negra/2, "blancaPuntillo":3*negra }
	return figuras

def reproducirMelodia(df,dd,archivo) :
	entrada = open(archivo,"r")
	entrada.readline() #se desecha
	lista = entrada.readlines()
	for compas in lista :
		compas = compas.rstrip("\n")
		notas = compas.split(",") #["si negra","la4 corchea"]
		for nota in notas :
			#nota --> "si5 negra"
			datos = nota.split(" ") #["si5","negra"]
			#print("*",dd[datos[1]],"*",df[datos[0]],"*")
			beep(dd[datos[1]], df[datos[0]])
	entrada.close()


def main() :

	dFrecuencias = crearDiccionarioFrecuencias()
	menu = int( input("Que cancion quieres escuchar?\n1.- Ejemplo\n2.- La Vie en Rose\n3.- Salir"))
	while menu != 3 :
		if menu == 1 :
			dDuracion = crearDiccionarioDuracion("cancionUno.txt")
			reproducirMelodia(dFrecuencias,dDuracion,"cancionUno.txt")
		elif menu == 2 :
			dDuracion = crearDiccionarioDuracion("cancionDos.txt")
			reproducirMelodia(dFrecuencias,dDuracion,"cancionDos.txt")
		menu = int( input("Que cancion quieres escuchar?\n1.- Ejemplo\n2.- La Vie en Rose\n3.- Salir"))



main()
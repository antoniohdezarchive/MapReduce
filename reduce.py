#!/usr/bin/python

#######################################################################
# Reduce.py							                                  #
#								                                      #
# Este programa lee el STDIN que recibe de Map.py y va sumarizando    #
# por cada clave (palabra) para escribir su frecuencia de aparicion   #
# El output de este programa son las palabras que recibe de Map.py    #
# sin repetirse seguidas de un tab y el valor de su frecuencia.       #
#																	  #
# Output: palabra\tfrecuencia		                                  #
#	  ej: foo	4                                                     #
# 	      raul	2					                                  #
#######################################################################

import sys
import re
import ast
import math

'''funcion que calcula la moda de una entrada de datos'''
def moda(valores, nombres):
	print "--------Moda---------"
	for x in xrange(0,len(valores)):
		cuenta = valores[x].count(valores[x][0])
		cuenta2 = 0
		moda = []
		moda.append(valores[x][0])
		for y in range(0,len(valores[x])):
			cuenta2 = valores[x].count(valores[x][y])
			if cuenta2 > cuenta:
				moda = []
				moda.append(valores[x][y])
				cuenta = valores[x].count(valores[x][y])
			elif cuenta2 == cuenta:
				moda.append(valores[x][y])
		moda = list(set(moda))
		print nombres[x], moda

def promedio(valores, nombres):
	print "-----Promedios-------"
	l = 0
	nombre = []
	prom = []
	for lista in valores :
		lista = [float(i) for i in lista]
		promedio = sum(lista) / len(lista)
		print  nombres[l], promedio
		nombre.append(nombres[l])
		prom.append(promedio)
		l = l + 1
	return prom


def desviacionEstandar(valores, nombres):
	promedios = promedio(valores, nombres)
	i = 0
	desviaciones = []
	for lista in valores:
		suma = 0
		for valor in lista:
			suma = suma + pow(float(valor) - float(promedios[i]), 2)
		suma = suma / (len(lista) - 1)
		suma = math.sqrt(suma)
		desviaciones.append(suma)
	i += 1
	print desviaciones
	return desviaciones

def varianza(valores, nombres):
	var = desviacionEstandar(valores, nombres)
	varis = []
	for valor in var:
		varis.append(pow(valor,2))

	print varis
	
	
				


# input viene desde el STDIN (standard input)
valores = []
nombres = []
for line in sys.stdin:
	line = line.strip()
	nom, lista = line.split(' ', 1)
	valores.append(ast.literal_eval(lista))
	nombres.append(nom)

print valores


moda(valores, nombres)
promedio(valores,nombres)
desviacionEstandar(valores, nombres)
varianza(valores, nombres)



	
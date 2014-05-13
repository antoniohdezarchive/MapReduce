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

from operator import itemgetter
import sys

current_key = ""
current_val = 0
key = ""
count = 1
avg = 0

# input viene desde el STDIN
for line in sys.stdin:
	line = line.strip()
	key, val = line.split(" ", 1)
	val = float(val)
	if current_key == key:
		current_val += val
		count += 1
	else:
		if current_key:
			avg = current_val / count
			print '%s\t%s' % (current_key, avg)
			count = 1
		current_val = val
		current_key = key

#imprime la ultima palabra
if current_key == key:
	avg = current_val / count
	print '%s\t%s' % (current_key, avg)
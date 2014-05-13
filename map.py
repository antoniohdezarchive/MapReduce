#!/usr/bin/python

#######################################################################
# Map.py 															  #
#                                                                     #
# Este programa lee el STDIN, por cada linea elimina los espacios     #
# iniciales y traseros, luego elimina todos los simbolos y convierte  #
# las palabras a minusculas. Luego se queda con cada una de las       #
# palabras que componen la linea; y por cada palabra imprime una      #
# linea con la palabra seguida de un tab y un 1.                      #
#								      								  #
# Output: palabra\t1	       					      				  #
#	  ej: foo	1                                             		  #
# 	      foo	1					      							  #
#######################################################################

import sys
import re

# input viene desde el STDIN (standard input)
for line in sys.stdin:
	line = line.strip()
	periodo, name, val = line.split(" ", 2)
	print "%s %s" % (name, val)
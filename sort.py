#!/usr/bin/python
import sys
key_anterior = ""
val_anterior = ""
datos = []
salida = {}
for line in sys.stdin:
	datos.append(line)

datos.sort()
for val in datos:	
	key, val = val.split(" ", 1)
	if salida.has_key(key):
		salida[key].append(val.replace("\n", ""))
	else:
		salida[key] = [val.replace("\n", "")]

for val in salida:
	print val, salida[val]
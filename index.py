#!/usr/bin/env python
import os

print """\
Content-Type: text/html\n
"""
content=""
with open('templates/index.html', 'r') as f:
    content = f.read()

entrada = ""
salida = ""
os.chdir("entrada/")
for dirname, dirnames, filenames in os.walk('.'):
    for filename in filenames:
    	if filename == ".DS_Store":
    		os.remove(filename)
    		continue
    	entrada += "<li class='list-group-item'>%s</li>" % filename

os.chdir("../salida/")
for dirname, dirnames, filenames in os.walk('.'):
    # print path to all subdirectories first.

    # print path to all filenames.
    for filename in filenames:
    	if filename == ".DS_Store":
    		os.remove(filename)
    		continue
    	salida += "<li class='list-group-item'>%s</li>" % filename

content = content.replace("{entrada}", entrada)
content = content.replace("{salida}", salida)
print content
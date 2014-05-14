#!/usr/bin/env python
import cgi, os
import cgitb; cgitb.enable()
from redirect import Redirect

form = cgi.FieldStorage()
dirPath = "salida/"
fileList = os.listdir(dirPath)
for fileName in fileList:
	os.remove(dirPath+"/"+fileName)

Redirect("index.py")
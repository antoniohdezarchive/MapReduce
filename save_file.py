#!/usr/bin/env python
import cgi, os
import cgitb; cgitb.enable()
from redirect import Redirect

try: # Windows needs stdio set for binary mode.
	import msvcrt
	msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
	msvcrt.setmode (1, os.O_BINARY) # stdout = 1
except ImportError:
	pass

form = cgi.FieldStorage()

# A nested FieldStorage instance holds the file
try:
	fileitem = form['file']
except Exception, e:
	Redirect("index.py")

# Test if the file was uploaded
if fileitem.filename:   
	# strip leading path from file name to avoid directory traversal attacks
	fn = os.path.basename(fileitem.filename)
	open('entrada/' + fn, 'wb').write(fileitem.file.read())
	Redirect("index.py")
else:
	Redirect("index.py?error")
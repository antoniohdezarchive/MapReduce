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
	formato = form["json"]
except Exception, e:
	pass#Redirect("index.py?error")

try:
	formato = form["csv"]
except Exception, e:
	pass#Redirect("index.py?error")

from subprocess import Popen, PIPE
for key in form.keys():
	formato = str(key)
p1 = Popen(["python", "lector.py"], stdout=PIPE)
p2 = Popen(["python", "map.py"], stdin=p1.stdout, stdout=PIPE)
p3 = Popen(["python", "sort.py"], stdin=p2.stdout, stdout=PIPE)
p4 = Popen(["python", "reduce.py", formato], stdin=p3.stdout)

print """\
Content-Type: text/html\n
"""

Redirect("index.py")
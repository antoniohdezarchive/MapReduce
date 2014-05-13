#!/usr/bin/python
import os
import json

def leer_json(filename):
	with open(filename, "r") as f:
		content = f.read()
	j = json.loads(content)
	content = ""
	for report in j["reports"]:
		for key, val in report.iteritems():
			for data in val:
				for name, rep in data.iteritems():
					content += "%s %s %s\n" % (key, name, rep)
	return content

def leer_txt(filename):
	with open(filename, "r") as f:
		content = f.read()
	return content

def leer_archivo(filename):
	content = ""
	ext = filename.split(".")[-1]
	if ext == "txt":
		content = leer_txt(filename)
	elif ext == "json":
		content = leer_json(filename)
	return content

entrada = ""
datos = ""
os.chdir("entrada/")
for dirname, dirnames, filenames in os.walk('.'):
	for filename in filenames:
		datos += leer_archivo(filename)

print datos


#!/usr/bin/env python
def Redirect(url = "index.py"):
	print "Content-Type: text/html"
	print "Location: %s" % url
	print # HTTP says you have to have a blank line between headers and content
	print "<html>"
	print "<head>"
	print "    <meta http-equiv='refresh' content='0;url=%s' />" % url
	print "    <title>You are going to be redirected</title>"
	print "</head>" 
	print "<body>"
	print "    Redirecting... <a href='%s'>Click here if you are not redirected</a>" % url
	print "</body>"
	print "</html>"
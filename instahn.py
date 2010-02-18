#instapaper.py is Copyright (c) 2009 Eiji Kato
#See http://github.com/technolize/python-instapaper/ for details.

#hnapi.py is Copyright (c) 2010 Scott Jackson
#See http://github.com/scottjacksonx/hn-api/ for details.

from instapaper import *
from hnapi import *
import sys

class InstaHNException(Exception):
	pass
	

username = ""
password = ""

args = sys.argv

if len(args) == 1:
	username = raw_input("Enter your Instapaper username: ")
	password = raw_input("Enter your Instapaper password (if you don't have a password, just press Return): ")
elif len(args) == 2:
	username = args[1]
elif len(args) == 3:
	username = args[1]
	password = args[2]


try:
	hn = HackerNewsAPI()
	instapaper = Instapaper(username, password)
	print "Authorising your Instapaper credentials..."
	instapaper.auth()
	print "Instapaper credentials accepted."
except Exception as e:
	print e
	sys.exit()
	
try:
	print "Getting stories from Hacker News..."
	stories = hn.getTopStories()

	for s in stories:
		instapaper.add(s.URL)
		print "story added = " + s.title
except HNException as e:
	print e
	sys.exit()
	
	
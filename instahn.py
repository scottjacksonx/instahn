#instapaper.py is Copyright (c) 2009 Eiji Kato
#See http://github.com/technolize/python-instapaper/ for details.

from instapaper import *
from hnapi import *
import sys

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

hn = HackerNewsAPI()
instapaper = Instapaper(username, password)
instapaper.auth()
stories = hn.getTopStories()

for s in stories:
	instapaper.add(s.URL)
	print "story added = " + s.title
	
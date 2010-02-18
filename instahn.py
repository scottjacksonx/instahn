instapaper.py is Copyright (c) 2009 Eiji Kato
See http://github.com/technolize/python-instapaper/ for details.

from instapaper import *
from hnapi import *

username = ""	# Change this to your own Instapaper username.
password = ""	# Change this to your own Instapaper password.



hn = HackerNewsAPI()
instapaper = Instapaper(username, password)
instapaper.auth()
stories = hn.getTopStories()

for s in stories:
	instapaper.add(s.URL)
	print "story added = " + s.title
	
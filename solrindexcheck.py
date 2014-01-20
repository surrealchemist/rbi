#!/usr/bin/env python
#Simple script to check some stats on a solr index. Written against SOLR 2.4, so your mileage may vary.
#Written by Joshua Kleiner

import urllib2
import sys
try:
    import json
except ImportError:
    import simplejson as json

def getIndexInfo (solrAddress,index):

	URL = ("http://") + solrAddress + (":8983/solr/") + index + ("/replication?command=details&wt=json")
	try:
	        Response = urllib2.urlopen(URL)
                stringResponse = Response.read()
                jsonResponse = json.loads(stringResponse)
                details = jsonResponse['details']
                indexSize = details['indexSize']
                print "Server " + solrAddress + " " + index + " Index Size: " + indexSize
                print "Server " + solrAddress + " " + index + " generation: " + str(details['generation'])
                print "Server " + solrAddress + " " + index + " indexVersion: " + str(details['indexVersion'])
                print ""
	except:
                print "Cannot reach server " + str(solrAddress) + ", check if the server is up \n"


 

if len(sys.argv) == 1:
	print "Please provide a server URL or IP, and the index you wish to check"
	print "Example:"
	print "solrindexcheck.py 192.168.1.1 myindex1"
elif len(sys.argv) > 3:
	print "Please provide only 2 arguments (URL/IP and the index to check)"
	print "Example:"
	print "solrindexcheck.py 192.168.1.1 myindex1"
else:
	getIndexInfo(sys.argv[1],sys.argv[2])
	

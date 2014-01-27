#!/usr/bin/env python
import socket
import sqlite
import sys

database = "./portcheck.db"

#For future reference: CREATE TABLE endpoints ( description text, address text, port integer, PRIMARY KEY (description) );

OPEN = '\33[94m'
CLOSED = '\33[31m'
ENDFORMAT = '\033[0m'

def portcheck(description,address,port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result = s.connect_ex(( address , int(port)))

	if(result == 0) :
		print '%s%-25s Host %-30s Port %7s Socket is open%s' % (OPEN, description, address, port, ENDFORMAT)
	else :
		print '%s%-25s Host %-30s Port %7s Socket is closed%s' % (CLOSED, description, address, port, ENDFORMAT)
	s.close()

try:
	conn = sqlite.connect(database)
except:
	print "Could not find database file %s, or incorrect permissions" % database
	exit()

cur = conn.cursor()
cur.execute('SELECT * FROM endpoints')

for row in cur.fetchall():
	portcheck(row[0],row[1],row[2]);

conn.close()

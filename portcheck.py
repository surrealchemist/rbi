#!/usr/bin/env python
import socket
import sqlite
import sys

database = "/rbiops/share/portcheck.db"
#For future reference: CREATE TABLE endpoints ( description text, address text, port integer, PRIMARY KEY (description) );

def portcheck(description,address,port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result = s.connect_ex(( address , int(port)))

	if(result == 0) :
		print '\33[94m%s socket is open: Host %s Port %s\033[0m' % (description, address, port)
	else :
		print '\33[31m%s socket is closed: Host %s Port %s\033[0m' % (description, address, port)
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

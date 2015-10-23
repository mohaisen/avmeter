import MySQLdb as mdb
import sys

con=mdb.connect('192.168.120.40','automal','1d3f3ns3','automal')
cur=con.cursor()

#ZeroAccess based on port number
#cur.execute('select distinct sid from network where dst_port=22292')
#for sid in cur.fetchall():
#	sid=sid[0]
#	cur.execute('select bin_id from submissions where sid=%d'%(sid))
#	bin_id=cur.fetchall()[0]
#	cur.execute('select md5 from binaries where id=%d'%(bin_id))
#	print cur.fetchall()[0][0]

cur.execute('select bin_id from submissions where comment="%s"'%(sys.argv[1]))
for bin_id in cur.fetchall():
	bin_id=bin_id[0]
	cur.execute('select md5 from binaries where id=%d'%(bin_id))
	print cur.fetchall()[0][0]
	

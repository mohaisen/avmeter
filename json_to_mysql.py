import json, MySQLdb, os, sys

path = sys.argv[1]
mdb= MySQLdb.connect(user='root',db='avmeter')
cur=mdb.cursor()

for f in os.listdir(path):
	if f.endswith('.json'):
		obj=json.loads(open(f,'rb').read())
		tbl=f.split('.')[0]
		print "processing file %s with %d records"%(f,len(obj.keys()))
		for md5 in obj:
			col=''
			val=''
			for av in obj[md5]:
				col+=',%s'%(av.replace('-','').replace('+',''))
				val+=",'%s'"%(obj[md5][av]) 
			qry="insert into %s (md5 %s) VALUES('%s' %s)"%(tbl,col,md5,val)
			if cur.execute(qry)<1:
				print "error in file %s md5 %s"%(tbl,md5)
			mdb.commit()

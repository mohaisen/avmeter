'''

This script gives you how many engines (s/l or l/s) are needed to achieve good completness.
'''
import sys
import json
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename", help="write report to FILE", metavar="FILE")
parser.add_option("-q", "--quiet", dest="", action="store_false", dest="verbose", default=True, help="don't print status messages to stdout")
parser.add_option("-z", "--zbot", action="store", help="gnerate coverage for all scans of zbot and write in FILE", metavar="FILE")
parser.add_option("-g", "--generic", action="store", help="gnerate coverage for all scans of generic zbot and write in FILE", metavar="FILE")
parser.add_option("-t", "--trojan", action="store", help="gnerate coverage for all scans of trojan zbot and write in FILE", metavar="FILE")
parser.add_option("-a", "--all", action="store", help="gnerate coverage for all scans of all zbot and write in FILE", metavar="FILE")
(options, args) = parser.parse_args(values=parser)

print args
print options
exit(0)

#print args

if sys.argv[1].rstrip() == '--help':
        print 'Usage: python coverage.py [option] zeus.json'
        print 'Options include the following:'
        print '\t-zbot: generates coverage using all scans of zbot'
        print '\t-generic: generates coverage using all scans of generic zbot'
        print '\t-trojan: generates coverage using all scans of trojan zbot'
        print '\t-all: generates coverage using zbot, trojan, and generic scans'
        print '\t--help: shows a help list'
	exit(0)
else:
	f=open(sys.argv[2],'rb')
	md5s = {}
	avs = {}
	jj = json.load(f)
	zeus = {}
	x = 0
	for md5 in jj:
		zeus[md5] = jj[md5]
		x+=1
		if x == 1000:
			break 

	if sys.argv[1].rstrip() == '-all':
		for md5 in zeus:
			for av in zeus[md5]:
				if 'zbot' in zeus[md5][av].lower() or 'trojan' in zeus[md5][av].lower() or 'generic' in zeus[md5][av].lower():
					if av in avs:
						avs[av].append(md5)
					else:
						avs[av] = []
						avs[av].append(md5)
	elif sys.argv[1].rstrip() == '-zbot':
		for md5 in zeus:
			for av in zeus[md5]:
				if 'zbot' in zeus[md5][av].lower():
					if av in avs:
						avs[av].append(md5)
					else:
						avs[av] = []
						avs[av].append(md5)
	elif sys.argv[1].rstrip() == '-generic':
		for md5 in zeus:
			for av in zeus[md5]:
				if 'generic' in zeus[md5][av].lower():
					if av in avs:
						avs[av].append(md5)
					else:
						avs[av] = []
						avs[av].append(md5)

	elif sys.argv[1].rstrip() == '-trojan':
		for md5 in zeus:
			for av in zeus[md5]:
				if 'trojan' in zeus[md5][av].lower():
					if av in avs:
						avs[av].append(md5)
					else:   
						avs[av] = []
						avs[av].append(md5)

#completeness score of detection
avsd = {}
dd = []
for av in avs:
	if len(avs[av])>=100:
		if len(avs[av]) in avsd:
			avsd[len(avs[av])-1]=avs[av]
			dd.append(len(avs[av])-1)
		else:
			avsd[len(avs[av])]=avs[av]
			dd.append(len(avs[av]))
#compute that for the largest to smallest, and smallest to largest
aup = set()
adown = set()

au = sorted(dd, reverse=True)
ad = sorted(dd, reverse=False)


for i in range(0,len(au)):
	for item in avsd[au[i]]:
		aup.add(item)
	for item in avsd[ad[i]]:
		adown.add(item)
	print i+1, len(aup), len(adown)
##looking forward to implement the best heuristic. 

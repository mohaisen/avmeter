import json
import sys

data=json.loads(open(sys.argv[1], 'rb').read())

avs={}
for md5 in data.keys():
	for av in data[md5]:
		if av not in avs:
			avs[av]={}
		else:
			print 
			if data[md5][av] not in avs[av]:
				avs[av][data[md5][av]]=1
			else:
				avs[av][data[md5][av]]+=1
s_list=[]
for av in avs:
	max=0
	max_n=''
	for detect in avs[av]:
		if avs[av][detect]>max:
			max=avs[av][detect]
			max_n=detect
			s_list.append((max, max_n,av))

for i in sorted(s_list, reverse=True):
	print i[0],i[1],i[2]
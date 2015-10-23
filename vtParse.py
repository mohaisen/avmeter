from bs4 import BeautifulSoup
import subprocess
import sys
import json

cmd=['find','.','-name','*.html','-size','+12k']
#subprocess.call(cmd)
files=subprocess.Popen(cmd,stdout=subprocess.PIPE).communicate()[0].split()

md5s={}
for f in files:
	idx=f[f.rfind('/')+1:-5]
	fin=open(f,'rb')
	soup=BeautifulSoup(fin.read())
	fin.close()
	av={}
	for td_tag in soup.find_all("td",'ltr text-red'):
		tmp=[]
		for child in td_tag.parent.children:
			if child.string.strip()=='':
				continue
			tmp.append(child.string.strip())
		av[tmp[0]]=tmp[1]
	md5s[idx]=av
fout=open('md5_vt_found.json','wb')
fout.write(json.dumps(md5s, indent=2))
fout.close()

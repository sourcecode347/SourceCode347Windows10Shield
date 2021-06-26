# Source Code 347 Windows 10 Shield ( Nikolaos Bazigos )
#https://patorjk.com/software/taag/#p=display&h=3&v=3&f=Small&t=Source%20Code%20347%20%0AWindows%2010%20Shield

MITLicense = '''
MIT License

Copyright (c) 2021 SourceCode347(Nikolaos Bazigos)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

https://github.com/sourcecode347/SourceCode347Windows10Shield
Official Website: https://sourcecode347.com
Youtube Channel: https://youtube.com/sourcecode347
'''

import os,subprocess,sys,random	 
license = '''

  ___                        ___        _       _____ _ ____          
 / __|___ _  _ _ _ __ ___   / __|___ __| |___  |__ | | |__  |         
 \__ / _ | || | '_/ _/ -_) | (__/ _ / _` / -_)  |_ |_  _|/ /          
 ____\______,_|_| \______|  \___\___\____\___| |___/_|_|/_/    _    _ 
 \ \    / (_)_ _  __| |_____ __ _____ / |/  \  / __| |_ (_)___| |__| |
  \ \/\/ /| | ' \/ _` / _ \ V  V (_-< | | () | \__ | ' \| / -_| / _` |
   \_/\_/ |_|_||_\__,_\___/\_/\_//__/ |_|\__/  |___|_||_|_\___|_\__,_|
                                                                      

'''

global AllowedApps , status
AllowedApps = []
status = "Setup"
def reset():
	try:
		os.system("netsh firewall reset")
	except:
		pass
	global status
	status="Unsecure"
	global AllowedApps
	AllowedApps = []
		
def setup():
	reset()
	try:
		os.system("netsh advfirewall set allprofiles firewallpolicy blockinbound,blockoutbound")
	except:
		pass
	global status
	status = "Secure"
	global AllowedApps
	AllowedApps = []
def appAllow(name,path,con):
	global status
	if status=="Unsecure":
		setup()
	output3=""
	output4=""
	if "in" in con:
		try:
			proc = subprocess.Popen("netsh advfirewall firewall add rule name="+name+" dir=in program=\""+path+"\" profile=any action=allow", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
			stdout_value = proc.stdout.read() + proc.stderr.read()
			output3 = stdout_value.decode("utf-8","ignore")
			print(output3)
		except:
			pass
	if "out" in con:
		try:
			proc = subprocess.Popen("netsh advfirewall firewall add rule name="+name+" dir=out program=\""+path+"\" profile=any action=allow", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
			stdout_value = proc.stdout.read() + proc.stderr.read()
			output4 = stdout_value.decode("utf-8","ignore")
			print(output4)
		except:
			pass
	if "Ok" in output3 or "Ok" in output4:
		AllowedApps.append(name)
		if len(AllowedApps) == 1:
			status = " Allowed 1 App or Port"
		else:
			status = " Allowed "+str(len(AllowedApps))+" Apps & Ports"
			
def portAllow(name , port , proto , con):
	global status
	if status=="Unsecure":
		setup()
	output3=""
	output4=""
	if "in" in con:
		try:
			proc = subprocess.Popen("netsh advfirewall firewall add rule name="+name+" dir=in protocol="+proto+" localport="+port+" action=allow", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
			stdout_value = proc.stdout.read() + proc.stderr.read()
			output3 = stdout_value.decode("utf-8","ignore")
			print(output3)
		except:
			pass
	if "out" in con:
		try:
			proc = subprocess.Popen("netsh advfirewall firewall add rule name="+name+" dir=out protocol="+proto+" localport="+port+" action=allow", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
			stdout_value = proc.stdout.read() + proc.stderr.read()
			output4 = stdout_value.decode("utf-8","ignore")
			print(output4)
		except:
			pass
	if "Ok" in output3 or "Ok" in output4:
		AllowedApps.append(name)
		if len(AllowedApps) == 1:
			status = " Allowed 1 App or Port"
		else:
			status = " Allowed "+str(len(AllowedApps))+" Apps & Ports"

def deleteRule(name):
	output3=""
	output4=""
	try:
		proc = subprocess.Popen("netsh advfirewall firewall delete rule name="+name+" dir=in", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
		stdout_value = proc.stdout.read() + proc.stderr.read()
		output3 = stdout_value.decode("utf-8","ignore")
		print(output3)
	except:
		pass
	try:
		proc = subprocess.Popen("netsh advfirewall firewall delete rule name="+name+" dir=out", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
		stdout_value = proc.stdout.read() + proc.stderr.read()
		output4 = stdout_value.decode("utf-8","ignore")
		print(output4)
	except:
		pass
	
	if "Ok" in output3 or "Ok" in output4:
		AllowedApps.remove(name)
		global status
		if len(AllowedApps) == 1:
			status = " Allowed 1 App or Port"
		elif len(AllowedApps) == 0:
			setup()
		else:
			status = " Allowed "+str(len(AllowedApps))+" Apps & Ports"
def executeCMD(cmd):
	try:
		proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
		stdout_value = proc.stdout.read() + proc.stderr.read()
		output3 = stdout_value.decode("utf-8","ignore")
		print(output3)
	except:
		pass			
	
setup()
mlbool = False
cmd = False
while True:
	os.system("cls")
	if mlbool == False:
		print(license)
	if mlbool == True:
		print(MITLicense)
		mlbool = False
	if cmd != False:
		executeCMD(cmd)
		cmd = False
	print("#"*80)
	print(("#"*3)+(" "*3)+"Status : "+status)
	print("#"*80)
	if len(AllowedApps) > 0:
		print(("#"*3)+(" "*3)+"Active Apps & Ports")
		print("#"*80)
		counter=0
		for x in AllowedApps:
			counter+=1
			print(("#"*3)+(" "*3)+str(counter)+") "+x)
		print("#"*80)
	a1 = str(input(" For Setup Enter  : 1 \n For Reset Enter  : 2 \n For Allow App	  : 3 \n For Delete Rule  : 4 \n For Allow Port	  : 5 \n View MIT License : 6 \n Source Code 347>"))
	if a1 == "1":
		setup()
	elif a1 == "2":
		reset()
	elif a1 == "3":
		a2 = str(input("     Enter App Name : "))
		a3 = str(input("     Enter App Path : "))
		a4 = str(input("  Out:1 In:2 both:3 : "))
		if a4=="1":
			con="out"
		elif a4=="2":
			con="in"
		else:
			con="in-out"
		appAllow(a2,a3,con)
	elif a1 == "4":
		a2 = str(input("  Enter App Name : "))
		deleteRule(a2)
	elif a1 == "5":
		a2 = str(input("     Enter Port Name : "))
		a3 = str(input("     Enter LocalPort : "))
		a5 = str(input("Protocol TCP/UDP/ANY : "))
		a4 = str(input("   Out:1 In:2 both:3 : "))
		if a4=="1":
			con="out"
		elif a4=="2":
			con="in"
		else:
			con="in-out"
		portAllow(a2,a3,a5,con)
	elif a1 == "6":
		mlbool = True
	else:
		cmd = a1
# Source Code 347 Windows 10 Shield ( Nikolaos Bazigos )
#https://patorjk.com/software/taag/#p=display&h=3&v=3&f=Small&t=Source%20Code%20347%20%0AWindows%2010%20Shield
# Windows Notification : https://gist.github.com/wontoncc/1808234

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

import os,subprocess,sys,random,sqlite3,time,hashlib  
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
r_args=['-s']
gsetup = False
for arg in range(0,len(sys.argv)):
    if sys.argv[arg]=="-s":
        gsetup=True
#############################################################################
# DATABASE FUNCTIONS
#############################################################################
def sql_connection():
    try:
        con = sqlite3.connect('database.db')
        return con
    except Error:
        print(Error)
def getID(con):
    newid=0
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM AllowedApps ORDER BY id DESC')
    rows = cursorObj.fetchall()
    for row in rows:
        newid = int(row[0])+1
        break
    return newid
def getIDIP(con):
    newid=0
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM blockedIP ORDER BY id DESC')
    rows = cursorObj.fetchall()
    for row in rows:
        newid = int(row[0])+1
        break
    return newid
def sql_table(con):
    try:
        cursorObj = con.cursor()
        cursorObj.execute("CREATE TABLE AllowedApps(id integer PRIMARY KEY,name text, path text, inc text, out text, protocol text)")
        con.commit()
    except:
        pass
    try:
        cursorObj = con.cursor()
        cursorObj.execute("CREATE TABLE Virus(id integer PRIMARY KEY, name text, path text, hash256 text, report text, status text)")
        con.commit()
    except:
        pass
    try:
        cursorObj = con.cursor()
        cursorObj.execute("CREATE TABLE blockedIP(id integer PRIMARY KEY, name text, ip text, inc text, out text)")
        con.commit()
    except:
        pass
def checkDB(con,name):
    cursorObj = con.cursor()
    cursorObj.execute("SELECT * FROM AllowedApps WHERE name='"+name+"'")
    rows = cursorObj.fetchall()
    for row in rows:
        if name == row[1]:
            return True
    return False
def checkDBIP(con,name):
    cursorObj = con.cursor()
    cursorObj.execute("SELECT * FROM blockedIP WHERE name='"+name+"'")
    rows = cursorObj.fetchall()
    for row in rows:
        if name == row[1]:
            return True
    return False
def sql_update(con,name,path,inc,out,proto):
    cursorObj = con.cursor()
    cursorObj.execute("UPDATE AllowedApps SET path = '"+path+"' WHERE name = '"+name+"'")
    cursorObj.execute("UPDATE AllowedApps SET inc = '"+inc+"' WHERE name = '"+name+"'")
    cursorObj.execute("UPDATE AllowedApps SET out = '"+out+"' WHERE name = '"+name+"'")
    cursorObj.execute("UPDATE AllowedApps SET protocol = '"+proto+"' WHERE name = '"+name+"'")
    con.commit()
def deleteFromFaces(con,name):
    cursorObj = con.cursor()
    cursorObj.execute("DELETE FROM faces WHERE name='"+name+"'")
    con.commit()
def insertDB(con,name,path,inc,out,proto):
    cdb = checkDB(con,name,)
    if cdb == True:
        sql_update(con,name,path,inc,out,proto)
    else:
        id = getID(sql_connection())
        cursorObj = con.cursor()
        cursorObj.execute("INSERT INTO AllowedApps VALUES('"+str(id)+"','"+str(name)+"','"+path+"', '"+inc+"', '"+out+"', '"+proto+"')")
        con.commit()
def insertDBIP(con,name,ip,inc,out):
    cdb = checkDBIP(con,name,)
    if cdb == True:
        sql_update(con,name,path,inc,out,proto)
    else:
        id = getIDIP(sql_connection())
        cursorObj = con.cursor()
        cursorObj.execute("INSERT INTO blockedIP VALUES('"+str(id)+"','"+str(name)+"','"+str(ip)+"', '"+str(inc)+"', '"+str(out)+"')")
        con.commit()
def deleteFromDB(con,name):
    cursorObj = con.cursor()
    cursorObj.execute("DELETE FROM AllowedApps WHERE name = '"+str(name)+"'")
    con.commit()
def deleteFromDBIP(con,name):
    cursorObj = con.cursor()
    cursorObj.execute("DELETE FROM blockedIP WHERE name = '"+str(name)+"'")
    con.commit()
def sql_fetch(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM AllowedApps')
    rows = cursorObj.fetchall()
    return rows
def sql_fetchIP(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM blockedIP')
    rows = cursorObj.fetchall()
    return rows
def truncateAllowedApps(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM AllowedApps')
    rows = cursorObj.fetchall()
    for row in rows:
        cursorObj.execute("DELETE FROM AllowedApps WHERE id = '"+str(row[0])+"'")
        con.commit()
def truncateblockedIP(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM blockedIP')
    rows = cursorObj.fetchall()
    for row in rows:
        cursorObj.execute("DELETE FROM blockedIP WHERE id = '"+str(row[0])+"'")
        con.commit()
#############################################################################
# MAIN FUNCTIONS
#############################################################################
def reset():
    try:
        os.system("netsh firewall reset")
    except:
        pass
    global status
    status="Unsecure"
    global AllowedApps
    AllowedApps = []
    try:
        truncateAllowedApps(sql_connection())
    except:
        pass
    try:
        truncateAllowedApps(sql_connection())
    except:
        pass
    try:
        sql_table(sql_connection())
    except:
        pass
def setup():
    reset()
    try:
        os.system("netsh advfirewall set allprofiles firewallpolicy blockinbound,blockoutbound")
    except:
        pass
    try:
        truncateAllowedApps(sql_connection())
    except:
        pass
    try:
        truncateblockedIP(sql_connection())
    except:
        pass
    try:
        sql_table(sql_connection())
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
        inc="0"
        out="0"
        if "Ok" in output3:
            inc="1"
        if "Ok" in output4:
            out="1"
        insertDB(sql_connection(),name,path,inc,out,"0")           
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
        inc="0"
        out="0"
        if "Ok" in output3:
            inc="1"
        if "Ok" in output4:
            out="1"
        insertDB(sql_connection(),name,"0",inc,out,proto)
def blockIP(name , ip , con):
    global status
    if status=="Unsecure":
        setup()
    output3=""
    output4=""
    if "in" in con:
        try:
            proc = subprocess.Popen("netsh advfirewall firewall add rule name="+name+" dir=in action=block remoteip="+str(ip), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            stdout_value = proc.stdout.read() + proc.stderr.read()
            output3 = stdout_value.decode("utf-8","ignore")
            print(output3)
        except:
            pass
    if "out" in con:
        try:
            proc = subprocess.Popen("netsh advfirewall firewall add rule name="+name+" dir=out action=block remoteip="+str(ip), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            stdout_value = proc.stdout.read() + proc.stderr.read()
            output4 = stdout_value.decode("utf-8","ignore")
            print(output4)
        except:
            pass
    if "Ok" in output3 or "Ok" in output4:
        AllowedApps.append(name)
        inc="0"
        out="0"
        if "Ok" in output3:
            inc="1"
        if "Ok" in output4:
            out="1"
        insertDBIP(sql_connection(),name,ip,inc,out)
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
        try:
            deleteFromDB(sql_connection(),name)
        except:
            pass
        try:
            deleteFromDBIP(sql_connection(),name)
        except:
            pass
def killall():
    try:
        proc = subprocess.Popen("netstat -ano | findstr ESTA" , shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        stdout_value = proc.stdout.read() + proc.stderr.read()
        output3 = stdout_value.decode("utf-8","ignore")
        return output3
    except:
        pass  
def exportFW(filename):
    if filename.endswith(".wfw")==False:
        filename=filename+".wfw"
    try:
        proc = subprocess.Popen('netsh advfirewall export "C:/'+filename+'"' , shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        stdout_value = proc.stdout.read() + proc.stderr.read()
        output3 = stdout_value.decode("utf-8","ignore")
        return output3
    except:
        pass
def importFW(filename):
    if filename.endswith(".wfw")==False:
        filename=filename+".wfw"
    try:
        proc = subprocess.Popen('netsh advfirewall import "C:/'+filename+'"' , shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        stdout_value = proc.stdout.read() + proc.stderr.read()
        output3 = stdout_value.decode("utf-8","ignore")
        return output3
    except:
        pass
def executeCMD(cmd):
    try:
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        stdout_value = proc.stdout.read() + proc.stderr.read()
        output3 = stdout_value.decode("utf-8","ignore")
        print(output3)
    except:
        pass
        
######################################################################################
#### Virus Scanner
######################################################################################
def getIDVirus(con):
    newid=0
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM Virus ORDER BY id DESC')
    rows = cursorObj.fetchall()
    for row in rows:
        newid = int(row[0])+1
        break
    return newid
'''    
def sql_table(con):
    try:
        cursorObj = con.cursor()
        cursorObj.execute("CREATE TABLE AllowedApps(id integer PRIMARY KEY,name text, path text, inc text, out text, protocol text)")
        con.commit()
    except:
        pass
    try:
        cursorObj = con.cursor()
        cursorObj.execute("CREATE TABLE Virus(id integer PRIMARY KEY, name text, path text, hash256 text, report text, status text)")
        con.commit()
    except:
        pass'''
def checkDBVirus(con,hash):
    cursorObj = con.cursor()
    cursorObj.execute("SELECT * FROM Virus WHERE hash256='"+hash+"'")
    rows = cursorObj.fetchall()
    for row in rows:
        if hash == row[3]:
            return True
    return False
def sql_updateVirus(con,name,path,hash,report,status):
    cursorObj = con.cursor()
    cursorObj.execute("UPDATE Virus SET path = '"+path+"' WHERE hash256 = '"+hash+"'")
    cursorObj.execute("UPDATE Virus SET report = '"+report+"' WHERE hash256 = '"+hash+"'")
    cursorObj.execute("UPDATE Virus SET status = '"+status+"' WHERE hash256 = '"+hash+"'")
    con.commit()
def insertDBVirus(con,name,path,hash,report,status):
    cdb = checkDBVirus(con,hash)
    if cdb == True:
        sql_updateVirus(con,name,path,hash,report,status)
    else:
        id = getIDVirus(sql_connection())
        cursorObj = con.cursor()
        cursorObj.execute("INSERT INTO Virus VALUES('"+str(id)+"','"+str(name)+"','"+path+"', '"+hash+"', '"+report+"', '"+status+"')")
        con.commit()
def deleteFromDBVirus(con,id):
    cursorObj = con.cursor()
    cursorObj.execute("DELETE FROM Virus WHERE id = '"+str(id)+"'")
    con.commit()
def sql_fetchVirus(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM Virus')
    rows = cursorObj.fetchall()
    return rows
def sql_fetchVirus_Unscanned(con):
    cursorObj = con.cursor()
    cursorObj.execute("SELECT * FROM Virus WHERE status='0'")
    rows = cursorObj.fetchall()
    return rows
def truncateVirus(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM Virus')
    rows = cursorObj.fetchall()
    for row in rows:
        cursorObj.execute("DELETE FROM Virus WHERE id = '"+str(row[0])+"'")
        con.commit()
def hashFile(filename):
    sha256_hash = hashlib.sha256()
    with open(filename,"rb") as f:
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
def virusTotalFree(hash):
    time.sleep(5)
    response = requests.get("https://www.virustotal.com/gui/file/"+str(hash))
    if "No security vendors and no sandboxes flagged this file as malicious" in str(response.text):
        return "Clean"
    else:
        return "Malicius"
######################################################################################
### MAIN CODE
######################################################################################
if gsetup==True:    
    setup()
mlbool = False
cmd = False
rp = []
AllowedApps = sql_fetch(sql_connection())
blockedIPS = sql_fetchIP(sql_connection())
if len(AllowedApps)>0:
    status = "Secure"
ptext = ""
vtext = []
while True:
    os.system("cls")
    AllowedApps = sql_fetch(sql_connection())
    blockedIPS = sql_fetchIP(sql_connection())
    if mlbool == False:
        print(license)
    if mlbool == True:
        print(MITLicense)
        mlbool = False
    if cmd != False:
        executeCMD(cmd)
        cmd = False
    if len(rp)>0:
        for row in rp:
            print("App : "+row[1]+" | Path : "+row[2]+" | In : "+row[3]+" | Out : "+row[4]+" Protocol : "+row[5])
        rp=[]
    if len(ptext)>0:
        print(ptext)
        s=ptext.splitlines()
        for l in s:
            pid = l.find("ESTABLISHED")
            pid+=len(("ESTABLISHED"))
            pid=l[pid:]
            pid=pid.replace(" ","")
            os.system("taskkill /pid "+str(pid)+" /f")
        ptext=""
    if len(vtext)>0:
        vcounter=0
        for row in vtext:
            print(("#"*80))
            print("Name   : "+row[1])
            print("Path   : "+row[2])
            print("Hash   : "+row[3])
            print("Report : "+row[4]+" | Status : "+row[5])
            vcounter+=1
        print(("#"*80))
        print(str(vcounter)+" UnScanned Files")
        vtext=[]
    print("#"*80)
    print(("#"*3)+(" "*3)+"Status : "+status)
    print("#"*80)
    if len(AllowedApps) > 0:
        print(("#"*3)+(" "*3)+"Active Apps & Ports")
        print("#"*80)
        counter=0
        spacelen=25
        spaceone = 0
        spaceid = 0
        for x in AllowedApps:
            counter+=1
            if counter>=10:
                spaceone=1
            if int(x[0])>=10:
                spaceid=1
            space=spacelen-len(x[1])
            print(("#"*3)+(" "*(3-spaceone))+str(counter)+") "+x[1]+(" "*space)+" | Id : "+str(x[0])+(" "*(2-spaceid))+" | In : "+str(x[3])+" | Out : "+str(x[4])+" | Prot. : "+str(x[5]))
        print("#"*80)
    if len(blockedIPS) > 0:
        print(("#"*3)+(" "*3)+"Blocked IP Addresses")
        print("#"*80)
        counter=0
        spacelen=25
        spaceone = 0
        spaceid = 0
        for x in blockedIPS:
            counter+=1
            if counter>=10:
                spaceone=1
            if int(x[0])>=10:
                spaceid=1
            space=spacelen-len(x[1])
            spaceip = 15 - len(x[2])
            print(("#"*3)+(" "*(3-spaceone))+str(counter)+") "+x[1]+(" "*space)+" | Id : "+str(x[0])+(" "*(2-spaceid))+" | IP : "+str(x[2])+(" "*spaceip)+" | In : "+str(x[3])+" | Out : "+str(x[4]))
        print("#"*80)
    a1 = str(input(" For Setup Enter  : 1 \
    \n For Reset Enter  : 2 \
    \n For Allow App    : 3 \
    \n For Delete Rule  : 4 \
    \n For Allow Port   : 5 \
    \n For Block IP     : 6 \
    \n View MIT License : 7 \
    \n View AllowedApps : 8 \
    \n Kill All         : 9 \
    \n Firewall         : 10 \
    \n Virus Scanner    : 11 \
    \n "+("#"*80)+"\n Source Code 347>"))
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
        a3=a3.replace('"',"").replace("'","")
        appAllow(a2,a3,con)
    elif a1 == "4":
        a2 = str(input("  Enter Rule Name : "))
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
        a2 = str(input("     Enter Rule Name  : "))
        a3 = str(input("     Enter IP Address : "))
        a4 = str(input("   Out:1 In:2 both:3  : "))
        if a4=="1":
            con="out"
        elif a4=="2":
            con="in"
        else:
            con="in-out"
        blockIP(a2,a3,con)
    elif a1 == "7":
        mlbool = True
    elif a1 == "8":
        rp = sql_fetch(sql_connection())
    elif a1 == "9":
        ptext=killall()
    elif a1 == "10":
        a2 = str(input("    1 ) Export Settings \n    2 ) Import Settings \n    1 or 2 or Any : "))
        if a2=="1":
            a3=str(input("  Enter a filename : "))
            exportFW(a3)
        if a2=="2":
            a3=str(input("  Enter a filename : "))
            importFW(a3)
    elif a1 == "11":
        print("    List UnScanned Files : 1")
        print("    List Scanned Files   : 2")
        print("    List Detections      : 3")
        print("    Set Critical Path    : 4")
        print("    List Critical Paths  : 5")
        a2 = str(input("    Enter Your Choice : "))
        if a2=="1":
            vtext=sql_fetchVirus_Unscanned(sql_connection())
    else:
        cmd = a1
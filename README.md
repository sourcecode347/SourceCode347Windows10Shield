# SourceCode347 Windows 10 Shield
Windows 10 Shield

<img src="SC347Shield.png" style="width:90%;height:auto;"/>

<br>

<img src="SC347Shield2.png" style="width:90%;height:auto;"/>

# Description

An open source and very powerful shield for Windows 10, written in Python3.

Offers strong security!

It basically blocks every application and every communication and gives you 

the opportunity to choose which application you will allow access to.

# Requirements

Download and install <a href="https://python.org">Python3.*</a>

Don't Forget to check "Add Python to Path" On installation

<h1 style='font-size:24px;'>Don't Forget to Save Your Firewall Settings Before Run <b>Reset or Setup(!)</h1>

# Usage if file is in Desktop

    1) open terminal as administrator and type
    
    2) cd c:/Users/YourName/Desktop
    
    3) python Shield.py
    
    4) Don't Forget to Save Your Default Firewall Settings (Read Below How to do this)

    5) After Step 4 You Can Run a Setup and Allowing Apps & Ports

# Add Rule

    4) type 3 and press enter

    5) type chrome_out and press enter

    6) type the full path of chrome C:\Program Files\Google\Chrome\Application\chrome.exe and press enter

    7) type 1 for outgoing traffic and press enter

* if you want to download files you need incoming and outgoing traffic

# Delete Rule

    8) type 4 and press enter

    9) type the name of Active rule and press enter

# Allow Port

    10 ) type 5 and press enter

    11 ) type the name of Port ex. port22 and press enter
    
    12 ) type the Port ex. 22 and press enter
    
    13 ) type the Protocol ex. TCP and press enter

    14 ) type 1,2 or 3 for incoming, outgoing or 2way traffic

# Block IP

    15 ) type 6 and press enter

    16 ) type the IP as name and press enter

    17 ) type the IP without protocols as IP

    18 ) type 1,2 or 3 for incoming, outgoing or 2way traffic

# Firewal Settings

    19 ) type 10 and press Enter

    20 ) Choose Export Settings and type a filename , the settings saved at C:\ Directory.

    21 ) The filename of saved setting needs the .wfw extension ( example fwSetttings.wfw )

* The Reset option resets all firewall settings

* The Setup option resets all firewall settings and blocks every application and every communication

* You can execute commands as Administrator to see the network statistics and connected ip adresses or domains
   
        netstat -ano | findstr ESTA

# Official Website

<a href="https://sourcecode347.com">SourceCode347.com</a>

# Youtube Channel

<a href="https://youtube.com/sourcecode347">SourcCode347 Youtube Channel</a>

# License
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

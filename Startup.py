import os
import time

def openDropbox():
    try:
        os.startfile('C:\Program Files (x86)\Dropbox\Client\dropbox.exe')

    except Exception as e: print(e)

def closeDropbox():
    try:
        os.system('TASKKILL /F /IM Dropbox.exe')
        
    except Exception as e: print(e)

def openBox():
    try:
        os.startfile('C:\Program Files\Box\Box Sync\BoxSync.exe')

    except Exception as e: print(e)

def closeBox():
    try:
        os.system('TASKKILL /F /IM BoxSync.exe')
        
    except Exception as e: print(e)

def openOutlook():
    try:
        os.startfile('OUTLOOK.exe')

    except Exception as e: print(e)

def openJabber():
    try:
        os.startfile('C:\Program Files (x86)\Cisco Systems\Cisco Jabber\CiscoJabber.exe')

    except Exception as e: print(e)
   
def openVPN():
    try:
        os.startfile('C:\Program Files (x86)\Cisco\Cisco AnyConnect Secure Mobility Client\\vpnui.exe')

    except Exception as e: print(e)

def openChrome():
    try:
        os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')

    except Exception as e: print(e)


openVPN()
time.sleep(30)

openOutlook()
time.sleep(5)

openChrome()
time.sleep(3)

openDropbox()
openBox()
time.sleep(5)

openJabber()
time.sleep(180)

closeDropbox()
time.sleep(2)

closeBox()

exit()



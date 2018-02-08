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

def openInbox():
    try:
        os.startfile('OUTLOOK.exe')

    except Exception as e: print(e)

def openSlack():
    try:
        os.startfile('C:\Users\cdubose\AppData\Local\slack\slack.exe')

    except Exception as e: print(e)
   
def openVPN():
    try:
        os.startfile('C:\Program Files (x86)\Cisco\Cisco AnyConnect Secure Mobility Client\\vpnui.exe')

    except Exception as e: print(e)

def openChrome():
    try:
        os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')

    except Exception as e: print(e)


# openVPN()
# time.sleep(30)

# openOutlook()
# time.sleep(5)

openChrome()
time.sleep(3)

openDropbox()
time.sleep(5)

openSlack()
time.sleep(180)

closeDropbox()
time.sleep(2)

exit()



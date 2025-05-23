s_config = """
[General:Options]
debug = no
scoreReportLocation = /home/ubuntu/Desktop/ScoreReport.html
remoteReportingenabled = no
remoteReportingServer = https://www.nicholaslau.com
remoteReportingRound = CyberTaipan
timeLimit = 150

[00-Forensics:Check_forensics]
enabled = yes
tag  = Forensics
pointValue = 10
parameters = forensic1.txt:302c63ccc99ccf5631abdabdbcc4d372 forensic2.txt:1005 forensic3.txt:phil forensic4.txt:goodluckbreakingthiscode
description = Ex: forensic9.txt:green (Check forensic9.txt for ANSWER: green)
msg = Forensic question %PARAMETER% is correct

[01-RemoveMcPoyle:Remove_users]
enabled = yes
tag = User Management
pointValue = 3
parameters = elmacho
description = Users that should be removed from the system 
msg = Unwanted user %PARAMETER% has been removed: 

[02-AddMacDee:Add_users]
enabled = yes
tag = User Management
pointValue = 1
parameters = norbert mike dave
description = Users that need to be added to the system
msg = New user %PARAMETER% added to system 

[03-GoodUsers:Required_users]
enabled = yes
tag = User Management
pointValue = -10
parameters = kevin bob phil
description = Users that are required on the system
msg = Essential user %PARAMETER% has been removed!

[04-FrankSudo:Add_to_sudo]
enabled = yes
tag = User Management
pointValue = 2
parameters = kevin
description = Users that are required to be Administrators
msg = User %PARAMETER% is now an administrator

[05-DennisNoSudo:Remove_from_sudo]
enabled = yes
tag = User Management
pointValue = 2 
parameters = bob
description = Users that are prohibited from being Administrators
msg = User %PARAMETER% is no longer an administrator

[06-CharlieDeeWebDev:Add_to_group]
enabled = yes
tag = User Management
pointValue = 2
parameters = bob:banana vector:banana
description = Users that are required to be in a group
msg = User %PARAMETER% is now in group

[6A-WebdevGroupCreated:File_now_contains]
enabled = yes
tag = Local Policy
pointValue = 3
parameters = /etc/group:banana
description = Text you would like added to file
msg = Group banana has been created

[07-DisableGuestEtc:Secure_lightdm]
enabled = no
tag = User Management
pointValue = 2
parameters = allow-guest greeter-hide-users greeter-show-manual-login
description = 
msg = Guest account has been disabled

[08-CheckUserPassword: Check_user_password]
enabled = yes
tag = User Management
pointValue = 2
parameters = kevin:MinDays vector:MaxDays gru:NoPassword
description = Ex: username:check. Possible parameters MinDays, MaxDays, NoPassword
msg = Password issue has been fixed: %PARAMETER%

[09-PasswordPolicy:Check_password_policy]
enabled = yes
tag = Account Policy
pointValue = 1
parameters = MinLen:8 Retry:5 Remember:12
description = Possible parameters RejectUsername, EnforceForRoot, LockoutTally, MinLen:#, Retry:#, MaxRepeat:#, Remember:#, UCredit:#, LCredit:#, DCredit:#, DifOk:#, GecosCheck:1
msg = Password policy %PARAMETER% secured

[10-LoginDefs:Secure_login_defs]
enabled = yes
tag = Account Policy
pointValue = 1
parameters = PasswordMaxDays PasswordMinDays LogUnknownFail
description = Possible parameters: PasswordMaxDays, PasswordMinDays, PasswordWarnAge, LogUnknownFail, LogOkLogins, SuLogFile
msg = Account policy has been made more secure by %PARAMETER%

[12-RemoveJohn:Prohibited_packages]
enabled = yes
tag = Unwanted Software
pointValue = 2
parameters = john rkhunter
description = Packages that are not allowed on the system
msg = Unwanted software %PARAMETER% removed

[13-ShieldsUP:Firewall_enabled]
enabled = yes
tag = Defensive Countermeasures
pointValue = 2
parameters = None
description = Make sure the firewall is enabled
msg = Firewall protection has been enabled

[14-SecureSSH:Secure_ssh]
enabled = yes
tag = Application Security
pointValue = 2
parameters = defaultPortChange PermitRootLoginNo Protocol2Only UsePAMyes PermitEmptyPasswordsNo
description = Possible parameters: defaultPortChange, PermitRootLoginNo, Protocol2Only, UsePAMyes, PermitUserEnvironmentNo PermitEmptyPasswordsNo
msg = SSH made more secure by %PARAMETER%

[15-SshApacheRequiredService:Required_services]
enabled = yes
tag = Service Auditing
pointValue = 3
parameters = apache2
description = Services that must be running
msg = Required service %PARAMETER% is running

[16-BadServiceApache2:Prohibited_services]
enabled = yes
tag = Service Auditing
pointValue = 4
parameters = mysql
description = Services that you want stopped
msg = Service %PARAMETER% has been disabled

[17-TurnOnUpdates:Update_settings]
enabled = yes
tag = OS Update
pointValue = 1
parameters = installSecUpdates checkDaily downloadSecUpdates 
description = Possible parameters: installSecUpdates checkDaily, downloadSecUpdates, notifyForLTS, mainRepoEnabled
msg = Update settings have been configured: 

[18-SysCtrlGoodness:Kernel_harden]
enabled = yes
tag = Local Policy
pointValue = 1
parameters = DmesgRestrict CtrlAltDel DisableSendRedirects 
description = Possible Parameters: BlockModLoading, DmesgRestrict, KexecLoadDisabled, UnprivBpfDisabled, CoreUsesPid, CtrlAltDel, SysRq, AllRejectAcceptRedirects, DefRejectAcceptRedirects, AllDisableAcceptSourceRoute, DefDisableAcceptSourceRoute, BootPReplay, Ipv4Forwarding, AllLogMartians, DefLogMartians, McForwarding, ProxyArp, RpFilter, DisableSendRedirects, IgnoreIcmpBroadcast, IgnoreIcmpBogusError, TcpSynCookies, TcpTimestamps, DisableUnprivUserNameSpace
msg = Kernel hardened via %PARAMETER%

[19-ChangePermShadow:Perm_no_longer_equal]
enabled = yes
tag = Uncategorized OS Setting
pointValue = 4
parameters = /etc/shadow:777
description = Ex: /etc/shadow:777 (Change permissions of /etc/shadow away from 777
msg = File permissions on /etc/shadow have been secured

[20-ChangePermSshConfig:Perm_now_equal_to]
enabled = yes
tag = Uncategorized OS Setting
pointValue = 3
parameters = /var/www/html:770
description = Ex: /etc
msg = Directory permissions on /var/www/html have set

[21-RemovePWFile:Bad_file]
enabled = yes
tag = Prohibited File
pointValue = 5
parameters = /home/gru/Desktop/notavirus.dll
description = Files you want removed from the system
msg = Plaintext unauthorized file %PARAMETER% removed

[22-SshLoginBanner:File_now_contains]
enabled = yes
tag = Local Policy
pointValue = 5
parameters = /etc/ssh/sshd_config:^Banner.*
description = Text you would like added to file
msg = Ssh server is now displaying a login banner.

[23-FrankNoPasswdLogin:File_no_longer_contains]
enabled = yes
tag = Local Policy
pointValue = 5
parameters = /etc/group:^nopasswdlogin.*gru.*
description = Text you would like removed from file
msg = User gru no longer allowed to login without password

[24-DennisHasPW:File_no_longer_contains]
enabled = yes
tag = Password Policy
pointValue = 3
parameters = /etc/shadow:bob::.*
description = Text you would like removed from file
msg = User bob has a password

[25-RkhunterCronJob:File_now_contains]
enabled = yes
tag = Local Policy
pointValue = 4
parameters = /var/spool/cron/crontabs/root:^0\s1\s[*]1\s[*]1\s[*]1\s.*rkhunter.*
description = Text you would like added to file
msg = Rkhunter scan being run via cron

[26-HttpFirewallRule:Firewall_rule_exists]
enabled = yes
tag = Defensive Countermeasures
pointValue = 3
parameters = 80
description = Port number that should exist in firewall rules
msg = HTTP traffic is allowed through firewall

[27-CharlieRbase:File_now_contains]
enabled = yes
tag = Local Policy
pointValue = 4
parameters = /etc/passwd:*.vector.*rbash.*
description = Text you would like added to file
msg = User vector has been set to a restricted bash shell

[28-DennisNoSsh:File_now_contains]
enabled = yes
tag = Local Policy
pointValue = 4
parameters = /etc/ssh/sshd_config:^DenyUsers.*phil.*
description = Text you would like added to file
msg = User phil has been denied ssh access.

[29-EtcPasswdRoot:Owned_by_user]
enabled = yes
tag = Local Policy
pointValue = 4
parameters = /etc/passwd:root
description = File must be owned by this user. Format = File:user
msg = User kevin is no longer owner of file /etc/passwd

[30-VarWwwWebdev:Owned_by_group]
enabled = no
tag = Local Policy
pointValue = 3
parameters = /var/www/:banana
description = File must be owned by this group. Format = File:user
msg = Webserver root directory is owned by group banana

[31-RemoveNCListener:Bad_file]
enabled = yes
tag = Prohibited File
pointValue = 5
parameters = /opt/listen.sh
description = Files you want removed from the system
msg = Netcat backdoor removed: %PARAMETER%




"""
import configparser
import subprocess
import time
import Event_checks
import hashlib
import requests
from collections import OrderedDict
import os
import io
import socket
import threading

DEBUG = False
scoreReportLocation = ''
teamIdLocation = '/usr/local/bin/pysel/TEAM'


class Pysel:

    def __init__(self, s_file, team_conf):
        buf = io.StringIO(s_file)
        config_parser = configparser.ConfigParser()
        config_parser.read_file(buf)

       
        team_config = configparser.ConfigParser()
        team_config.read(team_conf)

        self.events = {}
        self.general = {}
        self.team_config = {}
        self.currentScore = 0
        self.possibleScore = 0

        ## Parse team config
        for section in dict(team_config._sections):
            if section == "Team":
                self.team_config[section] = dict(team_config._sections[section])
        ## Parse the config
        for section in dict(config_parser._sections):
            if section == 'General:Options':  ## Look at the general options
                self.general[section] = dict(config_parser._sections['General:Options'])
            else:
                self.events[section] = dict(config_parser._sections[section])
                if self.events[section]['enabled'] == 'yes':
                    if int(self.events[section]['pointvalue']) > 0:
                        self.possibleScore += (int(self.events[section]['pointvalue']) * len(self.events[section]['parameters'].split()))
        self.sortedEvents = OrderedDict(sorted(self.events.items()))
        
        if self.general['General:Options']['debug'] == 'yes':
            global DEBUG
            DEBUG = True
        
    
    def __hash_score__(self, score):
        hashstring = str(score) + 'qwerty'
        hashedval = hashlib.md5(hashstring.encode('utf-8').rstrip())

        return hashedval

    def play_noise(self, file):
        pass
        #subprocess.call(["/usr/bin/aplay", file])
    
    def send_webhook(self, data):
        webhook_url = 'https://script.google.com/macros/s/AKfycbx8-hh2Ive9cm3yqu5XRlNGfYLYtD-jET3j4WuZxWfptAiepHAs_FmYJ3lngIMiNALd/exec'

        try:
            response = requests.post(webhook_url, json=data)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print("Error sending webhook request:", e)
            
    def draw_html_head(self, team, round):
        f = open(self.general['General:Options']['scorereportlocation'], 'w')
        f.write('<!DOCTYPE html><html lang="en">\n<head><title>PySEL Score Report</title><meta http-equiv="refresh" content="40"></head>\n<body><table align="center"><tr><td><div align="center"><H1>Cybersecurity Training</H1><H5>17A</H5></div></td></tr></table><br><hr><br><table border="1"; align="center"><tr><td colspan=3><div align="center"><b>Team: ' + team + '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Round: ' + round + '</b></div></td></tr><tr><td>Pts</td><td>Event</td><td>Tag</td></tr>\n')
        f.close()
#remove initialScore if not working
    def update_html_body(self, score, event, parameter, initialScore, tag):
        if '%PARAMETER%' not in event:
          reportedEvent = event
        else:
          reportedEvent = str(event).replace('%PARAMETER%', parameter)
        if score == 'MISS':
             payload = '<tr bgcolor="lightgray"><td>' + str(score) + '</td><td>' + reportedEvent + '</td><td>' + tag + '</td></tr>'

        else:
            if int(score) < 0:
                payload = '<tr bgcolor="crimson"><td>' + str(score) + '</td><td>' + reportedEvent + '</td><td>' + tag + '</td></tr>'
            else:
                payload = '<tr bgcolor="lightgreen"><td>' + str(score) + '</td><td>' + reportedEvent + '</td><td>' + tag + '</td></tr>'
            
        f = open(self.general['General:Options']['scorereportlocation'], 'a')
        f.write(payload)
        f.write('\n')
        f.close()
        
        
        machine_id = socket.gethostbyname(socket.gethostname())
        imagename = '17A'
        file_path = "/home/ubuntu/Desktop/teamname.txt"
        with open(file_path, "r") as file:
            line = file.readline().replace("\n", "").replace("\r", "").replace(" ", "")
            machine_id2 = line.split(":")[1].split(" ")[0]

        sendout = f"Image: {imagename}\nMachine ID: {machine_id2}\nCurrenttotal: {initialScore}\nScore: {score}\nEvent: {event}\nParameter: {parameter}\nTag: {tag}\nIP: {machine_id}"
#remove Currenttotal:initialScore if not working
        data = {
            'text': sendout
        }
        
        webhook_thread = threading.Thread(target=self.send_webhook, args=(data,))
        webhook_thread.start()


    def get_team_id(self, teamIdLocation):
        if os.path.exists(teamIdLocation):
            f = open(teamIdLocation, 'r')
            team = f.readline()
        else:
            team = '<font color="red">NO TEAM!</font>'
        return (team)


    def draw_html_tail(self, currentScore, totalScore):
        f = open(self.general['General:Options']['scorereportlocation'], 'a')
        payload = '</table><div align="center"><br><H3>Total Score: ' + currentScore + ' out of ' + totalScore + '</H3></div><hr><br>\n<div align="center">Last updated: ' + str(time.ctime()) + '</div></body></html>'
        f.write(payload)
        f.close()
        
        
    def send_notification(self):
        pass


    def start_engine(self):
        timeLeft = int(self.general['General:Options']['timelimit'])
    
        initialScore = 0
        while True:
            self.draw_html_head(self.get_team_id(teamIdLocation), self.general['General:Options']['remotereportinground'])
            self.currentScore = 0
            for name, event in self.sortedEvents.items():
            
            ## parse the parameters list
                if event['enabled'] != "yes":
                    continue
                else:
                    params = event['parameters'].split(' ')
                    for parameter in params:
                        ## Eval the event to call the correct Event_checks function
                        if eval("Event_checks."+name.split(":")[1]+"(parameter)"):
                            print('[X] ',event['pointvalue'], 'pts for',event['tag'], parameter)
                            self.currentScore += int(event['pointvalue'])
                            self.update_html_body(event['pointvalue'], event['msg'], parameter, self.currentScore, event['tag'])

                        else:
                            if DEBUG == True and int(event['pointvalue']) > 0:
                                    self.update_html_body('MISS', event['msg'], parameter, event['tag'])
                                    print("[ ]  0 pts for",event['msg'], parameter)
            

            
            initialScore = self.currentScore
            print('Current score: {} out of {}'.format(self.currentScore, self.possibleScore))
            self.draw_html_tail(str(self.currentScore), str(self.possibleScore))
         

            if self.general['General:Options']['remotereportingenabled'] == "yes":
                url = self.general['General:Options']['remotereportingserver']
                url += "/ss/ss.php?mode=send&game=okcyberrun_r1&team={self.team['team_id']}&player={self.general['General:Options']['remotereportinground']}&score={str(self.currentScore)}&md5={str(self.__hash_score__(self.currentScore))}"
                print('sending', url)
                r = requests.get(url) 
                print(r.status_code, r.text) 

            print('You have', timeLeft, 'minutes remaining.\n\n')
            timeLeft -= 1
            time.sleep(60)
            
 
if __name__ == "__main__":
    Engine = Pysel(s_config, "team.conf")
    
    Engine.start_engine()

from os import system

def editcron(preCmndStr):
    choice = str(input("\nEdit cron for Current User or Other User ([CU]/OU): ").lower() or "cu")
    print()
    if choice in ["ou", "o", "other", "other user", "otheruser"]:
        user = str(input("\nEnter Username: "))
        print()
        while True:
            if user != "":
                print()
                cmnd = "crontab -u {} -e".format(user)
                break
            else: 
                user = str(input("\033[91mPlease Enter Username: "))
                system("tput sgr0")
    else:
        cmnd = "crontab -e"
    system("{} {}".format(preCmndStr, cmnd))

def listcron(preCmndStr):
    choice = str(input("\nList cron for Current User or Other User ([CU]/OU): ").lower() or "cu")
    print()
    if choice in ["ou", "o", "other", "other user", "otheruser"]:
        user = str(input("\nEnter Username: "))
        print()
        while True:
            if user != "":
                print()
                cmnd = "crontab -u {} -l".format(user)
                break
            else: 
                user = str(input("\033[91mPlease Enter Username: "))
                system("tput sgr0")
    else:
        cmnd = "crontab -l"
    system("{} {}".format(preCmndStr, cmnd))

def delcron(preCmndStr):
    choice = str(input("\nDelete cron for Current User or Other User ([CU]/OU): ").lower() or "cu")
    print()
    if choice in ["ou", "o", "other", "other user", "otheruser"]:
        user = str(input("\nEnter Username: "))
        print()
        while True:
            if user != "":
                print()
                cmnd = "crontab -u {} -r".format(user)
                break
            else: 
                user = str(input("\033[91mPlease Enter Username: "))
                system("tput sgr0")
    else:
        cmnd = "crontab -r"
    system("{} {}".format(preCmndStr, cmnd))

def cronversion(preCmndStr):
    cmnd = "crontab -V"
    system("{} {}".format(preCmndStr, cmnd))

def svcRestart(preCmndStr):
    cmnd = "systemctl restart crond"
    system("{} {}".format(preCmndStr, cmnd))

def svcStart(preCmndStr):
    cmnd = "systemctl start crond"
    system("{} {}".format(preCmndStr, cmnd))

def svcStop(preCmndStr):
    cmnd = "systemctl stop crond"
    system("{} {}".format(preCmndStr, cmnd))

def svcStatus(preCmndStr):
    cmnd = "systemctl status crond"
    system("{} {}".format(preCmndStr, cmnd))

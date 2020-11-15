import os
def linux():
     os.system("clear")
     while True:    # while Loop is start For TUI-Linux Basic Operation
      os.system("tput setaf 1")
      os.system(' echo "\t\t\t Welcome To Linux Basic Operatiion \t\t\t [`date +%T `] " ')
      os.system("tput setaf 4")
      print("""                  
      \t1.Show The Date
      \t2.Show Calendar
      \t3.Create a File
      \t4.Check The File 
      \t5.Remove The File
      \t6.Read The File
      \t7.Check The Ip and Network Configuration 
      \t8.RAM status
      \t9.Capture network packets
      \t10.Clear cache
      \t11.Check cpu status
      \t12.Configure yum repos with epel release software
      \t13.Exit From TUI-Linux
      \t14.Go To TUI-Local Page

      """)
      LinuxChoice=input("Plz Enter You Coise:")
      if int(LinuxChoice)== 1:
        os.system('tput setaf 15')
        os.system('date')  # Showing Date / date command
        os.system("tput setaf 4")
      elif int(LinuxChoice) == 2:
        os.system('tput setaf 15')
        os.system('cal')               #showing Calender
        os.system('tput setaf 4')
      elif int(LinuxChoice) == 3:
        FileName=input("Plz Enter The File Name With Location Like (/Desktop/project/sumit.txt):")  # Creating File
        os.system('tput setaf 15')
        os.system('touch ~{0}'.format(FileName))
        os.system('tput setaf 4')
      elif int(LinuxChoice) == 4:
        FileName1=input("Plz Enter The Location Where You Want Check File :")    # Checking The File
        os.system('tput setaf 15')
        os.system('ls ~{0}'.format(FileName1))
        os.system('tput setaf 4')
      elif int(LinuxChoice) == 5:
        FileName2=input("Plz Entre The Location Of File For Delet. Like (/Desktop/project/sumit.txt)")   # Removing The File
        os.system('tput setaf 15')
        os.system('rm ~{0}'.format(FileName2))
        os.system('tput setaf 4')
      elif int(LinuxChoice) == 6:
        FileName3=input("Plz Entre The Location Of File For Read. Like (/Desktop/project/sumit.txt)")    # Reding The File 
        os.system('tput setaf 15')
        os.system('cat ~{0}'.format(FileName3))
        os.system('tput setaf 4')
      elif int(LinuxChoice) == 7:
        os.system('tput setaf 15')
        os.system('ifconfig')
        os.system('tput setaf 4')
      elif int(LinuxChoice)==8:
        os.system('free -m')
      elif int(LinuxChoice)==9:
        os.system('tcpdump')
      elif (LinuxChoice)==10:
        os.system("echo 3> /proc/sys/vm/drop_caches")
      elif (LinuxChoice)==11:
        os.system("ls cpu")
      elif (LinuxChoice)==12:
        os.system("cat /usr/bin/yum")
        os.system("mkdir /etc/yum.repos.d/")
        os.system("cd /etc/yum.repos.d/")
        os.system("sudo dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm")
        os.system("sudo dnf update") #toupdate
        os.system("sudo rpm -qa | grep epel") #toverify
      elif int(LinuxChoice) == 13:      #Exiting From TUI
        os.system('tput setaf 15')
        exit()
      elif int(LinuxChoice) == 14:      #Exiting From TUI-Linux Basic Operation 
        os.system('tput setaf 4')
        break;
      else:
      	print("Input Invalid")

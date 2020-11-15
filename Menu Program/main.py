print(""" Welcome to TUT World 
 -This Project is Implemeted in a python and RHCA
 -TUI is the name of Project. TUT means Terminal User Interface
 -The Project is for the user that doesn't have a knowledge about linux Command,Docke,aws,hadoop.)"""
import os
import getpass
import subprocess
from aws_menu import *
from hadoop import *
from docker import *
from Linux_Basic import *
i=0
while i<=3: 
    i=i+1
    os.system("clear") 
    os.system("tput setaf 1")
    os.system('printf "%75s\n" "WELCOME TO TUI WORLD"')
    os.system("tput setaf 4")
    Pass=getpass.getpass(" Enter Password :")
    if Pass != "g811":
     print("\t\tPassword Is Wrong You Have 3 Attempt.You Use {} Attempt:".format(i))
     input("Press Enter Key To Continue")
     os.system("clear")
     if i == 3:
      os.system("tput setaf 1")
      print("\t\t\tSorry,You Have Only Three Attempt")
      print("\t\t\t\t Try Again ")
      os.system("tput setaf 4")
      exit()
    elif Pass == "g811":
     break;
Location=input(" Enter Where You Want To TUI (local/remote):") # Providing The Option To Uer Where He want to Login
os.system("clear")
if Location == 'local':	# Local-Uer If loop Start
 while True:            # while loop is running for the Local Menu
    # Menu Provide By TUI For A User For Local
    os.system("tput setaf 1")
    os.system(' echo "\t\t\t Welcome To TUI-Local \t\t\t [`date +%T `] " ')
    os.system("tput setaf 4")
    print("""
    \t1.Linux Basic Operation Like(Create File, Remove File, Show Date)

    \t2.Partion Operation

    \t3.Installtion Of Software

    \t4.Networking commands

    \t5.Docker Operation
   
    \t7.Exit From The TUI

    \t8. Creating LVM

    \t9. AWS Operation

    \t10.Hadoop Operation

    \t11.Apache webserver
    """)
    os.system("tput setaf 4")  # Changing The Color of Hedline To Red   
    print("\t\t\t Enter Your Choice:",end='')
    ch=input()

    if int(ch) == 1: # Taking Input From user for Choice
     
      linux()
      LinuxInput=input("\t\tDo You Want Continue? (y/n)")
      if LinuxInput == 'n':
         break; 
      os.system("clear")
      # while Loop of TUI-Linux Basic Operation Is End Here 
 
    elif int(ch) == 2:
     while True:
       os.system('clear')
       os.system("tput setaf 1")
       os.system('echo "\t\t\t Welcome To Partition Operatiion\t\t [`date +%T`]" ')  #Heading Of Partition Menu
       os.system("tput setaf 4")
       print("""
        1.Check The Partion
        2.Create A Partition
        3.Exit From TUI
        4.Go TUI-Menu Page   
       """)
       partitionCh=input("\t\t Enter Your Choice :")
       if int(partitionCh) == 1:
          os.system("tput setaf 15")
          os.system('fdisk -l')
          os.system("tput setaf 4")
       elif int(partitionCh) == 2:
          help1=input("Enter -h To Get Information About Partition : ")
          if help1 =='h':
           os.system("tput setaf 15")
           print("""
		Help:
		  DOS (MBR)
		   a   toggle a bootable flag
		   b   edit nested BSD disklabel
		   c   toggle the dos compatibility flag

		  Generic
		   d   delete a partition
		   F   list free unpartitioned space
		   l   list known partition types
		   n   add a new partition
		   p   print the partition table
		   t   change a partition type
		   v   verify the partition table
		   i   print information about a partition

		  Misc
		   m   print this menu
		   u   change display/entry units
		   x   extra functionality (experts only)

		  Script
		   I   load disk layout from sfdisk script file
		   O   dump disk layout to sfdisk script file

		  Save & Exit
		   w   write table to disk and exit
		   q   quit without saving changes

		  Create a new label
		   g   create a new empty GPT partition table
		   G   create a nefrom test import *w empty SGI (IRIX) partition table
		   o   create a new empty DOS partition table
		   s   create a new empty Sun partition table
		""")
           os.system("tput setaf 4")
           Disk=input(" Enter The Disk Name For Going To inside Like (/dev/sda) :")
           os.system('fdisk {}'.format(Disk))
           os.system("tput setaf 4")
       elif int(partitionCh) == 3:
           os.system('tput setaf 15')
           exit()
       elif int(partitionCh) == 4:
           break; 
       LinuxInput1=input("\t\tDo You Want Continue? (y/n)")
       if LinuxInput1 == 'n':
         break;
       os.system('clear')

    elif int(ch) ==3:
       print("""
        \t 1. Docker
           2. httpd server
        """) # creating the user
       ch=int(input("Enter your Choice"))
       if ch==1:
         dockerSoftware()
       elif ch==2:
         httpdSoftware()
   
    elif int(ch) == 5:
       while True:   # While Loop are starting fo Docker Operation
         #Menu for the Docker Operation
         os.system("clear")
         os.system("tput setaf 1")
         os.system('echo "\t\t\t Welcome To Docker Operation \t\t\t [`date +%T `]" ')   #Heading Of Docker Menu
         os.system("tput setaf 4")
         print("""
         1.Start The Docker Services/Compulsory
	       2.check The No Container are Lanuch
         3.Lanuch New The Docker Container
         4.Downloads The Docker Images
         5.Go Menu Page
         6.Exit From TUI
         7.Docker Sub command
         """)
         os.system("tput setaf 14")
         os.system("echo '\t Note:If You Not Start The Docker Services First Run It Then Use The Other option:'")
         os.system("tput setaf 4")
         print("\t\t\tEnter your choice :",end='')
         os.system("tput setaf 4")
         DockerCh=input()
         os.system("tput setaf 4")
         if int(DockerCh)==1:
            os.system("tput setaf 15")
            os.system("systemctl start docker")  # Starting the Docker Services
            os.system("tput setaf 4")
         elif int(DockerCh)==2:
            os.system("tput setaf 15")
            os.system(" docker ps -a ")     # Checking the Runnig , ShutDown Container(OS)
            os.system("tput setaf 4")
            input(" Enter To Continue")
         elif int(DockerCh)==3:
            ContainerName=input(" Enter the container Name:")
            os.system("docker container run -it --name {} centos:latest".format(ContainerName))  # Lanuching New Container 
            os.system("tput setaf 4")
         elif int(DockerCh)==5:
            os.system("tput setaf 15")
            break;
         elif int(DockerCh)==6:
            os.system("tput setaf 15")
            exit()
         elif int(DockerCh)==7:
            docker()
         else:
           print(" Enter The Write Choice:")
         Forward=input("\t\t\tDo You Want Continue the Docker Operation ? (y/n) ")  # Taking Input for Continue or for Stop Program
         if Forward== 'n' or Forward== 'N' :
               break;
         # While Loop are Ending Of Docker operation

    elif int(ch)==7:
      os.system("tput setaf 15")
      exit()
    
    elif int(ch)==8:
      print("------------------------- DISPLAYING ALL HARDDISK ATTACHED -------------------------")
      print(subprocess.getoutput("fdisk -l"))

      hd1 = input("Enter the first harddisk name : ")

      print("Creating Physical Volume ...")
      print(subprocess.getoutput("sudo pvcreate {}".format(hd1)))
      print("-----PV created-----")
      display = input("Do you want to display created Physical Volume(y/n):")
      if display == "n":
    	  pass
      else:
    	  print(subprocess.getoutput("sudo pvdisplay {}".format(hd1)))
      print("----------------------------------")

      hd2 = input("Enter the second harddisk name : ")

      print("Creating Physical Volume ...")
      print(subprocess.getoutput("sudo pvcreate {}".format(hd2)))
      print("-----PV created--------")
      display = input("Do you want to display created Physical Volume(y/n):")
      if display == "n":
    	  pass
      else:
    	  print(subprocess.getoutput("sudo pvdisplay {}".format(hd2)))
      print("----------------------------------")

      print("Creating VG ...")
      vg = input("Please enter your VG name : ")
      print(subprocess.getoutput("vgcreate {} {} {}".format(vg, hd1, hd2)))

      display = input("Do you want to display created VG(y/n):")
      if display == "n":
    	  pass
      else:
    	  print(subprocess.getoutput("vgdisplay {}".format(vg)))
      print("----------------------------------")

      print("Creating Logical Volume from created VG ...")
      size = input("Please enter size of Logical Volume(LV): ")
      name = input("Please enter name of LV: ")
      print(subprocess.getoutput("lvcreate --size {}G --name {} {}".format(size,name,vg)))
      print("Logical Volume Created ...")
      display = input("Do you want to display created LV(y/n):")
      if display == "n":
    	  pass
      else:
    	  print(subprocess.getoutput("lvdisplay {}/{}".format(vg,name)))
      print("-----------EXITING-----------")
      exit()

    elif int(ch)==9:
      os.system("clear")
      ch=0
      s="yes"
      print("------------------Welcome to AWS!!---------------\n")
      s= input("Do you wish to configure AWS?\n")
      if s.lower()=="yes":
         os.system("aws configure")
         print("AWS is configured")
      while ch!=5:
         print("-----------------AWS MENU---------------")
         ch=0
         print("""
             1.AWS ec2
             2.AWS CloudFront
             3.AWS S3
             4.AWS ebs
             5.Exit\n""")
         ch=int(input("Enter the service\n"))

         if ch==1:
           ec2()
         elif ch==2:
           cloudfront()
         elif ch==3:
           s3()
         elif ch==4:
           ebs()
         else:
           ch=5
    elif int(ch)==10:
      os.system("clear")
      print("\t\t\t------------------Welcome to hadoop!!---------------\n")
      while ch!=5:
         print("\t\t\t\t-----------------Hadoop MENU---------------")
         ch=0
         print("""
             1.create datanode
             2.create namenode
             3.start service
             4.show report
             5.upload file
             6.create a file
             7.remove a file
             8.Stop namenode
             9.Stop datanode
             10.Exit\n""")
         ch=int(input("Enter the service\n"))

         if ch==1:
           core()
         elif ch==2:
           hdfs()
         elif ch==3:
           data()
         elif ch==4:
           os.system("hadoop dfsadmin -report")
         elif ch==5:
           file1=input("Enter file name to be uploaded")
           os.system("Hadoop fs -put {} /".format(file1))
         elif ch==6:
            file2=input("Enter file name to be created")
            os.system("hadoop fs -touchz {}".format(file2))
         elif ch==7:
            file=input('Enter file name with extension to be removed')
            os.system("Hadoop fs -rm /{}/".format(file))
         elif ch==8:
           os.system("sudo hadoop-daemon.sh stop namenode")
         elif ch==9:
           os.system("sudo hadoop-daemon.sh stop datanode")

         else:
           ch=11

    else:
      print(" Choice Write Option")
      os.system("tput setaf 15")

    x=input("\t\t\tDo You Want Continue TUI-Locally ? (y/n) ")  # Taking Input For Continue Or For Stop Program
    if x== 'n' or x== 'N' :
      os.system("tput setaf 15")
      exit()
    os.system("clear")                  # Clearing The Screen For Holding The Menu at Fix Position

# Remote-user Loop is Starting
elif Location == 'remote':
 os.system("tput setaf 1")
 os.system('echo "\t\t\t Welcome To TUI-Remotly \t\t\t [`date +%T`] "')  #Heading Of Remote-Control menu
 os.system("tput setaf 4")
 RemoteUserName=input(" Enter User Name(root/sumit)")
 UserIp=input(" Enter The User Ip Befor Go To Menu :")
 os.system("clear")
 while True:   # While Loop Are Start For Remote TUI
      # Menu Provide By TUI For A User For Remote
      os.system("tput setaf 1")
      print("\t\t\t Welcome To TUI-Remotly")
      os.system("tput setaf 4")
      print("""
      \t1.Ping To User
      \t2.Today Date
      \t3.Show Calendar
      \t4.Create A User
      \t5.Give Me The User Terminal Access 
      \t6.Upload The File
      \t7.Download The File
      \t8.Exit From TUI
      """)
      RemoteChoice=input(" Enter The Choice :")
      if int(RemoteChoice) == 1:       # Ping To Remote Host Machine 
          os.system("ping {}".format(UserIp))
      elif int(RemoteChoice) == 2:     # Running The Date Command On Remote-Host Machine 
          os.system("ssh {0}@{1} date".format(RemoteUserName,UserIp))
      elif int(RemoteChoice) == 3:
          os.system("ssh {0}@{1} cal".format(RemoteUserName,UserIp))
      elif int(RemoteChoice) == 4:      # Creating The User On Remote Host Machine
          UserAdd=input(" Enter The User Name: ")
          os.system("ssh {0}@{1} useradd {2} ".format(RemoteUserName,UserIp , UserAdd))
      elif int(RemoteChoice) == 5:      # Connecting To Remote Host Machine
          os.system("ssh {0}@{1}".format(RemoteUserName,UserIp))
      elif int(RemoteChoice) == 6:      # Uploading The File 
          os.system("tput setaf 14")
          print("\tNote: If You Don`t Know File Name Then  Ref Option-5 And Check File Name")
          os.system("tput setaf 4")
          Option5=input("\tDo you Want to Go To The Option-5 ? (y/n)")
          if Option5 == 'y': 
            os.system("ssh {0}@{1}".format(RemoteUserName,UserIp))      # Connecting To Remote Host Machine
          os.system("tput setaf 4")
          RemoteHostFile=input("Ok Then  Enter The File Name:")          
          os.system("scp /root/Desktop/project/{2} {0}@{1}:/home/sumit/Desktop/".format(RemoteUserName,UserIp,RemoteHostFile))
      elif int(RemoteChoice) == 7:     #Downloading The File 
          os.system("tput setaf 4")
          print("\tNote: If You Don`t Know The File Name  Ref Option-5 And Check File Name")
          Option6=input("\tDo You Want To GO To The Option-5 ? (y/n)")
          if Option6 == 'y':
             os.system("ssh {0}@{1}".format(RemoteUserName,UserIp))
          os.system("tput setaf 4")
          DownloadHostFile=input(" Enter The File Name :")
          os.system("scp {0}@{1}:/home/sumit/Desktop/{2} /root/Desktop/".format(RemoteUserName,UserIp,DownloadHostFile))
      elif int(RemoteChoice) == 8:    # Exit From TUT
          os.system("tput setaf 15")
          exit()
      p=input("Do You Want To Continue TUI-Remotelly ? (y/n)")
      if p == 'n' or p=='N':
         exit() 
      os.system("clear")
      os.system("tput setaf 15")
      # While Loop Is Ending Here 
 

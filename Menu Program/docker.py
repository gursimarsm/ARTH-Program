import os
def docker():
   print("""
\n
Press 1 : To Install a docker 
Press 2 : To pull any image
Press 3 : To check images
Press 4 : To Check runnnig container on docker
Press 5 : To run new Container 
Press 6 : To check all container 
Press 7 : To start a stopped container
Press 8 : To stop a container
Press 9 : To go inside a running container 
Press 10 : To terminate container
Press 11 : To remove container image
Press 12 : Exit the menu  
""")

   ch = input("Enter your choice: ")

   if int(ch) == 1:
      os.system("yum install docker-ce --nobest")
      os.system("systemctl start docker")

   elif int(ch) == 2:
      x = input("Enter image name: ")
      y = input("Enter version: ")
      os.system("docker pull {0}:{1}".format(x,y))

   elif int(ch) == 3:
      os.system("docker images")

   elif int(ch) == 4:
      os.system("docker ps")

   elif int(ch) == 5:
      a = input("Enter Image name: ")
      b = input("Enter version: ")
      c = input("Enter container name: ")
      os.system("docker run -it --name {2} {0}:{1}".format(a,b,c))

   elif int(ch) == 6:
      os.system("docker ps -a")

   elif int(ch) == 7:
      r = input("Enter container name: ")
      os.system("docker start {0}".format(r))

   elif int(ch) == 8:
      u = input("Enter container name: ")
      os.system("docker stop {0}".format(u)) 

   elif int(ch) == 9:
      h = input("Enter container name: ")
      os.system("docker attach {0}".format(h))

   elif int(ch) == 10:
      i = input("Enter container name: ")
      os.system("docker rm {0}".format(i))

   elif int(ch) == 11:
      g = input("Enter image name: ")
      f = input("Enter version")
      os.system("docker rmi {0}:{1}".format(g,f))

   elif int(ch) == 12:
      exit()

   else :
    print("Invalid choice..!!!!!")























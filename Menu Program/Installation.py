def dockerSoftware():
    os.system("tput setaf 15")
    os.system("yum install -y yum-utils")
    os.system("yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo")
    os.system("yum install dokcer-ce --nobest")
    os.system("tput setaf 15")

def httpdSoftware():
    os.system("tput setaf 15")
    os.system("yum install httpd -y") #Installing the Web server
    os.system("tput setaf 4")
#Setting hadoop on remote desktop
c2=input("1. Data Node, 2.Name node: ")
print(c2)
remote_ip=input('Enter the remote IP')
def core():
	print('Enter NameNode IP: ', end='') 
	nn_ip=input()
	os.system ('echo \<configuration\> >> core-site.xml')
	os.system('echo \<property\> >> core-site.xml') 
	os.system("echo \<name\>fs.default.name\<\/name\> >> core-site.xml")
	os.system("echo \<value\>hdfs://{}:9001\<\/value\> >> core-site.xml".format(nn_ip)) 
	os.system('echo <\/property\> >> core-site.xml')
	os.system("echo \<\/configuration\> >> core-site.xml")
	os.system('cp core-site.xml {}:/etc/hadoop/core-site.xml')
	os.system ("rm -rf core-site.xml") 
	os.system("cp temp.xml core-site.xml")

def hdfs():
	if c2=='1':  #Configuring data node
		print('Enter DataNode Directory name for NN : ', end='')
	elif c2=='2': #configuring name node
		print('Enter NameNode Directory you want to create : ', end='')
	dir_name=input()
	os.system('echo \<configuration > >> hdfs-site.xml')
	os.system('echo \<property\> >> hdfs-site.xml')
	if c2=='1':  #Data node
		os.system('echo <name\>dfs.data.dir\<\/name\> >> hdfs-site.xml')
	elif c2=='2': #Name node
		os.system('echo \<name\>dfs.name.dir\<\/name\> >> hdfs-site.xml')
	os.system('echo \<value\>{}\<\/value\> >> hdfs-site.xml'.format(dir_name))
	os.system("echo \</property\> >> hdfs-site.xml")
	os.system('echo \</configuration > >> hdfs-site.xml')
	os.system('cp hdfs-site.xml /etc/hadoop/hdfs-site.xml')
	os.system('rm -rf hdfs-site.xml')
	os.system('cp temp2.xml hdfs-site.xml')

if c2=='2': #Name node code:
	os.system('ssh {} rpm -ivh /root/jdk-8u171-linux-x64.rpm'.format(remote_ip))
	os.system('ssh {} rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force'.format(remote_ip))
	hdfs()
	core()
	os.system('ssh {} hadoop namenode -format'.format(remote_ip))
	os.system("ssh {} hadoop-daemon.sh start namenode".format(remote_ip))
	os.system("ssh {} jps".format(remote_ip))
	
else:
	os.system('ssh {} rpm -ivh /root/jdk-8u171-linux-x64.rpm'.format(remote_ip))
	os.system('ssh {} rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force'.format(remote_ip))
	hdfs()
	core()
	os.system("ssh {} hadoop-daemon.sh start datanode".format(remote_ip))
	os.system("ssh {} jps".format(remote_ip))
	os.system('ssh {} hadoop dfsadmin -report'.format(remote_ip))
import subprocess
import os 
print("------------------------- DISPLAYING ALL HARDDISK ATTACHED -------------------------")
print(subprocess.getoutput("fdisk -l"))

hd1 = input("Enter the first harddisk name : ")

print("Creating Physical Volume ...")
print(subprocess.getoutput("pvcreate {}".format(hd1)))
print("-----PV created-----")
display = input("Do you want to display created Physical Volume(y/n):")
if display == "n":
    pass
else:
    print(subprocess.getoutput("pvdisplay {}".format(hd1)))
print("----------------------------------")

hd2 = input("Enter the second harddisk name : ")

print("Creating Physical Volume ...")
print(subprocess.getoutput("pvcreate {}".format(hd2)))
print("-----PV created--------")
display = input("Do you want to display created Physical Volume(y/n):")
if display == "n":
    pass
else:
    print(subprocess.getoutput("pvdisplay {}".format(hd2)))
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

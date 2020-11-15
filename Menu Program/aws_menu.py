
def ec2():
    a=0
    while a!=8:
        print("-----------------EC2 MENU---------------")
        print("""
             1.Create new instance
             2.Describe instance
             3.Start instance 
             4.Stop an instance
             5.Terminate an instance
             6.Create Security group
             7.Create new key-pair
             8.Exit\n""")
        a=int(input("Enter your choice\n"))

        if a==1:
            print("launching new instance")
            ami = input('AMI ID: ')
            instance_type = input('instance type: ')
            num = input('number: ')
            sg = input('security group: ')
            key = input('key: ')
            print('aws ec2 run-instances --image-id {} --instance-type {} --count {} --security-group-ids {} --key-name {}'.format(ami,instance_type,num,sg,key))
            os.system('aws ec2 run-instances --image-id {} --instance-type {} --count {} --security-group-ids {} --key-name {}'.format(ami,instance_type,num,sg,key))
        elif a==2:
            print("describing instance....")
            print('aws ec2 describe-instances')
            os.system('aws ec2 describe-instances')
        elif a==3:
            print("starting instance....")
            ami = input('Instance ID: ')
            print('aws ec2 start-instances --instance-ids {}'.format(ami))
            os.system('aws ec2 start-instances --instance-ids {}'.format(ami))
        elif a==4:
            print("stopping instance....")
            ami = input('Instance ID: ')
            print('aws ec2 stop-instances --instance-ids {}'.format(ami))
            os.system('aws ec2 stop-instances --instance-ids {}'.format(ami))
        elif a==5:
            print("terminating instance....")
            ami = input('Instance ID: ')
            print('aws ec2 terminate-instances --instance-ids {}'.format(ami))
            os.system('aws ec2 terminate-instances --instance-ids {}'.format(ami))
        elif a==6:
            print("Creating new security group....")
            name = input('name: ')
            desc = input('description: ')
            vpc = input('vcp_id: ')
            print('aws ec2 create-security-group --group-name {} --description {} --vpc-id {}'.format(name,desc,vpc))
            os.system('aws ec2 create-security-group --group-name {} --description {} --vpc-id {}'.format(name,desc,vpc))
        elif a==7:
            print("Creating new key pair....")
            key = input('key')
            print('aws ec2 create-key-pair --key-name {}'.format(key))
            os.system('aws ec2 create-key-pair --key-name {}'.format(key))
        else:
            a=8 
def ebs():
    a=0
    while a!=5:
        print("-----------------EBS MENU---------------")
        print("""
             1.Create ebs
             2.Describe ebs
             3.Attach ebs
             4.Delete ebs
             5.Exit\n""")
        a=int(input("Enter your choice\n"))

        if a==1:
            print(".....Creating new ebs.....")
            vol_type = input('Volume type: ')
            vol_size = input('Volume size: ')
            region = input('Availability zone: ')
            print('aws ec2 create-volume --volume-type {} --size {} --availability-zone {}'.format(vol_type,vol_size,region))
            os.system('aws ec2 create-volume --volume-type {} --size {} --availability-zone {}'.format(vol_type,vol_size,region))
        elif a==2:
            print(".....Describing ebs.......")
            os.system('aws ec2 describe-volumes')
        elif a==3:
            print(".....Attaching ebs........")
            ins_id = input('Instance ID: ')
            vol_id = input('Volume ID: ')
            device = input('Device: ')
            print('aws ec2 attach-volume --instance-id {} --volume-id {} --device {}'.format(ins_id,vol_id,device))
            os.system('aws ec2 attach-volume --instance-id {} --volume-id {} --device {}'.format(ins_id,vol_id,device))
        elif a==4:
            print(".....Deleting ebs........")
            vol_id = input('Volume ID: ')
            os.system('aws ec2 delete-volume --volume-id {}'.format(vol_id))
        else:
            a=5
def s3():
    a=0
    while a!=6:
        print("-----------------S3 MENU---------------")
        print("""
             1.Create bucket
             2.Update acl
             3.delete object 
             4.Delete bucket
             5.List all buckets
             6.Exit\n""")
        a=int(input("Enter your choice\n"))

        if a==1:
            print(".....Creating new bucket.....")
            name = input('bucket name: ')
            region = input('region: ')
            print('aws s3api create-bucket --bucket {} --region {} --create-bucket-configuration LocationConstraint={}'.format(name,region,region))
            os.system('aws s3api create-bucket --bucket {} --region {} --create-bucket-configuration LocationConstraint={}'.format(name,region,region))
        elif a==2:
            print(".....put in bucket.......")
            name = input('bucket name: ')
            key = input('key: ')
            acl= input('acl: ')
            print('aws s3api put-object-acl --bucket {} --key {} --acl {}'.format(name,key,acl))
            os.system('aws s3api put-object-acl --bucket {} --key {} --acl {}'.format(name,key,acl))
        elif a==3:
            print(".....delete object of bucket.......")
            name = input('bucket name: ')
            key = input('key: ')
            print('aws s3api delete-object --bucket {} --key {}'.format(name,key))
            os.system('aws s3api delete-object --bucket {} --key {}'.format(name,key))   
        elif a==4:
            print(".....delete bucket.......")
            name = input('bucket name: ')
            print('aws s3api delete-bucket --bucket {}'.format(name))
            os.system('aws s3api delete-bucket --bucket {}'.format(name))
        elif a==5:
            print(".....list buckets.......")
            print('aws s3 ls')
            os.system('aws s3 ls')
        else:
            a=6

def cloudfront():
    a=0
    while a!=2:
        print("-----------------CLOUDFRONT MENU---------------")
        print("""
             1.Create distribution
             2.Exit\n""")
        a=int(input("Enter your choice\n"))

        if a==1:
            print(".....Creating distribution.....")
            name = input('bucket name: ')
            print('aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com'.format(name))
            os.system('aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com'.format(name))










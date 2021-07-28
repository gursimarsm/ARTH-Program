provider "aws" {
    profile="default"
    region="ap-south-1"
}


# Step 1 : Creating a Key Pair
resource "tls_private_key" "this" {
  algorithm = "RSA"
}

module "key_pair" {
  source = "terraform-aws-modules/key-pair/aws"

  key_name   = "keypair_for_terraform"
  public_key = tls_private_key.this.public_key_openssh
}


# Step 2 : Creating a Security Group
resource "aws_security_group" "sg_for_terraform" {
  name = "sg_for_terraform"
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }


  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  tags = {
    Name = "sg_for_terraform"
  }
}


# Step 3 : Launching an EC2 instance
resource "aws_instance" "terraform" {
    ami = "ami-00bf4ae5a7909786c"
    key_name = "keypair_for_terraform" 
    instance_type = "t2.micro"
    vpc_security_group_ids = [aws_security_group.sg_for_terraform.id]

  connection {
    type     = ssh
    user     = ec2-user
    private_key = var.p_key
    host     = aws_instance.terraform.public_ip
  }
  provisioner "remote-exec" {
    inline = [
      "sudo yum install mysql -y",  
      "sudo amazon-linux-extras install php7.2 -y",
      "sudo yum install httpd -y",
      "sudo wget https://wordpress.org/latest.tar.gz",
      "sudo cp latest* /var/www/html",
      "sudo tar -xvf latest.tar.gz",
      "sudo cp -r wordpress* /var/www/html",
      "sudo systemctl enable httpd --now",
      "sudo mysql -h ${aws_db_instance.default.address} -u ${var.username} -p${var.password} -e 'CREATE DATABASE DBTF;'"
    ]
  }
    tags = {
        Name = "instance_for_terraform"
          }
}


# Step 4 : Creating an EBS Volume
resource "aws_ebs_volume" "volume" {
    availability_zone = aws_instance.terraform.availability_zone
    size = 10
    tags = {
        Name = "ebs_for_terraform"
         }
}


# Step 5 : Attaching volume to instance
resource "aws_volume_attachment" "ebs_att" {
  device_name = "/dev/sdh"
  volume_id   = aws_ebs_volume.volume.id
  instance_id = aws_instance.terraform.id
}


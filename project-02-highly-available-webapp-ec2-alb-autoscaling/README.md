# CloudInfra: EC2 NGINX Deployment using Terraform

This project demonstrates how to provision and configure a web server on AWS using Terraform (Infrastructure as Code).

An EC2 instance is created, configured with IAM (SSM access), secured using Security Groups, and automatically installs NGINX to serve a web page.

---

# Architecture Overview

Terraform → AWS → EC2 → NGINX → Internet

Flow:

1. Terraform provisions infrastructure  
2. EC2 instance is created  
3. IAM role enables secure SSM access (no SSH keys)  
4. Security Group allows HTTP (port 80)  
5. NGINX is installed using user data  
6. Web server is accessible via public IP  

---

# AWS Services Used

- Amazon EC2  
- AWS IAM  
- AWS Systems Manager (SSM)  
- Amazon VPC  
- Security Groups  

---

# Architecture Diagram

![Architecture](architecture.png)

---

# How It Works

## Step 1 — Infrastructure Provisioning

Terraform creates:
- EC2 instance  
- Security Group (HTTP + SSH)  
- IAM Role + Instance Profile  

---

## Step 2 — Secure Access via SSM

Instead of SSH keys, the instance is accessed using:
- AWS Systems Manager (Session Manager)  
- IAM Role with required permissions  

---

## Step 3 — NGINX Installation

Using user_data, the EC2 instance runs:

yum update -y  
amazon-linux-extras install nginx1 -y  
systemctl start nginx  
systemctl enable nginx  

---

## Step 4 — Web Server Live

After deployment:
- Access via public IP  
- Default NGINX page is served  

---

# Terraform Code (main.tf)

provider "aws" {
  region = "us-east-1"
}

data "aws_ami" "amazon_linux" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }
}

resource "aws_security_group" "my_sg" {
  name = "terraform-sg"

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_iam_role" "ssm_role" {
  name = "ec2-ssm-role-new"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Service = "ec2.amazonaws.com"
        }
        Action = "sts:AssumeRole"
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "ssm_attach" {
  role       = aws_iam_role.ssm_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore"
}

resource "aws_iam_instance_profile" "ssm_profile" {
  name = "ec2-ssm-profile-new"
  role = aws_iam_role.ssm_role.name
}

resource "aws_instance" "my_ec2" {
  ami           = data.aws_ami.amazon_linux.id
  instance_type = "t2.micro"

  vpc_security_group_ids = [aws_security_group.my_sg.id]
  iam_instance_profile   = aws_iam_instance_profile.ssm_profile.name

  user_data = <<EOF
#!/bin/bash
yum update -y
amazon-linux-extras install nginx1 -y
systemctl start nginx
systemctl enable nginx
EOF

  tags = {
    Name = "terraform-nginx-instance"
  }
}

---

# Steps to Run

terraform init  
terraform plan  
terraform apply  

---

# Access

 # http://<your-public-ip>

---

# Challenges Faced

- HTTP not working → Fixed via Security Group  
- Subnet issue → Fixed route table  
- SSM not connecting → Fixed IAM role  

---

# Key Learnings

- Terraform basics  
- EC2 provisioning  
- IAM + SSM usage  
- Networking debugging  
- Real-world cloud troubleshooting  

---

# Author

Sudharsan B  
Cloud & DevOps Enthusiast


---


- AWS Systems Manager (SSM)  
- Amazon VPC

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
    Version = "2012-10

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

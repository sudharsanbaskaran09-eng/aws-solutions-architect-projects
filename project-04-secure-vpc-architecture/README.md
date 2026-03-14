## Architecture

![Architecture](Architecture%20image.png)

# 🌐 Secure VPC Architecture on AWS

This project demonstrates how to design a **secure network architecture on AWS** using **Amazon VPC, public and private subnets, Internet Gateway, NAT Gateway, and EC2**.

The architecture isolates application resources inside a **private subnet** while allowing controlled internet access through a **NAT Gateway**, following AWS security best practices.

---

## AWS Services Used

### Amazon VPC
- Created a custom Virtual Private Cloud
- Defined CIDR block for network isolation

### Subnets
- **Public Subnet** – Accessible from the internet
- **Private Subnet** – Securely isolated from direct internet access

### Internet Gateway
- Allows resources in the public subnet to communicate with the internet

### NAT Gateway
- Enables instances in the private subnet to access the internet securely

### Route Tables
- Configured routing rules for public and private subnets

### Amazon EC2
- Launched an instance inside the private subnet to demonstrate secure deployment

---

## Architecture

```
Internet
   ↓
Internet Gateway
   ↓
Public Subnet
   ↓
NAT Gateway
   ↓
Private Subnet
   ↓
EC2 Instance
```

---

## Key Concepts Demonstrated

- Virtual Private Cloud (VPC) networking
- Public and private subnet architecture
- Internet Gateway connectivity
- NAT Gateway for secure outbound internet access
- Route table configuration
- Secure deployment of EC2 instances in private networks

---

## Screenshots

- VPC created  
- Public subnet created  
- Private subnet created  
- Internet gateway attached  
- Public route table configured  
- NAT gateway created  
- Private route table configured  
- EC2 instance launched in private subnet  

---

## Outcome

Successfully built a **secure AWS network architecture** where public resources access the internet through an Internet Gateway, while private resources remain protected and access the internet only through a NAT Gateway.

---

## Author

**Sudharsan B**  
Cloud & DevOps Enthusiast

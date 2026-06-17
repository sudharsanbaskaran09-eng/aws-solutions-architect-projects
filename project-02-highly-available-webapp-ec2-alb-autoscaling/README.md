## Architecture

![Architecture](Architecture%20image.png)

# Highly Available Web Application on AWS

This project demonstrates how to deploy a **highly available and scalable web application on AWS** using **Amazon EC2, Application Load Balancer (ALB), and Auto Scaling**.

The architecture distributes incoming traffic across multiple EC2 instances and automatically launches new instances when needed, ensuring reliability and high availability.

---

## Architecture

```
User
  ↓
Application Load Balancer
  ↓
Auto Scaling Group
  ↓
EC2 Instances
```

---

## Key Concepts Demonstrated

- High Availability Architecture
- Load Balancing with Application Load Balancer
- Automatic scaling of EC2 instances
- Health checks using target groups
- Fault-tolerant infrastructure

---

## Screenshots

- EC2 instance launched  
- Target group created  
- Application Load Balancer configured  
- Auto Scaling Group created  
- Website accessed via ALB DNS

---

## Outcome

Successfully deployed a **highly available web application architecture on AWS**, where traffic is balanced across multiple EC2 instances and the system automatically scales based on demand.

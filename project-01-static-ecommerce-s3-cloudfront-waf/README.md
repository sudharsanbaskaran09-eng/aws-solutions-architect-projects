## Architecture

![Architecture](Architecture%20image.png)

# 🛒 Static E-Commerce Frontend on AWS

This project demonstrates how to deploy a **secure static e-commerce website on AWS** using Amazon S3, CloudFront, and AWS WAF.

The website files are stored in a **private S3 bucket**, delivered globally through **CloudFront CDN**, and protected using **AWS WAF security rules**.

## AWS Services Used

**Amazon S3**
- Stores static website files (HTML, CSS, JS, images)
- Versioning enabled
- Server-side encryption (SSE-S3)
- Public access blocked

**Amazon CloudFront**
- Global CDN for faster content delivery
- HTTPS enabled
- HTTP → HTTPS redirect
- Uses Origin Access Control (OAC) to securely access S3

**AWS WAF**
- Web ACL configured with managed security rules
- Protection against SQL injection, XSS, and common web attacks

## Architecture

User → CloudFront → AWS WAF → Private S3 Bucket

## Key Concepts Demonstrated

- Static website hosting on AWS
- CloudFront edge caching
- Secure S3 access using Origin Access Control
- Web application protection with AWS WAF
- Encryption at rest using SSE-S3

## AWS Certification Concepts

This project covers important topics from the **AWS Solutions Architect Associate (SAA-C03)**:

- Secure architecture (WAF, OAC, encryption)
- High performance architecture (CloudFront CDN)
- Resilient storage (S3 durability and versioning)
- Cost-optimized serverless hosting

## Author

Sudharsan B  
Cloud & DevOps Enthusiast

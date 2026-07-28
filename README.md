# AWS Solutions Architect — Hands‑On Projects
Practical, interview-ready AWS architectures and end-to-end demos built to show real-world solution design, infrastructure-as-code, security posture, and operational runbooks. Ideal for recruiters and hiring managers looking for an AWS Solutions Architect who can design, implement, and operate secure, scalable cloud systems.

Why this repo matters
- 10 focused projects that demonstrate core AWS patterns: static hosting with edge protection, highly-available EC2 fleets, serverless processing & APIs, secure VPC design, monitoring & alerting, CI/CD pipelines, and Terraform-based IaC.
- Each project contains architecture notes, the key services used, and step-by-step instructions to deploy a working demo.
- Hands-on evidence of skills recruiters care about: IaC (Terraform), Lambda/API Gateway, networking (VPC, NAT, IGW), security (IAM, pre-signed S3 URLs, WAF, OAC), observability (CloudWatch, SNS), and CI/CD (CodePipeline / CI patterns).

Quick recruiter summary
- Role fit: AWS Solutions Architect / Cloud Engineer — design + build + secure cloud systems.
- Strengths shown: architecture design, Terraform + AWS service integration, serverless patterns, monitoring & ops readiness, secure file handling, CI/CD automation.
- What you can verify quickly: run any project's README to deploy the demo (requires an AWS account and standard tooling). The projects are small, self-contained, and documented for rapid evaluation.

Project index (one-line + core services)
- project-01-static-ecommerce-s3-cloudfront-waf — Static e-commerce site with S3 + CloudFront + WAF + Origin Access Control (S3, CloudFront, WAF, OAC).
- project-02-highly-available-webapp-ec2-alb-autoscaling — HA web app on EC2 with ALB and Auto Scaling (EC2, ALB, AutoScaling, Session Manager).
- project-03-serverless-image-processing — Event-driven image processing (S3 triggers → Lambda, CloudWatch logs, SNS notifications).
- project-04-secure-vpc-architecture — Secure VPC patterns: private/public subnets, NAT/Igw, routing and network controls (VPC, Subnets, NAT Gateway, IGW, route tables, security groups).
- project-05-Serverless-REST-API — REST API with API Gateway → Lambda → DynamoDB (API Gateway, Lambda, DynamoDB, IAM).
- project-06-Secure-File-Sharing-System — Secure uploads using pre-signed URLs and controlled access flows (S3 presigned URLs, IAM roles/policies, optional Lambda/SSM hooks).
- project-07-Monitoring & Alerting-System — Real-time monitoring, alarms, and automated notifications (CloudWatch metrics & alarms, SNS, Lambda, SSM).
- project-08-Infrastructure-as-Code-Deployment — Terraform examples that provision typical infra stacks and policy/role attachments (Terraform, aws provider, IAM, security groups).
- project-09-CI-CD-Pipeline — CI/CD concepts using AWS Code* services and GitHub integration (CodePipeline, CodeBuild, CodeDeploy, S3 static deploy).
- project-10-Multi-Tier-Web-Architecture — Notes and references for a classic multi-tier (web → app → DB) deployment (RDS/app/web reference).

Stack
- Languages: Terraform (HCL), Python (Lambda), Bash (helper scripts), JSON/YAML (policy and payload samples)
- Runtime / Framework: AWS-native services (Lambda, API Gateway, EC2, S3, CloudFront)
- Notable libraries/tools: boto3 (Python Lambda examples), AWS CLI, Terraform, AWS SAM / Serverless patterns (documented examples)

How the repo is organized
```
README.md                              this overview (proposed)
project-01-static-ecommerce-s3-cloudfront-waf/    static site + CloudFront + WAF demo
project-02-highly-available-webapp-ec2-alb-autoscaling/
project-03-serverless-image-processing/
project-04-secure-vpc-architecture/
project-05-Serverless-REST-API/
project-06-Secure-File-Sharing-System/
project-07-Monitoring & Alerting-System/
project-08-Infrastructure-as-Code-Deployment/
project-09-CI-CD-Pipeline/
project-10-Multi-Tier-Web-Architecture/
```
Each project folder contains a README.md with architecture notes, the services used, and step-by-step deployment instructions. Many projects include small demo code (Lambda handlers, Terraform configs, bash scripts).

How it fits together
- This repo is a portfolio: each project is an independent demonstration of a common production problem and its AWS solution. Patterns repeat across projects (IAM + least privilege, IaC with Terraform, serverless event-driven processing), giving breadth and depth for interview discussions.

Quick start — fastest way to review a working demo
Requirements: Git, AWS CLI configured (credentials & default region), Terraform (for Terraform projects), Python 3 (for local Lambda tests), and an AWS account with permissions to create the described resources.

1) Clone the repo
   git clone https://github.com/sudharsanbaskaran09-eng/aws-solutions-architect-projects.git
   cd aws-solutions-architect-projects

2) Pick a demo and follow its README (recommended order for a quick run)
   - project-08-Infrastructure-as-Code-Deployment — Terraform examples (good to validate IaC skills)
     cd project-08-Infrastructure-as-Code-Deployment
     # Inspect README.md for exact Terraform commands and environment variables
     terraform init
     terraform plan
     terraform apply -auto-approve
   - project-03-serverless-image-processing — S3 → Lambda event-driven flow
     cd ../project-03-serverless-image-processing
     # follow the README to create S3 buckets, deploy the Lambda function, and upload an image to trigger processing
   - project-05-Serverless-REST-API — API Gateway + Lambda + DynamoDB
     cd ../project-05-Serverless-REST-API
     # follow README for API endpoint creation and sample requests

Notes and safety
- Many demos create real AWS resources that may incur cost (EC2, NAT Gateways, RDS). Always review each project's README and teardown steps. Use a dedicated sandbox account and remember to destroy/dismantle resources after testing.

Why this is recruiter‑friendly
- Clear mapping from job responsibilities to repo artifacts (architecture + IaC + code + operational notes).
- Each project is small enough to run for live interviews and rich enough to ask deep design/security/ops questions.
- Demonstrates both design-level thinking and implementation skills with real AWS services.

Want me to:
- Add a one-page walk-through for interviews (one-liner + 5-slide deck) summarizing each project?
- Create GitHub Actions that run lightweight validation or Terraform fmt/validate across the repo?
- Push this README.md into your repo as the root README?

Contact / Author
Sudharsan B — Cloud & DevOps Enthusiast (profile: https://github.com/sudharsanbaskaran09-eng)

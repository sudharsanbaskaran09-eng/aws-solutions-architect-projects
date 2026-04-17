provider "aws" {
  region = "us-east

# IAM Role for SSM
resource "aws_iam_role" "ssm_role" {
  name = "ec2-ssm-role-new"


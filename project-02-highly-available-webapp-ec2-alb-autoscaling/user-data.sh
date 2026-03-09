#!/bin/bash

# Update system packages
yum update -y

# Install Apache web server
yum install httpd -y

# Start Apache service
systemctl start httpd

# Enable Apache to start on boot
systemctl enable httpd

# Create a simple webpage
echo "<h1>Welcome to Sudharsan's Highly Available AWS Web App</h1>" > /var/www/html/index.html

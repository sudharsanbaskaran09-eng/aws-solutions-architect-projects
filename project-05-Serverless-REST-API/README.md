# Serverless REST API on AWS

This project demonstrates how to build a **serverless REST API on AWS** using **Amazon API Gateway, AWS Lambda, and Amazon DynamoDB**.

The API allows users to **create tasks through an HTTP endpoint**. The request is processed by a Lambda function and stored in a DynamoDB table.

---

## Architecture

![Architecture](Architecture%20image.png)

---

## AWS Services Used

### Amazon API Gateway
- Provides a public REST API endpoint
- Handles HTTP requests
- Routes requests to AWS Lambda

### AWS Lambda
- Runs backend code without managing servers
- Processes API requests
- Stores data in DynamoDB

### Amazon DynamoDB
- Fully managed NoSQL database
- Stores tasks created through the API
- Highly scalable and serverless

---

## Architecture Flow

User → API Gateway → Lambda → DynamoDB

1. User sends a **POST request** to API Gateway.
2. API Gateway triggers the **Lambda function**.
3. Lambda processes the request.
4. Data is stored in **DynamoDB**.
5. Lambda returns a response to the user.

---

## Example API Request

POST  
https://your-api-id.execute-api.us-east-1.amazonaws.com/prod/task

### Request Body

```json
{
  "task": "Learn AWS Serverless APIs"
}
```

### Response

```json
{
  "message": "Task created successfully",
  "taskId": "random-id"
}
```

---

## Key Concepts Demonstrated

- Serverless backend architecture
- API development with API Gateway
- Event-driven compute using Lambda
- NoSQL data storage with DynamoDB
- Cloud-native application design

---

## AWS Certification Concepts

This project covers important topics from the **AWS Solutions Architect Associate (SAA-C03)**:

- Serverless architecture
- API Gateway integration with Lambda
- DynamoDB database design
- Secure and scalable cloud applications

---

## Author

Sudharsan B  
Cloud & DevOps Enthusiast

# Secure Serverless File Upload using AWS (Pre-Signed URLs)


```
{
 "Version": "2012-10-17",
 "Statement": [
   {
     "Effect": "Allow",
     "Action": "s3:PutObject",
     "Resource": "arn:aws:s3:::secure-file-upload-sudharsan/*"
   }
 ]
}
```

---

# Testing with Postman

### Step 1 — Generate Pre-Signed URL

```
GET https://<api-id>.execute-api.us-east-1.amazonaws.com/prod/upload
```

Response:

```
{
 "uploadURL": "...",
 "fileName": "example.jpg"
}
```

---

### Step 2 — Upload File

Use PUT request:

```
PUT <uploadURL>
```

Body:

```
binary → image.jpg
```

Expected Response:

```
200 OK
```

The file will now appear in the S3 bucket.

---

# Challenges Faced During Development

### SignatureDoesNotMatch Error

Cause:
Incorrect headers were sent from Postman during file upload.

Fix:
Removed unnecessary headers and ensured the request matched the signed parameters.

---

### Request Expired Error

Cause:
Pre-signed URLs expire after a short time.

Fix:
Generated a new URL before uploading the file.

---

### IAM Permission Error

Cause:
Lambda role did not have permission to upload objects to S3.

Error:

```
is not authorized to perform: s3:PutObject
```

Fix:
Added IAM policy allowing the `s3:PutObject` action.

---

# Key Learnings

- Building serverless architectures
- Secure file uploads using pre-signed URLs
- Managing IAM permissions
- API Gateway and Lambda integration
- Debugging AWS authentication errors
- Understanding request signing in AWS

---

# Future Improvements

Possible enhancements for this project:

- Add authentication using Amazon Cognito
- Store file metadata in DynamoDB
- Add file type validation
- Add file size limits
- Serve files through CloudFront CDN

---

# Author

Sudharsan B  
Cloud & DevOps Enthusiast  
B.E Computer Science Engineering  
Global Institute of Engineering and Technology, Vellore

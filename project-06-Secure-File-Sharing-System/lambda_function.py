import json
import boto3
import uuid

# Create S3 client
s3 = boto3.client('s3')

# Your bucket name
bucket_name = "secure-file-upload-sudharsan"

def lambda_handler(event, context):

    # Generate unique file name
    file_name = str(uuid.uuid4()) + ".jpg"

    # Generate pre-signed URL
    upload_url = s3.generate_presigned_url(
        'put_object',
        Params={
            'Bucket': bucket_name,
            'Key': file_name
        },
        ExpiresIn=300
    )

    # Return response
    return {
        'statusCode': 200,
        'body': json.dumps({
            'uploadURL': upload_url,
            'fileName': file_name
        })
    }

import json

def lambda_handler(event, context):
    
    print("Image uploaded to S3!")
    print("Event:", json.dumps(event))
    
    return {
        'statusCode': 200,
        'body': json.dumps('Image event processed successfully!')
    }

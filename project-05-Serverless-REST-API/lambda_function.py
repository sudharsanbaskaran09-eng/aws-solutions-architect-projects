import json
import boto3
import uuid

# Initialize DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('tasks-table')

def lambda_handler(event, context):

    try:
        body = json.loads(event['body'])
        task = body['task']

        task_id = str(uuid.uuid4())

        table.put_item(
            Item={
                'taskId': task_id,
                'task': task
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Task created successfully',
                'taskId': task_id
            })
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            })
        }

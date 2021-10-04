import json
import boto3

dynamodb = boto3.resource('dynamodb')
s3 = boto3.client('s3')

BUCKET_NAME="meng-quiz"

def lambda_handler(event, context):
    quiz_name=event['quiz_name']
    table = dynamodb.Table(quiz_name)
    
    file_name=quiz_name+".json"
    data = s3.get_object(Bucket=BUCKET_NAME, Key=file_name)
    json_content=json.loads(data['Body'].read().decode('utf-8'))
    
    print(json_content)
    response = table.put_item(
        Item=json_content)
# return a properly formatted JSON object
    return {
        'statusCode': 200,
        'body': "success"
    }

import boto3

s3client = boto3.client('s3')
def lambda_handler(event,context):  
    key = event['Records'][0]['s3']['object']['key']
    print(key)
    obj_path = {'Bucket': 'buckettraining007', 'Key': key}
    s3client.copy_object(Bucket='buckettraining10', Key=key, CopySource=obj_path)


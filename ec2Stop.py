import boto3
region = 'us-east-1'
instances = ['i-05c9fa6c5f821704c']


def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name=region)
    ec2.start_instances(InstanceIds=instances)
    print 'started your instances: ' + str(instances)

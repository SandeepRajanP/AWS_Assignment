import boto3

region = 'us-east-1'
instances = ['i-074c8fcf835d11dd3']

#Start event whose id mentioned
def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name=region)
    ec2.stop_instances(InstanceIds=instances)
    print 'Instances Stop' + str(instances)

import boto3
from datetime import datetime
ec2=boto3.client('ec2')
id = ['i-074c8fcf835d11dd3']

#Check Current Time with start time and stop time mentioned and perform actions accordingly
def checkCurrentTime(starthr,stophr):
	gmtnow = datetime.utcnow()
	Status = ec2.describe_instance_status(InstanceIds = id,IncludeAllInstances=True)
	print Status
	if gmtnow.hour<starthr: 
		if Status['InstanceStatuses'][0]['InstanceState']['Code'] == 16:
			ec2.stop_instances(InstanceIds=id)
	if starthr<=gmtnow.hour:
		if Status['InstanceStatuses'][0]['InstanceState']['Code'] == 80:
			ec2.start_instances(InstanceIds=id)
	if gmtnow.hour<stophr:
		if Status['InstanceStatuses'][0]['InstanceState']['Code'] == 80:
			ec2.start_instances(InstanceIds=id)
	if stophr<=gmtnow.hour:
		if Status['InstanceStatuses'][0]['InstanceState']['Code'] == 16:
			ec2.stop_instances(InstanceIds=id)	
	
def lambda_handler(event,context):	
    #Change Event Rule according to the input from the API Gateway Trigger attached to it
    #The input will be of type Dictionary with 'starthr','startmin' and 'stophr'.'stopmin' as keys
    client = boto3.client('events')
    checkCurrentTime(event['starthr'],event['stophr'])
    starthour = event['starthr']
    startminute = event['startmin']
    response1 = client.put_rule(
		Name='sandeepEC2Start',
		ScheduleExpression= 'cron(%s %s ? * * *)' %(startminute,starthour)
	)
    stophour = event['stophr']
    stopminute = event['stopmin']
    response2 = client.put_rule(
		Name='sandeepEC2Stop',
		ScheduleExpression='cron(%s %s ? * * *)' %(stopminute,stophour)
	)

#Note:API Gateway Name is LambdaScheduler. We can run test by passing the appropriate request



	
	

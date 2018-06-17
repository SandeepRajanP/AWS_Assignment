import boto3


def lambda_handler(event,context):
	client = boto3.client('events')
	#Change the start time and stop time every 12'o clock
	response1 = client.put_rule(
	    Name='sandeepEC2Start',
	    ScheduleExpression='cron(0 9 ? * * *)'
	)
	response2 = client.put_rule(
	    Name='sandeepEC2Stop',
	    ScheduleExpression='cron(0 20 ? * * *)'
	)

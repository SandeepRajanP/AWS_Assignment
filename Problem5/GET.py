import boto3
import json
dynamodb_resource = boto3.resource('dynamodb')

#Python Code for Returning all the items in a DynamoDB
def lambda_handler(event, context):
    # TODO implement
    try:
        TABLENAME = event['queryParams']['table_name']
        table_details=read_table_item(TABLENAME)
        item_count = table_details['Count']
        item_list = table_details['Items']
        for i in range(item_count):
            print item_list[i]
        return item_list
    except Exception as e:
        return e
        
def read_table_item(table_name):
    #Return all items
    table = dynamodb_resource.Table(table_name)
    response = table.scan()
    return response

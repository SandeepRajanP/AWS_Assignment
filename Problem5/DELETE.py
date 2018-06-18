import boto3
from boto3.dynamodb.conditions import Key
dynamodb_resource = boto3.resource('dynamodb')

#Python Code for Lambda function to DELETE OBJECTS IF A PRIMARY KEY IS SPECIFIED
def lambda_handler(event, context):
    # TODO implement
    try:
        TABLENAME = event['queryParams']['table_name']
        table = dynamodb_resource.Table(TABLENAME)
        item = event['body']
        try:
            response = table.get_item(Key=item)
            item1=response['Item']
            exists = True
        except:
            exists = False
        if exists == True: 
            try:
                response = delete_item(TABLENAME,item)
                deleted = True
            except:
                deleted = False
            if deleted == True:
                table_details=read_table_item(TABLENAME)
                item_count = table_details['Count']
                item_list = table_details['Items']
                for i in range(item_count):
                    print item_list[i]
                return item_list
            else:
                return "Error in Deleting"
        else:
            if exists == False:
                return "Key Specified is Missing"
            else:
                return "Error in Input"
    except Exception as e:
        return e
    
def read_table_item(table_name):
    #Return all items
    table = dynamodb_resource.Table(table_name)
    response = table.scan()
    return response 

def delete_item(table_name, pk):
    #Delete an item (row) in table from its primary key.
    table = dynamodb_resource.Table(table_name)
    response = table.delete_item(Key=pk)
    return response

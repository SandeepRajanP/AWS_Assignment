import boto3
from boto3.dynamodb.conditions import Key
dynamodb_resource = boto3.resource('dynamodb')


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
                response = add_item(TABLENAME,item)
                added = True
            except:
                added = False
            if added == True:
                table_details=read_table_item(TABLENAME)
                item_count = table_details['Count']
                item_list = table_details['Items']
                for i in range(item_count):
                    print item_list[i]
                return item_list
            else:
                return "Error in Adding"
        else:
            if exists == False:
                try:
                    response = add_item(TABLENAME,item)
                    added = True
                except:
                    added = False
                if added == True:
                    table_details=read_table_item(TABLENAME)
                    item_count = table_details['Count']
                    item_list = table_details['Items']
                    for i in range(item_count):
                        print item_list[i]
                    return item_list
                else:
                    return "Error in Adding"    
            else:
                return "Error in Input"
    except Exception as e:
        return e
    
def read_table_item(table_name):
    #Return all items
    table = dynamodb_resource.Table(table_name)
    response = table.scan()
    return response 

def add_item(table_name, col_dict):
    #Add one item (row) to table. col_dict is a dictionary {col_name: value}.
    table = dynamodb_resource.Table(table_name)
    response = table.put_item(Item=col_dict)
    return response

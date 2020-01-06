import json


def hello(event, context):
    print(event["body"])
    data = json.loads(event["body"])
    response = {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin":"*"},
        "body": json.dumps(data)
    }
    return response

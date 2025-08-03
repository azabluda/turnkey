import json

def lambda_handler(event, context):
    """
    A simple lambda function that returns a "Hello World" message.
    """
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "message": "Hello from Lambda!"
        })
    }
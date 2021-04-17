import json
import helper
import time
import base64

class Response:
    def __init__(self, requestId: str, timestamp: int, errorMessage: str):
        self.requestId = requestId
        self.timestamp = timestamp
        self.errorMessage = errorMessage

def main(event, context):
    event_json = json.loads(event["body"])
    records = event_json["records"]

    errorMessage = ""
    try:
        records_count = len(records)
        print(f'kinesis recourds count: {records_count}')

        for record in records:
            b64_data = record['data']
            data = base64.b64decode(b64_data).decode('utf-8')
            # print(data)
            helper.set('data', data)
    except Exception as e:
        errorMessage = e

    resp = Response(event_json["requestId"], int(time.time()*1000), errorMessage)

    result = {
        "statusCode": 200,
        "headers": {
            "content-type": "application/json"
        },
        "body": json.dumps(resp, default=lambda obj: obj.__dict__),
        "isBase64Encoded": False
    }

    return result

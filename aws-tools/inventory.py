import boto3
import json
import datetime

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

client =  boto3.client('ec2')

response = client.describe_volumes()

r = json.loads(response)

print (r["VolumeId"])

# print(json.dumps(response, indent=4, default = myconverter))
#!/usr/bin/env python3

import boto3
import json


def getRecords():
    client = boto3.client('route53')
    result=client.list_resource_record_sets(
        HostedZoneId='',
        StartRecordName='testlambda.com.',
        StartRecordType='NS',
    )
    return result

def setDevRecords():
    client = boto3.client('route53')
    result=client.change_resource_record_sets(
    HostedZoneId='',
    ChangeBatch={
        'Comment': 'test',
        'Changes': [
            {
                'Action': 'UPSERT',
                'ResourceRecordSet': {
                    'Name': 'test.testlambda.com.',
                    'Type': 'A',
                    'TTL': 123,
                    'ResourceRecords': [
                        {
                            'Value': '0.0.0.1'
                        },
                    ],
                },
                'ResourceRecordSet': {
                    'Name': 'www.test.testlambda.com.',
                    'Type': 'A',
                    'TTL': 123,
                    'ResourceRecords': [
                        {
                            'Value': '0.0.0.0'
                        },
                    ],
                }
            },
        ]
    }
)
    return print (result)

def prettyJson(list):
    return json.dumps(list, indent=2)


if __name__ == '__main__':
    export=getRecords()
    setDevRecords()

import boto3

hosted_zone=''

route53 = boto3.client('route53')

route53.create_hosted_zone(

Name='testzone',
    VPC={
        'VPCRegion': 'eu-west-1',
        'VPCId': ''
    },
    CallerReference='date',
    HostedZoneConfig={
        'Comment': 'test',
        # 'PrivateZone': True
    }
    # DelegationSetId='string'
)

route53.list_hosted_zones()



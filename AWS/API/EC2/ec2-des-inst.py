#####coding=utf-8
import boto3
#####session
ec2 = boto3.client('ec2')
subnet = ec2.Subent('id')


######设置参数
request = ec2.describe_instances(
'''
    Filters=[
        {
            'Name': 'string',
            'Values': [
                'string',
            ]
        },
    ],
    InstanceIds=[
        'string',
    ],
    DryRun=True,
    MaxResults=123,
    NextToken='string'
'''
)

#######发出请求
print(request)
#####coding=utf-8
import boto3
#####session
ec2 = boto3.client('ec2')
#subnet = ec2.Subent('id')


######设置参数
request = ec2.describe_instances(

    Filters=[
       {
            'Name': 'instance-type',
            'Values': ['t2.micro',]
        },
    ],
    InstanceIds=['i-07abf839463b7fb4b'],
     #MaxResults=5,
    #NextToken='string'
)


#######发出请求
print(request)
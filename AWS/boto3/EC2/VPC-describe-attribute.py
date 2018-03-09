#####coding=utf-8
import boto3
#####session
ec2 = boto3.resource('ec2')
vpc = ec2.Vpc('vpc-30b10257')
#subnet = ec2.Subent('id')


######设置参数
######Describes the specified attribute of the specified VPC. You can specify only one attribute at a time.
request = vpc.describe_attribute(
    Attribute = 'enableDnsSupport',
    #DryRun = True
     #MaxResults=5,
    #NextToken='string'
)
#######发出请求
print(request)
#####coding=utf-8
import boto3
#####session
ec2 = boto3.client('ec2')
#subnet = ec2.Subent('id')


######设置参数
'''
request = ec2.associate_iam_instance_profile(
    IamInstanceProfile={
        'Arn': 'arn:aws:iam::586321868129:instance-profile/Role_EC2_S3',
        'Name': 'Role_EC2_S3'
    },
    InstanceId='i-07abf839463b7fb4b'
)
'''
request1 = ec2.disassociate_iam_instance_profile(
    AssociationId='iip-assoc-059f1bfcc8bd84d0a'
    #InstanceId='i-07abf839463b7fb4b'
)


request2 = ec2.describe_iam_instance_profile_associations()

#######发出请求
reponse=print(request1)
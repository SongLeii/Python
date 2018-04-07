#####coding=utf-8
import boto3
#####session
ec2 = boto3.resource('ec2')
subnet = ec2.Subnet('subnet-27000f61')
print(help(boto3.client))

######设置参数
'''
request = subnet.create_instances(
    BlockDeviceMappings=[
        {
            'DeviceName': '/dev/xvda',
            'VirtualName': 'ebstest',
            'Ebs': {
#                'Encrypted': False,
                'DeleteOnTermination': True,
  #              'Iops': 100,
 #               'KmsKeyId': 'string',
  #              'SnapshotId': 'string',
                'VolumeSize': 10,
                'VolumeType': 'gp2'
            },
#            'NoDevice': 'string'
        },
    ],
    ImageId='ami-68097514',
    InstanceType='t2.micro',
#    Ipv6AddressCount=123,
#    Ipv6Addresses=[
#       {
#            'Ipv6Address': 'string'
#        },
#    ],
#    KernelId='string',
    KeyName='Lei-Pro',
    MaxCount=1,
    MinCount=1,
    Monitoring={
        'Enabled': False
    },
#    Placement={
#        'AvailabilityZone': 'string',
 #       'Affinity': 'string',
 #       'GroupName': 'string',
 #       'HostId': 'string',
 #       'Tenancy': 'default'
 #       'SpreadDomain': 'string'
 #   },
#    RamdiskId='string',
   SecurityGroupIds=[
        'sg-38d70941',
    ],
 #   SecurityGroups=[
 #       'Lei-ssh',
  #  ],
#    SubnetId='subnet-9f050ad9',
#    UserData='string',
#    AdditionalInfo='string',
#    ClientToken='string',
    DisableApiTermination=True,
#    DryRun=True|False,
    EbsOptimized=False,
#    IamInstanceProfile={
#       'Arn': 'arn:aws:iam::586321868129:user/Lei-EC2',
#      'Name': 'Lei-EC2'
#    },
    InstanceInitiatedShutdownBehavior='stop',
#    NetworkInterfaces=[
#        {
#            'AssociatePublicIpAddress': True,
#            'DeleteOnTermination': True,
#            'Description': 'test-interfance',
#            'DeviceIndex': 0,
#            'Groups': [
#                'sg-38d70941',
#            ],
#            'NetworkInterfaceId': 'string',
#            'PrivateIpAddress': 'string',
#            'PrivateIpAddresses': [
#                {
#                    'Primary': True,
#                    'PrivateIpAddress': '192.168.2.12'
#                },
#            ],
#            'SecondaryPrivateIpAddressCount': 123,
#           'SubnetId': 'subnet-9f050ad9'
#        },
#    ],
#    PrivateIpAddress='string',

#    TagSpecifications=[
#        {
#            'ResourceType': 'customer-gateway'|'dhcp-options'|'image'|'instance'|'internet-gateway'|'network-acl'|'network-interface'|'reserved-instances'|'route-table'|'snapshot'|'spot-instances-request'|'subnet'|'security-group'|'volume'|'vpc'|'vpn-connection'|'vpn-gateway',
#            'Tags': [
#                {
#                    'Key': 'string',
#                    'Value': 'string'
#                },
#            ]
#        },
#    ],
#    CreditSpecification={
#        'CpuCredits': 'string'
#    }
)
#######发出请求
print(request)
'''
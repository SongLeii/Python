#########coding=utf-8

import boto3
#####session
ec2 = boto3.client('ec2')
#subnet = ec2.Subent('id')

######request  to start the instance if it has stoped or else stop the instance
ins_id = 'i-07abf839463b7fb4b'

status = ec2.describe_instances(InstanceIds=[ins_id])
print(type(status))
#print(status[1])

#print(type(d1))

def instance_start_stop():
    if  str('stopped') in str(status):
       ec2.start_instances(
            InstanceIds=[ins_id,],
#            AdditionalInfo='None',
            DryRun=False
        )
    else:
        ec2.stop_instances(
            InstanceIds=[ins_id,],
 #           AdditionalInfo='None',
            DryRun=False
        )
######response
if __name__ == '__main__':
    instance_start_stop()

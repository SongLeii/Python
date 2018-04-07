######coding=utf-8
import boto3 # to import boto3 library
ec2 = boto3.resource('ec2', region_name='ap-southeast-1') # call ec2 recourse to perform further actions
instances = ec2.instances.all()  # get all instances from above region
for instance in instances:
  print("Instance id ", instance.id)
  print("Instance public IP  ", instance.public_ip_address)
  print("Instance private IP ", instance.private_ip_address)
  print("------------------------")

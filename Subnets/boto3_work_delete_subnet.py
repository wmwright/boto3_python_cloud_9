import boto3

subnet_id = 'subnet-065d94e3a01435827'

ec2 = boto3.client('ec2')

ec2.delete_subnet(
    SubnetId=subnet_id,
)

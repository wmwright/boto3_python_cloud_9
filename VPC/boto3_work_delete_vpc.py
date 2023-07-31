import boto3

vpc_id = 'vpc-05a9db06accb24178'

ec2 = boto3.client('ec2')

ec2.delete_vpc(
    VpcId=vpc_id,
)
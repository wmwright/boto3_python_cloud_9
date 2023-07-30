import boto3

internet_gateway_id = "igw-098310d7eca5f0353"
vpc_id = "vpc-05a9db06accb24178"

ec2 = boto3.client('ec2')

ec2.detach_internet_gateway(
    InternetGatewayId=internet_gateway_id,
    VpcId=vpc_id,
)
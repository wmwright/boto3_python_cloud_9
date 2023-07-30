import boto3

internet_gateway_id = "igw-098310d7eca5f0353"

ec2 = boto3.client('ec2')

ec2.delete_internet_gateway(
    InternetGatewayId=internet_gateway_id,
)
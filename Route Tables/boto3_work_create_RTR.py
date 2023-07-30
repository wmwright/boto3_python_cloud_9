import boto3

route_table_id = "rtb-08b6bafb3d6336a63"
internet_gateway_id = "igw-098310d7eca5f0353"

ec2 = boto3.client('ec2)')

ec2.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=internet_gateway_id,
    RouteTableId=route_table_id,
)

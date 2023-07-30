import boto3

route_table_id = 'rtb-08b6bafb3d6336a63'

ec2 = boto3.client('ec2')

ec2.delete_route_table(
    RouteTableId=route_table_id,
)
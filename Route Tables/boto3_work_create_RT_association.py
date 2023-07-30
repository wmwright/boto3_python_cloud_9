import boto3

route_table_id = 'rtb-08b6bafb3d6336a63'
subnet_id = 'subnet-065d94e3a01435827'

ec2 = boto3.client('ec2')

association = ec2.associate_route_table(
    RouteTableId=route_table_id,
    SubnetId=subnet_id,
)

print(association["AssociationId"])
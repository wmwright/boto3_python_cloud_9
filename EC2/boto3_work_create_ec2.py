import boto3

ami_id = ""
key_pair_name = ""
security_group_id = ""

ec2 = boto3.client('ec2')

response = ec2.run_instances(
    ImageId=ami_id,
    InstanceType='t2.micro',
    KeyName=key_pair_name,
    MaxCount=1,
    MinCount=1,
    SecurityGroupIds=[
        security_group_id
    ]
)

print(response)
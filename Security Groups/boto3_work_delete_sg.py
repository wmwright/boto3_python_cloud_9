import boto3

ec2 = boto3.client('ec2')

response = ec2.delete_security_group(
    GroupId='sg-0cbbd2ed44750a7a0',
)

print(response)
import boto3

ec2 = boto3.client('ec2')

response = ec2.create_image(
    InstanceId='i-1234567890abcdef0',
    Name='My server',
)

print(response["ImageId"])
import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_instances_type(
    Filters=[
        {
            'Name': 'free-teir-eligible',
            'Values': [
                'true',
            ]
        },
    ],
    
    )

for instanceType in response["InstanceTypes"]:
    print(instanceType["InstanceType"], instanceType["FreeTierEligible"])
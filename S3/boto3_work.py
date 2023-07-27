import boto3

s3 = boto3.client('s3')

response = s3.create_bucket(
    Bucket='wwright-boto3-07242023'
    )
    
print(response)
import boto3

s3 = boto3.client('s3')

response = s3.list_objects_v2(Bucket="wwright-boto3-07242023")

for content in response["Contents"]:
    if(".txt" in content["Key"]):
        print(content["Key"])
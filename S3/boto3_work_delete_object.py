import boto3

bucket = "wwright-boto3-07242023"
key = "test_text_sting.txt"

s3 = boto3.client('s3')

response = s3.delete_object(
    Bucket=bucket,
    Key=key,
    
)
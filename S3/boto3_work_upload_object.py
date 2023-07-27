import boto3

s3 = boto3.client('s3')

s3.put_object(Bucket="wwright-boto3-07242023", Key="test_text.txt", Body="Hey this is a string", ContentType="text/plain")
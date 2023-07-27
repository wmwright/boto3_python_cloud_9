import boto3

def empty_bucket(client, bucket):
    response = client.list_objects_v2(Bucket=bucket)
    
    if "Contents" in response:
        objects = [{'Key': content["Key"]} for content in response["Contents"]]
        
        response = client.delete_objects(
            Bucket=bucket,
            Delete={
                'Objects':objects
            }
        )
        
        while repsonse.get("NextContinuationToken"):
            response = client.list_objects_v2(Bucket=bucket,
                            ContinuationToke=response["NextContinuationToken"])
                            
            objects = [{'Key': content["Key"]} for content in response["Contents"]]
                
            response = client.delete_objects(
                Bucket=bucket,
                Delete={
                    'Objects':objects
            }
        )   

s3 = boto3.client('s3')

bucket = "wwright-boto3-07242023"

empty_bucket(s3, bucket)


import json
import logging
import boto3
import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
instace_list = []
ec2 = boto3.resource('ec2')
mytime = datetime.datetime.now().hour
s3=boto3.resource("s3")
s3g = boto3.client("s3")
bucket_name = "chen-instance-bucket"
 
def lambda_handler(event, context):
    # TODO implement
    logger.info(f"Got Event: {event}")
    mybucket = s3.Bucket(bucket_name)
    if len(event['detail'])>0:
        instance_id=event['detail']['instance-id']
        instace_list.append(instance_id)
        s3.Bucket(bucket_name).put_object(Key=instance_id,Body="111")
    if "Contents" in s3g.list_objects(Bucket=bucket_name):
        ids=s3g.list_objects(Bucket=bucket_name)['Contents']
        for item in ids:
            ins = item['Key']
            try:
                tag = ec2.Instance(ins).tags
                instance = ec2.Instance(ins)
                if tag[0]['Key']=="chen_ec2" and mytime==20:
                    response = instance.stop()
            except :
                logger.info("error")
            if mytime==20:
                response = mybucket.delete_objects(
                    Delete={'Objects': [{'Key': ins,},],},) 
# Automatic-Stopping-Instance-AWS

Detecting my running EC2 instances and stopping them automatically with lambda function.

## Primary Usage

- Detect instance launches

- Make sure the EC2 Instances would not incur costs

- Terminate only the specifically tagged Instances

## Components & Libraries

- AWS Cloudwatch

- AWS Lambda

- AWS IAM role

- boto3

- json

- AWS S3

## Procedure

* Capture the action where an Instance is launched by detecting state change along with instance running tag.

* Write the instance id to S3 bucket.

* Check if the lambda function is triggered by time hitting 17:00. If so , read the list of instances from S3 bucket. 

* Go through the list to see if a given instance has specific tag that signals it is my instance. If so, stop the instance. 

* Clear the S3 bucket. 

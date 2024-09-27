import json
import boto3

# Initialize the Glue client
glue = boto3.client('glue')

def lambda_handler(event, context):

    # Extract bucket name and object key from the event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']
    
    # Define the folder prefixes and corresponding crawler names
    folder_prefix_1 = 'folder_for_dim_flipkart/'
    folder_prefix_2 = 'folder_for_fact_flipkart/'
    
    glueJobName1 = 'GlueJobFordim'
    glueJobName2 = 'GlueJobForFact'

    # Check which folder prefix the object key matches and trigger the appropriate crawler
    
    if object_key.startswith(folder_prefix_1):
        glue.start_job_run(JobName = glueJobName1)
        
    elif object_key.startswith(folder_prefix_2):
        glue.start_job_run(JobName = glueJobName2)


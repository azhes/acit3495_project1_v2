import boto3
import yaml
from app import app

def download_video(filename):
    with open('upload_config.yaml', 'r') as f:
            s3_config = yaml.safe_load(f.read())

    aws_access_key_id = s3_config['upload']['aws_access_key_id']
    aws_secret_access_key = s3_config['upload']['aws_secret_access_key']

    s3_client = boto3.client("s3")

    s3_bucket_name = "acit3495-filestorage"

    prefix = ''

    response = s3_client.list_objects(Bucket=s3_bucket_name, Prefix=prefix)
    for file in response['Contents']:
        name = file['Key']
        print(name)
        if name == filename:
            s3_client.download_file(s3_bucket_name, name, filename)

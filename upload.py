import boto
import boto3
import yaml

def upload_video_file(filename):

    with open('upload_config.yaml', 'r') as f:
        s3_config = yaml.safe_load(f.read())

    aws_access_key_id = s3_config['upload']['aws_access_key_id']
    aws_secret_access_key = s3_config['upload']['aws_secret_access_key']

    s3 = boto3.client("s3", aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

    s3.upload_file(
        filename,
        Bucket="acit3495-filestorage",
        Key=filename
    )
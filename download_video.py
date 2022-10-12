import boto3
import yaml
from app import app

def download_video(filename):
    with open('upload_config.yaml', 'r') as f:
            s3_config = yaml.safe_load(f.read())

    aws_access_key_id = s3_config['upload']['aws_access_key_id']
    aws_secret_access_key = s3_config['upload']['aws_secret_access_key']

    s3_client = boto3.client("s3", aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

    s3_bucket_name = "acit3495-filestorage"

    prefix = ''

    response = s3_client.list_objects(Bucket=s3_bucket_name, Prefix=prefix)
    for file in response['Contents']:
        name = file['Key']
        print(name)
        if name == filename:
            s3_client.download_file(s3_bucket_name, name, f'{filename}')

# download_video('static/uploads/Y2Mate.is_-_The_Dark_Side_of_the_Force_is_a_pathway_to_many_abilities_some_consider_to_be_unnatural.-jIHF8Xe-O6Y-1080p-1655537488690.mp4')
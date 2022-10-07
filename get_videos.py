import boto3
import yaml

def get_videos():

    with open('upload_config.yaml', 'r') as f:
        s3_config = yaml.safe_load(f.read())

    aws_access_key_id = s3_config['upload']['aws_access_key_id']
    aws_secret_access_key = s3_config['upload']['aws_secret_access_key']

    s3_client = boto3.client("s3")

    s3_bucket_name = "acit3495-filestorage"

    s3 = boto3.resource('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

    bucket = s3.Bucket(s3_bucket_name)

    videos_list = []

    for file in bucket.objects.filter(Prefix=''):
        video_name = file.key[15:]
        videos_list.append(video_name)

    return videos_list    
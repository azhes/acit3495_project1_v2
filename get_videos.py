import boto3
import yaml
import mysql.connector

def get_videos():

    # with open('upload_config.yaml', 'r') as f:
    #     s3_config = yaml.safe_load(f.read())

    # aws_access_key_id = s3_config['upload']['aws_access_key_id']
    # aws_secret_access_key = s3_config['upload']['aws_secret_access_key']

    # s3_client = boto3.client("s3")

    # s3_bucket_name = "acit3495-filestorage"

    # s3 = boto3.resource('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

    # bucket = s3.Bucket(s3_bucket_name)

    # videos_list = []

    # for file in bucket.objects.filter(Prefix=''):
    #     video_name = file.key[15:]
    #     videos_list.append(video_name)

    with open('db_config.yaml', 'r') as f:
        db_config = yaml.safe_load(f.read())

    hostname = db_config['datastore']['hostname']
    username = db_config['datastore']['user']
    current_database = db_config['datastore']['db']
    portnumber = db_config['datastore']['port']
    pw = db_config['datastore']['password']

    db = mysql.connector.connect(host=hostname, user=username, database=current_database, port=portnumber, password=pw)

    mycursor = db.cursor()

    videos_list = []

    sql = "SELECT path FROM videos;"

    mycursor.execute(sql)

    videos = mycursor.fetchall()

    for video in videos:
        videos_list.append(video)

    return videos_list
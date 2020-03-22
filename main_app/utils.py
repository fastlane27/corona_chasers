import uuid
import boto3

S3_BASE_URL = 'https://s3-us-east-2.amazonaws.com/'
BUCKET = 'coronachaser'
SESSION = boto3.Session(profile_name='coronachaser')


def upload_file(file):
    s3 = SESSION.client('s3')
    key = uuid.uuid4().hex[:6] + file.name[file.name.rfind('.'):]
    s3.upload_fileobj(file, BUCKET, key)
    url = f'{S3_BASE_URL}{BUCKET}/{key}'
    return url

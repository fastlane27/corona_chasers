import uuid
import boto3

S3_BASE_URL = 'https://s3-us-east-2.amazonaws.com/'
BUCKET = 'coronachaser'
SESSION = boto3.Session(profile_name='coronachaser').client('s3')


def upload_file(file):
    key = uuid.uuid4().hex[:6] + file.name[file.name.rfind('.'):]
    SESSION.upload_fileobj(file, BUCKET, key)
    url = f'{S3_BASE_URL}{BUCKET}/{key}'
    return url


def delete_file(url):
    key = url.rsplit('/', 1)[-1]
    SESSION.delete_object(Bucket=BUCKET, Key=key)
    return

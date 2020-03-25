import uuid
import boto3

S3_BASE_URL = 'https://s3-us-east-2.amazonaws.com/'
BUCKET = 'coronachaser'


def upload_file(file):
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + file.name[file.name.rfind('.'):]
    s3.upload_fileobj(file, BUCKET, key)
    url = f'{S3_BASE_URL}{BUCKET}/{key}'
    return url


def delete_file(url):
    s3 = boto3.client('s3')
    key = url.rsplit('/', 1)[-1]
    s3.delete_object(Bucket=BUCKET, Key=key)
    return

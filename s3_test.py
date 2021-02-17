import boto3
import logging
import os

from boto3.session import Session

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

for name in ["boto3", "s3transfer", "urllib3"]:
    logging.getLogger(name).setLevel(logging.INFO)

BUCKET_NAME = os.getenv('BUCKET_NAME_ENV', default='bucket-name')
KEY = "test.txt"
UPLOAD_FILE = "test/" + KEY
DOWNLOAD_FILE = "S3_" + KEY

profile = 'default'
session = Session(profile_name=profile)

# Let's use Amazon S3
s3 = session.resource('s3')
bucket = s3.Bucket(BUCKET_NAME)

# Print out bucket names
print('## Existing buckets:')
for bucket_list in s3.buckets.all():
    print(bucket_list.name)

# Upload a new file
print('## Upload a new file:')
print('## Target Bucket is ' + bucket.name)

bucket.upload_file(KEY,UPLOAD_FILE,ExtraArgs={'ACL': 'public-read'})
obj = bucket.Object(UPLOAD_FILE)
print('## Upload File is ' + obj.key)

print('## Object List :')
for obj_list in bucket.objects.all():
    print(obj_list)

# Download file
bucket.download_file(UPLOAD_FILE,DOWNLOAD_FILE)
print('## Download File is ' + DOWNLOAD_FILE)
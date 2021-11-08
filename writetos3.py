import boto3
import os
from secrets import ACCESS_KEY_ID, SECRET_ACCESS_KEY

s3 = boto3.resource(
    service_name='s3',
    region_name='us-east-1',
   aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=SECRET_ACCESS_KEY
)

import time

now = time.time()

with open(f"file_{now}.txt", "w") as f:
    f.write(f"Hello world at {now}")

s3.Bucket('moritz-demo-bucket').upload_file(f"file_{now}.txt", f"file_{now}.txt")

os.remove(f"file_{now}.txt")

with open("skip_shutdown.txt", "r") as f:
    skip_shutdown = f.read()
    
if not "yes" in skip_shutdown:
    os.system("sudo shutdown now -h")
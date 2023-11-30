import os
import glob
import boto3
from botocore.exceptions import NoCredentialsError
from dotenv import load_dotenv
from sys import platform

load_dotenv()

# AWS S3 settings
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')
BUCKET_NAME = os.getenv('BUCKET_NAME')

# Find .als files in the system
def find_als_files():
    files = []
    # Check operating system
    if platform == "win32": # For Windows
        drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
        for drive in drives:
            files.extend(glob.glob(drive + '/**/*.als', recursive=True))
    else: # For macOS and Linux
        files.extend(glob.glob('/**/*.als', recursive=True))

    return files

# Upload file to S3
def upload_to_s3(file_name, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY,
                      aws_secret_access_key=AWS_SECRET_KEY)

    try:
        s3.upload_file(file_name, bucket, s3_file)
        print(f"Upload Successful: {s3_file}")
    except FileNotFoundError:
        print(f"The file was not found: {file_name}")
    except NoCredentialsError:
        print("Credentials not available")



def main():
    als_files = find_als_files()
    for file in als_files:
        upload_to_s3(file, BUCKET_NAME, os.path.basename(file))

if __name__ == "__main__":
    main()


#TODO Tracking File Modifications
#Comparing Modification Times
#Scheduling the Script




import logging
import boto3
from botocore.exceptions import ClientError
import os


s3 = boto3.client("s3")

# ### read buckets

# response = s3.list_buckets()

# # Output the bucket names
# print("Existing buckets:")
# for bucket in response["Buckets"]:
#     print(f'  {bucket["Name"]}')


### upload file


def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client("s3")
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def download_file(file_name, bucket_name, object_name):
    s3 = boto3.client("s3")
    with open(file_name, "wb") as f:
        s3.download_fileobj(bucket_name, object_name, f)


download_file("new_downloaded_azure.py", "test-sda-Flavian", "azure.py")

# upload_file(
#     "/home/flavi/SDA/devops_python_scripting/azure_blob.py",
#     "test-sda-Flavian",
#     "azure.py",
# )

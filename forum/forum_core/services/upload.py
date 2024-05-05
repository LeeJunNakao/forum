import boto3
from uuid import uuid4
from botocore.exceptions import ClientError
import os


def upload_file(file, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # Upload the file
    s3_client = boto3.client('s3')
    file_uuid = uuid4()
    object_name = object_name or file.name
    object_name = f"{file_uuid}-{object_name}"

    try:
        bucket_name = os.environ.get("FILES_BUCKET")
        s3_client.upload_fileobj(file, bucket_name, object_name)
        public_url = f"{s3_client.meta.endpoint_url}/{bucket_name}/{object_name}"

        return True, public_url
    except ClientError as e:
        return False, ''
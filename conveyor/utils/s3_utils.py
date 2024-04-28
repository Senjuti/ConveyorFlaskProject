import logging
import boto3

from botocore.exceptions import ClientError

from conveyor.config import region

log = logging.getLogger(__name__)


def init_s3_resource():
    # boto3.resource('s3') will allow you to perform High level API calls
    return boto3.resource('s3', region_name=region)


def init_s3_client():
    #  boto3.client('s3') will allow you to perform Low level API calls
    return boto3.client('s3', region_name=region)


def list_buckets():
    s3_resource = init_s3_resource()
    buckets = [bucket.name for bucket in s3_resource.buckets.all()]
    log.info(f'{buckets=}')
    return buckets


def create_bucket(bucket_name: str):
    s3_resource = init_s3_resource()

    try:
        log.info(f'Creating new bucket: {bucket_name}')
        bucket = s3_resource.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': s3_resource.meta.client.meta.region_name
            },
        )
        bucket.wait_until_exists()
        return list_buckets()
    except ClientError as e:
        log.error(f'Failed to create bucket: {e}')
        raise e


def delete_bucket(bucket_name: str):
    log.info(f'Deleting bucket: {bucket_name}')
    s3_client = init_s3_client()

    try:
        s3_client.delete_bucket(Bucket=bucket_name)
        return list_buckets()
    except ClientError as e:
        log.error(f'Failed to delete bucket: {e}')
        raise e

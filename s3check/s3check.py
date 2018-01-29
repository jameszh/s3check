#!/usr/bin/env python

import os
from tempfile import NamedTemporaryFile

import boto3
import click
from botocore.client import ClientError

s3 = boto3.resource('s3')

temp_file = NamedTemporaryFile(delete=False)
test_data = "test data"

temp_file.write(test_data)
temp_file.close()


def exists(bucket_name):
    try:
        s3.meta.client.head_bucket(Bucket=bucket_name)
        return True
    except ClientError:
        return False


def can_write(bucket_name, file):
    try:
        bucket = s3.Bucket(bucket_name)
        bucket.upload_file(file.name, os.path.basename(file.name))
        return True
    except (boto3.exceptions.S3UploadFailedError, ClientError):
        return False


def can_read(bucket_name, file):
    try:
        bucket = s3.Bucket(bucket_name)
        bucket.download_file(os.path.basename(file.name), file.name)

        with open(file.name, 'rt') as f:
            if f.read() != test_data:
                return False
        return True
    except ClientError:
        return False


def can_delete(bucket_name, file):
    try:
        bucket = s3.Bucket(bucket_name)
        bucket.delete_objects(
            Delete={
                'Objects': [
                    {
                        'Key': os.path.basename(file.name)
                    }
                ]
            }
        )
        return True
    except ClientError:
        return False


def can_list(bucket_name):
    try:
        bucket = s3.Bucket(bucket_name)
        response = bucket.objects.limit(count=10)
        if len(list(response)) >=0:
            return True
    except ClientError:
        return False


@click.command()
@click.option('--bucket', help='The bucket to check')
def main(bucket):
    if not exists(bucket):
        print("The bucket {} doesn't exist".format(bucket))
        exit(1)

    if not can_list(bucket):
        print("[ ] List objects in the bucket {}: Fail".format(bucket))
        exit(1)
    print("[*] List objects in the bucket {}: Pass".format(bucket))

    if not can_write(bucket, temp_file):
        print("[ ] Write to the bucket {}: Fail".format(bucket))
        exit(1)
    print("[*] Write to the bucket {}: Pass".format(bucket))

    if not can_read(bucket, temp_file):
        print("[ ] Read from the bucket {}: Fail".format(bucket))
        exit(1)
    print("[*] Read from the bucket {}: Pass".format(bucket))

    if not can_delete(bucket, temp_file):
        print("[ ] Delete object from bucket {}: Fail".format(bucket))
        exit(1)
    print('[*] Delete object from bucket {}: Pass'.format(bucket))

    os.unlink(temp_file.name)


if __name__ == '__main__':
    main()

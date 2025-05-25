from app.minio_client import client
from io import BytesIO
from typing import Iterable

# Bucket operations

def create_bucket(bucket_name: str):
    if not client.bucket_exists(bucket_name):
        client.make_bucket(bucket_name)


def delete_bucket(bucket_name: str):
    client.remove_bucket(bucket_name)


def list_buckets():
    return [b.name for b in client.list_buckets()]

# Object operations

def upload_object(bucket_name: str, object_name: str, data: bytes, content_type: str = "application/octet-stream"):
    client.put_object(bucket_name, object_name, data=BytesIO(data), length=len(data), content_type=content_type)


def download_object(bucket_name: str, object_name: str):
    return client.get_object(bucket_name, object_name)


def delete_object(bucket_name: str, object_name: str):
    client.remove_object(bucket_name, object_name)


def list_objects(bucket_name: str, prefix: str = "") -> Iterable[str]:
    for obj in client.list_objects(bucket_name, prefix=prefix):
        yield obj.object_name
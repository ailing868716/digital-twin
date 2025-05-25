from pydantic import BaseModel
from typing import List, Optional

class BucketRequest(BaseModel):
    bucket_name: str

class ObjectDeleteRequest(BaseModel):
    bucket_name: str
    object_names: List[str]

class ObjectListRequest(BaseModel):
    bucket_name: str
    prefix: Optional[str] = None
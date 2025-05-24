from fastapi import FastAPI
from app.routers import bucket, object

app = FastAPI(title="MinIO Adapter Service")

app.include_router(bucket.router, prefix="/minio/bucket", tags=["Bucket"])
app.include_router(object.router, prefix="/minio/object", tags=["Object"])

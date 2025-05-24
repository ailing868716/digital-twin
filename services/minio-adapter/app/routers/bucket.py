from fastapi import APIRouter, HTTPException
from app.schemas import BucketRequest
from app import crud

router = APIRouter()

@router.post("/create")
def create_bucket(req: BucketRequest):
    try:
        crud.create_bucket(req.bucket_name)
        return {"message": f"Bucket {req.bucket_name} created"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/delete")
def delete_bucket(bucket_name: str):
    try:
        crud.delete_bucket(bucket_name)
        return {"message": f"Bucket {bucket_name} deleted"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/list")
def list_buckets():
    try:
        buckets = crud.list_buckets()
        return {"buckets": buckets}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

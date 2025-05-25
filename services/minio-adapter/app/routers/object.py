from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from fastapi.responses import StreamingResponse
from io import BytesIO
from app.schemas import ObjectDeleteRequest, ObjectListRequest
from app import crud

router = APIRouter()

@router.post("/upload")
def upload_object( bucket_name: str = Form(...), file: UploadFile = File(...)):
    try:
        data = file.file.read()
        crud.upload_object(
            bucket_name,
            file.filename,
            data,
            content_type=file.content_type or "application/octet-stream"
        )
        return {"message": f"{file.filename} uploaded to {bucket_name}"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/download")
def download_object(bucket_name: str, object_name: str):
    try:
        resp = crud.download_object(bucket_name, object_name)
        return StreamingResponse(resp, headers={'Content-Disposition': f'attachment; filename="{object_name}"'})
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/delete")
def delete_objects(req: ObjectDeleteRequest):
    try:
        for name in req.object_names:
            crud.delete_object(req.bucket_name, name)
        return {"message": "objects deleted"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/list")
def list_objects(req: ObjectListRequest):
    try:
        names = list(crud.list_objects(req.bucket_name, prefix=req.prefix or ""))
        return {"objects": names}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
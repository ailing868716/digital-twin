from fastapi import APIRouter, HTTPException
from app.schemas import EntityCreateRequest, EntityUpdateRequest
from app import crud

router = APIRouter()


@router.post("/create")
def create_entity(req: EntityCreateRequest):
    try:
        entity_id = crud.create_entity(req.entity)
        return {"id": entity_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/get")
def get_entity(entity_id: str):
    try:
        entity = crud.get_entity(entity_id)
        return {"entity": entity}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.patch("/update")
def update_entity(req: EntityUpdateRequest):
    try:
        crud.update_entity(req.entity_id, req.attributes)
        return {"message": "updated"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/delete")
def delete_entity(entity_id: str):
    try:
        crud.delete_entity(entity_id)
        return {"message": "deleted"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/list")
def list_entities(entity_type: str = None):
    try:
        entities = crud.list_entities(entity_type)
        return {"entities": entities}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

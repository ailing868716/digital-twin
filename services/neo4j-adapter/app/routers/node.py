from fastapi import APIRouter, HTTPException
from app.schemas import NodeCreateRequest, NodeQueryRequest, NodeUpdateRequest, NodeDeleteRequest
from app import crud

router = APIRouter()

@router.post("/create")
def create_node(req: NodeCreateRequest):
    try:
        node_id = crud.create_node(req.label, req.properties)
        return {"id": node_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/query")
def query_nodes(req: NodeQueryRequest):
    try:
        nodes = crud.query_nodes(req.label, req.filters or {})
        return {"nodes": nodes}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.patch("/update")
def update_nodes(req: NodeUpdateRequest):
    try:
        count = crud.update_nodes(req.label, req.filters or {}, req.properties)
        return {"updated": count}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/delete")
def delete_nodes(req: NodeDeleteRequest):
    try:
        count = crud.delete_nodes(req.label, req.filters or {})
        return {"deleted": count}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
        
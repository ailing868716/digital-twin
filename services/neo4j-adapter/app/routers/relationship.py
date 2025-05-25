from fastapi import APIRouter, HTTPException
from app.schemas import (
    RelationshipCreateRequest,
    RelationshipQueryRequest,
    RelationshipDeleteRequest,
    RelationshipUpdateRequest,
    CypherRequest
)
from app import crud

router = APIRouter()

@router.post("/create")
def create_relationship(req: RelationshipCreateRequest):
    try:
        rel_id = crud.create_relationship(req.dict())
        return {"id": rel_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/query")
def query_relationships(req: RelationshipQueryRequest):
    try:
        relationships = crud.query_relationships(
            req.start_label, req.start_filters,
            req.end_label, req.end_filters,
            req.rel_type, req.rel_filters
        )
        return {"relationships": relationships}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/delete")
def delete_relationships(req: RelationshipDeleteRequest):
    try:
        count = crud.delete_relationships(
            req.start_label, req.start_filters,
            req.end_label, req.end_filters,
            req.rel_type
        )
        return {"deleted": count}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.patch("/update")
def update_relationships(req: RelationshipUpdateRequest):
    try:
        count = crud.update_relationships(
            req.start_label, req.start_filters,
            req.end_label, req.end_filters,
            req.rel_type, req.properties
        )
        return {"updated": count}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/cypher")
def run_cypher(req: CypherRequest):
    try:
        result = crud.run_cypher(req.cypher, req.params)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

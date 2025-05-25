from typing import Dict, Any
from pydantic import BaseModel


class EntityCreateRequest(BaseModel):
    entity: Dict[str, Any]


class EntityUpdateRequest(BaseModel):
    entity_id: str
    attributes: Dict[str, Any]

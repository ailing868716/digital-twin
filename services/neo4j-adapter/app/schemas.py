from typing import Dict, Any, Optional
from pydantic import BaseModel

class NodeBase(BaseModel):
    label: str
    filters: Optional[Dict[str, Any]] = None

class NodeCreateRequest(BaseModel):
    label: str
    properties: Dict[str, Any]

class NodeQueryRequest(NodeBase):
    pass

class NodeUpdateRequest(NodeBase):
    properties: Dict[str, Any]

class NodeDeleteRequest(NodeBase):
    pass

class RelationshipCreateRequest(BaseModel):
    start_label: str
    start_filters: Dict[str, Any]
    end_label: str
    end_filters: Dict[str, Any]
    rel_type: str
    properties: Optional[Dict[str, Any]] = None

class RelationshipQueryRequest(BaseModel):
    start_label: str
    start_filters: Optional[Dict[str, Any]] = None
    end_label: str
    end_filters: Optional[Dict[str, Any]] = None
    rel_type: str
    rel_filters: Optional[Dict[str, Any]] = None

class RelationshipDeleteRequest(BaseModel):
    start_label: str
    start_filters: Optional[Dict[str, Any]] = None
    end_label: str
    end_filters: Optional[Dict[str, Any]] = None
    rel_type: str

class RelationshipUpdateRequest(BaseModel):
    start_label: str
    start_filters: Optional[Dict[str, Any]] = None
    end_label: str
    end_filters: Optional[Dict[str, Any]] = None
    rel_type: str
    properties: Dict[str, Any]

class CypherRequest(BaseModel):
    cypher: str
    params: Optional[Dict[str, Any]] = None
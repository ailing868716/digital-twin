from pydantic import BaseModel
from typing import List, Dict, Any

class CreateTableRequest(BaseModel):
    table_name: str
    columns: Dict[str, str]  # {"id": "INT PRIMARY KEY", "name": "VARCHAR(255)"}

class InsertDataRequest(BaseModel):
    table_name: str
    values: List[Dict[str, Any]]

class QueryDataRequest(BaseModel):
    table_name: str
    filters: Dict[str, Any] = {}

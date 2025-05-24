from fastapi import APIRouter, HTTPException
from app.schemas import InsertDataRequest, QueryDataRequest
from app.crud import execute_raw_sql

router = APIRouter()

@router.post("/insert")
def insert_data(req: InsertDataRequest):
    for row in req.values:
        cols = ", ".join(row.keys())
        vals = ", ".join([f"'{v}'" for v in row.values()])
        sql = f"INSERT INTO {req.table_name} ({cols}) VALUES ({vals})"
        try:
            execute_raw_sql(sql)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
    return {"message": f"数据已插入 {req.table_name}"}

@router.post("/query")
def query_data(req: QueryDataRequest):
    filter_str = " AND ".join([f"{k}='{v}'" for k, v in req.filters.items()])
    sql = f"SELECT * FROM {req.table_name}"
    if filter_str:
        sql += f" WHERE {filter_str}"
    try:
        rows = execute_raw_sql(sql)
        return {"rows": [dict(row._mapping) for row in rows]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

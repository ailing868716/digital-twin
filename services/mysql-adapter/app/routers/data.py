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

@router.delete("/delete")
def delete_data(table_name: str, filters: str = ""):
    sql = f"DELETE FROM {table_name}"
    if filters:
        sql += f" WHERE {filters}"
    try:
        result = execute_raw_sql(sql)
        return {"message": f"数据已删除", "affected": result.rowcount}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.patch("/update")
def update_data(table_name: str, set_clause: str, filters: str = ""):
    sql = f"UPDATE {table_name} SET {set_clause}"
    if filters:
        sql += f" WHERE {filters}"
    try:
        result = execute_raw_sql(sql)
        return {"message": f"数据已更新", "affected": result.rowcount}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

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

from fastapi import APIRouter, HTTPException
from app.schemas import CreateTableRequest
from app.crud import execute_raw_sql

router = APIRouter()

@router.post("/create")
def create_table(req: CreateTableRequest):
    cols = ", ".join([f"{k} {v}" for k, v in req.columns.items()])
    sql = f"CREATE TABLE IF NOT EXISTS {req.table_name} ({cols})"
    try:
        execute_raw_sql(sql)
        return {"message": f"表 {req.table_name} 创建成功"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/drop")
def drop_table(table_name: str):
    sql = f"DROP TABLE IF EXISTS {table_name}"
    try:
        execute_raw_sql(sql)
        return {"message": f"表 {table_name} 已删除"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.patch("/alter")
def alter_table(table_name: str, action: str, column: str, col_type: str = None):
    if action == "add":
        sql = f"ALTER TABLE {table_name} ADD COLUMN {column} {col_type}"
    elif action == "drop":
        sql = f"ALTER TABLE {table_name} DROP COLUMN {column}"
    else:
        raise HTTPException(status_code=400, detail="action参数只支持 add 或 drop")
    try:
        execute_raw_sql(sql)
        return {"message": f"表 {table_name} 已变更"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/list")
def list_tables():
    sql = "SHOW TABLES"
    try:
        rows = execute_raw_sql(sql)
        tables = [list(row)[0] for row in rows]
        return {"tables": tables}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/schema")
def get_table_schema(table_name: str):
    sql = f"DESCRIBE {table_name}"
    try:
        rows = execute_raw_sql(sql)
        schema = [dict(row._mapping) for row in rows]
        return {"schema": schema}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

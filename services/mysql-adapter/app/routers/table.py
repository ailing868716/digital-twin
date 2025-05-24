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

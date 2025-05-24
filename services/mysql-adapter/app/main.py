from fastapi import FastAPI
from app.routers import table, data

app = FastAPI(title="MySQL Adapter Service")

# 注册路由模块
app.include_router(table.router, prefix="/mysql/table", tags=["Table"])
app.include_router(data.router, prefix="/mysql/data", tags=["Data"])

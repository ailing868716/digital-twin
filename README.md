# Digital Twin Platform

## 📁 项目结构
### test vscode 推送gitee，转移目录

digital-twin/
├── .env # 环境变量配置
├── docker-compose.yml # 容器编排文件
├── README.md # 项目说明
├── services/ # 微服务目录
│ └── api-service/ # 示例服务模块
│ └── main.py # FastAPI 示例入口
└── scripts/ # 辅助脚本
└── deploy.sh # 云端部署脚本（示意）

## 🚀 开发流程说明

### 本地开发
1. 在本地 VSCode 中打开项目目录
2. 编辑服务代码或 `docker-compose.yml`
3. 使用 `.env` 配置连接云端数据库等依赖服务
4. 本地运行 `uvicorn` 做功能测试

### 版本管理
1. 使用 `git add/commit/push` 将代码提交到 Gitee
2. 多人协作通过分支与 PR 管理代码合并
3. 保持 `main` 分支为部署主干

### 云端部署（在阿里云服务器）
```bash
cd ~/projects/digital-twin
git pull origin main
docker-compose up -d

☁️ 服务说明
MySQL: 3306

Neo4j: 7474（HTTP） / 7687（Bolt）

MinIO: 9001（控制台）

Orion-LD: 1026

📦 依赖工具
Docker / Docker Compose

Git / Gitee

VSCode / Uvicorn / FastAPI


---

### 📄 FastAPI 示例代码（路径：`digital-twin/services/api-service/main.py`）

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Digital Twin API Service is running"}
```

### 新增微服务
- `mysql-adapter`：提供 MySQL 数据库操作 API
- `minio-adapter`：提供 MinIO 对象存储操作 API

test克隆
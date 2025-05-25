from fastapi import FastAPI
from app.routers import node, relationship

app = FastAPI(title="Neo4j Adapter Service")

app.include_router(node.router, prefix="/neo4j/node", tags=["Node"])
app.include_router(relationship.router, prefix="/neo4j/relationship", tags=["Relationship"])

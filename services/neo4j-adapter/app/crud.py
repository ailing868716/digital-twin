from neo4j.exceptions import Neo4jError
from app.database import driver
from typing import Dict, Any, Tuple


def execute_cypher(cypher: str, params: Dict[str, Any] = None, fetch: bool = True):
    """Execute a Cypher query."""
    with driver.session() as session:
        try:
            result = session.run(cypher, params or {})
            if fetch:
                return [r.data() for r in result]
            else:
                return result.consume()
        except Neo4jError as e:
            raise e


def _build_match(var: str, label: str, filters: Dict[str, Any]) -> Tuple[str, Dict[str, Any]]:
    conditions = []
    params = {}
    for idx, (k, v) in enumerate(filters.items()):
        key = f"{var}{idx}"
        conditions.append(f"{var}.{k} = ${key}")
        params[key] = v
    clause = f"MATCH ({var}:{label})"
    if conditions:
        clause += " WHERE " + " AND ".join(conditions)
    return clause, params


def create_node(label: str, properties: Dict[str, Any]):
    cypher = f"CREATE (n:{label} $props) RETURN id(n) AS id"
    result = execute_cypher(cypher, {"props": properties})
    return result[0]["id"]


def query_nodes(label: str, filters: Dict[str, Any]):
    match, params = _build_match("n", label, filters)
    cypher = f"{match} RETURN properties(n) AS props, id(n) AS id"
    return execute_cypher(cypher, params)


def update_nodes(label: str, filters: Dict[str, Any], properties: Dict[str, Any]):
    match, params = _build_match("n", label, filters)
    params["props"] = properties
    cypher = f"{match} SET n += $props RETURN count(n) AS count"
    result = execute_cypher(cypher, params)
    return result[0]["count"]


def delete_nodes(label: str, filters: Dict[str, Any]):
    match, params = _build_match("n", label, filters)
    cypher = f"{match} DETACH DELETE n RETURN count(n) AS count"
    result = execute_cypher(cypher, params)
    return result[0]["count"]


def create_relationship(req: Dict[str, Any]):
    start_match, sp = _build_match("a", req["start_label"], req.get("start_filters", {}))
    end_match, ep = _build_match("b", req["end_label"], req.get("end_filters", {}))
    params = {**sp, **ep, "props": req.get("properties", {})}
    cypher = (
        f"{start_match}\n{end_match}\n"
        f"CREATE (a)-[r:{req['rel_type']} $props]->(b) RETURN id(r) AS id"
    )
    result = execute_cypher(cypher, params)
    return result[0]["id"]

# 关系查询
def query_relationships(start_label: str, start_filters: dict, end_label: str, end_filters: dict, rel_type: str, rel_filters: dict = None):
    start_match, sp = _build_match("a", start_label, start_filters or {})
    end_match, ep = _build_match("b", end_label, end_filters or {})
    params = {**sp, **ep}
    rel_clause = f"[r:{rel_type}]"
    if rel_filters:
        rel_conds = [f"r.{k} = $rel_{k}" for k in rel_filters]
        for k, v in rel_filters.items():
            params[f"rel_{k}"] = v
        rel_clause = f"[r:{rel_type} {{"
        rel_clause += ", ".join([f"{k}: $rel_{k}" for k in rel_filters])
        rel_clause += "}]"
    cypher = f"{start_match}\n{end_match}\nMATCH (a)-{rel_clause}->(b) RETURN id(r) AS id, properties(r) AS props"
    return execute_cypher(cypher, params)

# 关系删除
def delete_relationships(start_label: str, start_filters: dict, end_label: str, end_filters: dict, rel_type: str):
    start_match, sp = _build_match("a", start_label, start_filters or {})
    end_match, ep = _build_match("b", end_label, end_filters or {})
    params = {**sp, **ep}
    cypher = f"""{start_match}
{end_match}
MATCH (a)-[r:{rel_type}]->(b) DELETE r RETURN count(r) AS count"""
    result = execute_cypher(cypher, params)
    return result[0]["count"]

# 关系更新
def update_relationships(start_label: str, start_filters: dict, end_label: str, end_filters: dict, rel_type: str, properties: dict):
    start_match, sp = _build_match("a", start_label, start_filters or {})
    end_match, ep = _build_match("b", end_label, end_filters or {})
    params = {**sp, **ep, "props": properties}
    cypher = f"""{start_match}
{end_match}
MATCH (a)-[r:{rel_type}]->(b) SET r += $props RETURN count(r) AS count"""
    result = execute_cypher(cypher, params)
    return result[0]["count"]

# 通用Cypher接口
def run_cypher(cypher: str, params: dict = None):
    return execute_cypher(cypher, params)

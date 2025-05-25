from typing import Optional, Dict, Any
from app.orion_client import session, ORION_URL


def create_entity(entity: Dict[str, Any]):
    resp = session.post(f"{ORION_URL}/ngsi-ld/v1/entities", json=entity)
    resp.raise_for_status()
    return entity.get("id")


def get_entity(entity_id: str):
    resp = session.get(f"{ORION_URL}/ngsi-ld/v1/entities/{entity_id}")
    resp.raise_for_status()
    return resp.json()


def update_entity(entity_id: str, attributes: Dict[str, Any]):
    resp = session.patch(
        f"{ORION_URL}/ngsi-ld/v1/entities/{entity_id}/attrs",
        json=attributes,
    )
    resp.raise_for_status()


def delete_entity(entity_id: str):
    resp = session.delete(f"{ORION_URL}/ngsi-ld/v1/entities/{entity_id}")
    resp.raise_for_status()


def list_entities(entity_type: Optional[str] = None):
    params = {"type": entity_type} if entity_type else None
    resp = session.get(f"{ORION_URL}/ngsi-ld/v1/entities", params=params)
    resp.raise_for_status()
    return resp.json()

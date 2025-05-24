from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from app.database import SessionLocal

def execute_raw_sql(sql: str):
    session = SessionLocal()
    try:
        result = session.execute(text(sql))
        session.commit()
        return result.fetchall()
    except SQLAlchemyError as e:
        session.rollback()
        raise e
    finally:
        session.close()

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from app.database import SessionLocal

def execute_raw_sql(sql: str, fetch: bool = False):
    session = SessionLocal()
    try:
        result = session.execute(text(sql))
        session.commit()
        # 只有 SELECT、SHOW、DESC 等语句才需要 fetch
        if fetch:
            return result.fetchall()
        else:
            return result
    except SQLAlchemyError as e:
        session.rollback()
        raise e
    finally:
        session.close()


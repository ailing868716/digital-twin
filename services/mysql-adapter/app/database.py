from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import os

MYSQL_URL = f"mysql+pymysql://root:123456@mysql:3306/testdb"

engine = create_engine(MYSQL_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

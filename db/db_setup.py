from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# set up db using progress
SQLALCHEMY_DATABASE_URL = "postgresql://<pguser>:<pgpwd>@<host:port>/<dbname>."


engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={}, future=True)

SessionLocal = sessionmaker(future=True, autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# get the db
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os


DATABASE_URL = os.getenv("DATABASE_URL")
engine=create_engine(DATABASE_URL)
sessionlocal=sessionmaker(bind=engine)
base=declarative_base()

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os


DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:kinjal123@localhost:5432/job_scraper_db"
)
engine=create_engine(DATABASE_URL)
sessionlocal=sessionmaker(bind=engine)
base=declarative_base()
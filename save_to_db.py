from scraper import scrape_jobs
from database import engine,sessionlocal
from models import Job,base

#create table
base.metadata.create_all(bind=engine)

def save_jobs():
    db=sessionlocal()
    jobs=scrape_jobs()
    
    for job in jobs:
        db.add(Job(**job))
    
    db.commit()
    db.close()
    print("job saved to postgreSql.")

if __name__=="__main__":
    save_jobs()

from fastapi import FastAPI
from sqlalchemy.orm import Session
from database import sessionlocal, engine
from models import Job, base 
from schemas import JobCreate,JobUpdate,JobResponse
from fastapi import HTTPException

# Create tables if not exists
base.metadata.create_all(bind=engine)

app=FastAPI(title="job scraper API")

def get_db():
    db=sessionlocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Job Scraper API is running!"}

@app.get("/jobs")
def read_jobs():
    db: Session=next(get_db())
    jobs=db.query(Job).all()
    result=[]
    for job in jobs:
        result.append({
            "id": job.id,
            "title": job.title,
            "company": job.company,
            "location": job.location
        })
    return result

@app.get("/jobs/{id}")
def read_jobs_id(id:int):
    db: Session = sessionlocal()
    job=db.query(Job).filter(Job.id==id).first()
    if not job:
        print("job not found")
    else:
        return job
    db.close()

@app.post("/jobs")
def create_job(job: JobCreate):
    db: Session = sessionlocal()
    try:
        new_job = Job(title=job.title, company=job.company, location=job.location)
        db.add(new_job)
        db.commit()
        db.refresh(new_job)
        return new_job
    finally:
        db.close()

@app.put("/jobs/{id}",response_model=JobResponse)
def update_job(id:int,jobs:JobUpdate):
    db: Session = sessionlocal()
    try:
        job = db.get(Job, id)        
        if not job:
            print("job not found.")
        
        for key, value in jobs.dict(exclude_unset=True).items():
            setattr(job, key, value)

        db.commit()
        db.refresh(job)
        return job
    finally:
        db.close()
        
@app.delete("/jobs/{id}")
def delete_job(id: int):
    db: Session = sessionlocal()
    try:
        job = db.get(Job, id)
        if not job:
            raise HTTPException(status_code=404, detail="Job not found")
        db.delete(job)
        db.commit()
        return {"message": "Job deleted successfully"}
    finally:
        db.close()


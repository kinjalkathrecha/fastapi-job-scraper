from pydantic  import BaseModel
class JobCreate(BaseModel):
    title: str
    company: str
    location: str

class JobUpdate(BaseModel):
    title: str | None=None
    company: str | None=None
    location: str | None=None

class JobResponse(BaseModel):
    id: int
    title: str
    company: str
    location: str

    class Config:
        orm_mode = True

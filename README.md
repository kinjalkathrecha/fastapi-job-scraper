# FastAPI Job Scraper

A **FastAPI-based Job Scraper API** that scrapes job listings from websites and stores them in a PostgreSQL database.  
Provides **CRUD operations** via REST API and includes a web scraping script.

---

## Features

- Scrapes job title, company, and location
- Stores jobs in PostgreSQL using SQLAlchemy
- FastAPI REST API:
  - GET all jobs
  - GET job by ID
  - POST a new job
  - PUT/PATCH to update job
  - DELETE a job
- Swagger documentation available at `/docs`

---

## Tech Stack

- **Backend:** Python, FastAPI
- **Database:** PostgreSQL, SQLAlchemy ORM
- **Web Scraping:** BeautifulSoup, Requests

---

## Installation

1. Clone the repo:
```bash
git clone https://github.com/kinjalkathrecha/fastapi-job-scraper.git
cd fastapi-job-scraper

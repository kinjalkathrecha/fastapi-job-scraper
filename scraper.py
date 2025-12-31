import requests
from bs4 import BeautifulSoup

url="https://realpython.github.io/fake-jobs/"

def scrape_jobs():
    res=requests.get(url)
    soup=BeautifulSoup(res.text,"html.parser")
    jobs=[]
    job_cards=soup.find_all("div",class_='card-content')
    for job in job_cards:
        title=job.find("h2",class_="title").text.strip()
        company = job.find("h3", class_="company").text.strip()
        location = job.find("p", class_="location").text.strip()

        jobs.append({
            "title":title,
            "company":company,
            "location":location
        })
    return jobs

if __name__=="__main__":
    job_list=scrape_jobs()
    for job in job_list:
        print(job)
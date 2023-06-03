from requests import get
from bs4 import BeautifulSoup

def extract_wic_jobs():  
  response = get("https://workinculture.ca/JobBoard.aspx?itemid=&region=&levelid=1&ddfrom=&ddto=&pdfrom=&pdto=") 

  if response.status_code != 200:
    print("Can't request website")
  else:
    result = []
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find("div", {"id":"jobResultList"})
    job_posts = jobs.select("table tr")
    job_posts.pop(0)
    for job in job_posts:
      company = job.find("p", class_="organization")
      position = job.find("a")
      location = job.select('td')[1]
      anchor = job.select_one("a")
      link = anchor['href']

      job_data = {
        "company" : company.string.replace(",", " "),
        "position" : position.string.replace(",", " "),
        "location" : location.string.replace(",", " "),
        "link" : f"https://workinculture.ca{link}"
      }
      result.append(job_data)
    return result  
    
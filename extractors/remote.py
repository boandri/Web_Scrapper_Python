from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from file import save_to_file


def extract_remote_jobs(keyword):
    results = []
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)

    base_url = "https://remoteok.com/remote-"
    end_url = "-jobs"
    final_url = f"{base_url}{keyword}{end_url}"

    print("Requesting", final_url)
    driver.get(final_url)

    soup = BeautifulSoup(driver.page_source, "html.parser")

    table = soup.find(id="jobsboard")
    jobs = table.findAll("td", class_="company", recursive="False")
    
    for job in jobs:
        position = job.select_one("a > h2")
        anchor = job.select_one("a")
        link = anchor['href']
        company = job.select_one("span > h3")
        location = job.select_one("div", class_="location")
        
        if company != None:
            job_data = {
                'position': position.string.strip(),
                'link': f"https://remoteok.com{link}",
                'company': company.string.strip(),
                'location': location.string
            }
            results.append(job_data)
    return results

# save_to_file("remote", extract_remote_jobs("python"))
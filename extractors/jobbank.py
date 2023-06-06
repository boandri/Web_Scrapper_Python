from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def extract_jobbank_jobs(keyword):
  options = webdriver.ChromeOptions()
  options.add_experimental_option("excludeSwitches", ["enable-logging"])
  driver = webdriver.Chrome(options=options)

  base_url = "https://www.jobbank.gc.ca/jobsearch/jobsearch?searchstring="
  final_url = f"{base_url}{keyword}"
  driver.get(final_url)
  
  soup = BeautifulSoup(driver.page_source, "html.parser")

  print(soup)

  while (True):
    pass
  
extract_jobbank_jobs("python")
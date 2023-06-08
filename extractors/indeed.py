from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



def get_page_count(keyword):
  options = webdriver.ChromeOptions()
  options.add_experimental_option("excludeSwitches", ["enable-logging"])
  driver = webdriver.Chrome(options=options)

  # driver = webdriver.Chrome('C:/Users/seowo/source/repos/NomadCoder')
  # driver.implicitly_wait(3)
  driver.get(f"https://ca.indeed.com/jobs?q={keyword}")

  
  soup = BeautifulSoup(driver.page_source, "html.parser")

  pagination = soup.find('nav', {"aria-label": "pagination"})
  if pagination == None:
    return 1
  else:
    pages = pagination.find_all("div", recursive = False)
    count = len(pages)+1
    if count >= 5:
      return 5
    else:
      return count


def extract_indeed_jobs(keyword):
  pages = get_page_count(keyword)
  
  print("Found", pages, "pages")
  print("---------------------")

  results = []
  # results.append({'position': '<indeed jobs>', 'company':' ', 'location': ' ', 'link':' '})

  for page in range(pages):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)

    # driver = webdriver.Chrome('C:/Users/seowo/source/repos/NomadCoder')
    # driver.implicitly_wait(3)
    
    final_url = f"https://ca.indeed.com/jobs?q={keyword}&start={page * 10}"
    print("Requesting", final_url)
    
    driver.get(final_url)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    
    job_list = soup.find("ul", class_="jobsearch-ResultsList")
    jobs = job_list.find_all("li", recursive = False)
    
    for job in jobs:
      zone = job.find("div", class_="mosaic-zone")
      if zone == None:
        anchor = job.select_one("h2 a")
        title = anchor["aria-label"]
        link = anchor["href"]
        company = job.find("span", class_="companyName")
        location = job.find("div", class_="companyLocation").text.replace(",", " ")
        

        if location != None:
          job_data = {
            'link' : f"https://ca.indeed.com{link}",
            'company' : company.string.replace(",", " "),
            'location' : location,
            'position' : title.replace(",", " ")
          }
        results.append(job_data)
  
  return results
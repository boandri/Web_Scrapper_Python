from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def extract_remote_jobs(keyword):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)

    base_url = "https://remoteok.com/remote-"
    end_url = "-jobs"
    final_url = f"{base_url}{keyword}{end_url}"

    print("Requesting", final_url)
    driver.get(final_url)

    soup = BeautifulSoup(driver.page_source, "html.parser")

    print(soup)

    while (True):
        pass

extract_remote_jobs("python")
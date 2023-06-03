from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs
from extractors.wic import extract_wic_jobs

#make CSV file of indeed and wwr


# keyword = input("What do you want to search 4?")

# indeed = extract_indeed_jobs(keyword)
# wwr = extract_wwr_jobs(keyword)
# jobs = wwr + indeed

# file = open(f"{keyword}.csv", "w")
# file.write("Position,Company,Location,URL\n")
# for job in jobs:
#   file.write(f"{job['position']},{job['company']},{job['location']},{job['link']}\n")
# file.close()




#make csv file of Work In Culture "intern" jobs

keyword = input("Type name of file for extracting Work In Culture intern jobs:")
file = open(f"{keyword}.csv", "w")
file.write("Position, Company, Location, URL\n")

jobs = extract_wic_jobs()
for job in jobs:
  file.write(f"{job['position']},{job['company']},{job['location']},{job['link']}\n")
file.close()
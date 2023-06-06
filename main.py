from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs
from extractors.wic import extract_wic_jobs
from file import save_to_file

#make CSV file
keyword = input("What do you want to search for?")
file_name = input("File name:")

indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)
wic = extract_wic_jobs()

jobs = indeed + wwr + wic
save_to_file(file_name, jobs)



# from flask import Flask, render_template, request
# from extractors.indeed import extract_indeed_jobs
# from extractors.wic import extract_wic_jobs
# from extractors.wwr import extract_wwr_jobs

# app = Flask("JobScrapper")

# @app.route("/")
# def home():
#   return render_template("home.html", name = "Tho")

# @app.route("/search")  
# def search():
#   keyword = request.args.get("keyword")
#   wic = extract_wic_jobs()
#   wwr = extract_wwr_jobs(keyword)
#   indeed = extract_indeed_jobs(keyword)
#   jobs = indeed
#   return render_template("search.html", keyword = keyword, jobs = jobs)

# app.run("0.0.0.0")


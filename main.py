"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""
import os
from flask import Flask, render_template, request, redirect, send_file
from scrapper.so import get_jobs as get_so_jobs
from scrapper.wwr import get_jobs as get_wwr_jobs
from scrapper.rok import get_jobs as get_rok_jobs
from scrapper.exporter import save_to_file

db = {}
app = Flask("LastChallenge")

# static folder reset
for file in os.listdir("./static"):
  os.remove(f"./static/{file}")

# index.html
@app.route("/")
def index():
  return render_template("index.html")

# search.html / search jobs by term
@app.route("/search")
def search():
  term = request.args.get('term')
  from_db = db.get(term)
  if from_db:
    jobs = from_db
  else:
    jobs = get_so_jobs(term) + get_wwr_jobs(term) + get_rok_jobs(term)
    if jobs:
      db[term] = jobs
      save_to_file(term, jobs)
  return render_template(
    "search.html",
    searching_by = term,
    jobs = jobs,
    num_results = len(jobs)
  )

app.run(host="0.0.0.0")
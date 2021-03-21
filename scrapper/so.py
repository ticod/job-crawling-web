import requests
from bs4 import BeautifulSoup

so_url = "https://stackoverflow.com"

def make_url(term):
  term = term.lower()
  return f"{so_url}/jobs?r=true&q={term}"

def get_jobs(term):
  soup = BeautifulSoup(requests.get(make_url(term)).text, "html.parser")
  try:
    result_empty = soup.find("div", {"class":"s-empty-state"})
    if result_empty:
      raise Exception()
    results = soup.find("div", {"class":"listResults"}).find_all("div", {"class":"-job"})
  except:
    return []
  jobs = []
  for result in results:
    try:
      temp = result.find("h2").find("a")
      title = temp["title"]
      company = result.find("h3", {"class":"mb4"}).find_all("span")[0].string.strip()
      url = so_url + temp["href"]
      jobs.append({"title":title, "company":company, "url":url})
    except Exception as e:
      print(e)
  return jobs
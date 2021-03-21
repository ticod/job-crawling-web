import requests
from bs4 import BeautifulSoup

wwr_url = "https://weworkremotely.com"

def make_url(term):
  term = term.lower()
  return f"{wwr_url}/remote-jobs/search?term={term}"

def get_jobs(term):
  soup = BeautifulSoup(requests.get(make_url(term)).text, "html.parser")
  try:
    results = soup.find("div", {"class":"jobs-container"}).find_all("li")
    results_viewall = soup.find("div", {"class":"jobs-container"}).find_all("li", {"class":"view-all"})
  except:
    return []
  results = list(set(results)-set(results_viewall))
  jobs = []
  for result in results:
    try:
      temp = result.find("a", recursive=False)
      title = temp.find("span", {"class":"title"}).string.strip()
      company = temp.find("span", {"class":"company"}).string.strip()
      url = wwr_url + temp["href"]
      jobs.append({"title":title, "company":company, "url":url})
    except Exception as e:
      print(e)
  return jobs
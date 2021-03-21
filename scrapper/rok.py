import requests
from bs4 import BeautifulSoup

rok_url = "https://remoteok.io"

def make_url(term):
  term = term.lower()
  if '+' in term:
    term.replace("+", "-plus")
  if '#' in term:
    term.replace("#", "-sharp")
  return f"{rok_url}/remote-dev+{term}-jobs"

def get_jobs(term):
  soup = BeautifulSoup(requests.get(make_url(term)).text, "html.parser")
  try:
    results = soup.find("table", {"id":"jobsboard"}).find_all("tr", {"class":"job"})
  except:
    return []
  jobs = []
  for result in results:
    try:
      temp = result.find("td", {"class":"company"})
      title = temp.find("h2").string.strip()
      company = temp.find("h3").string.strip()
      url = rok_url + temp.find("a", {"itemprop":"url"})["href"]
      jobs.append({"title":title, "company":company, "url":url})
    except Exception as e:
      print(e)
  return jobs
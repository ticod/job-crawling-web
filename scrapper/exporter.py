import csv

def save_to_file(term, jobs):
  file = open(f"./static/{term}.csv", mode="w")
  writer = csv.writer(file)
  writer.writerow(["title", "company", "link"])
  for job in jobs:
    writer.writerow(list(job.values()))
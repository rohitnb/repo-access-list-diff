import requests
import json
import os
import csv
fields = ['name','viewerPermission']

### INPUTS AS ENVIRONMENT VARIABLES
organization_name = os.environ['ORG_NAME']
token= os.environ['GH_TOKEN']
affiliation = os.environ['AFFILIATION']
if affiliation:
      payload="{\n    \"affiliation\": \""+affiliation+"\"\n}"

### PAGES
page=1
total_pages=99999

csv_data = []

### GET RESPONSES FROM ALL PAGES
while page<=total_pages:
  print("Page Number "+str(page))
  url = "https://api.github.com/user/repos?per_page=100&page="+str(page)
  headers = {
    'Accept': 'application/vnd.github.v3+json',
    'Authorization': 'token '+token,
    'Content-Type': 'application/json'
  }
  if affiliation:
    response = requests.request("GET", url, headers=headers, data=payload)
  else:
    response = requests.request("GET", url, headers=headers)
  try:
    if page == 1:
      total_pages = int(response.headers['Link'].split(",")[1].split(">;")[0].split("&page=")[1])
      print("Total Page still at MAX. Reset to "+str(total_pages))
  except KeyError:
    total_pages=1
  
  responseobject = response.json()  
  page = page+1

  for row in responseobject:
    if row['owner']['login'] == organization_name:
      if row['permissions']['admin']:
        permissions = "ADMIN"
      elif row['permissions']['push']:
        permissions = "WRITE"
      elif row['permissions']['pull']:
        permissions = "READ"

      temp = [row['name'],permissions]
      csv_data.append(temp)

filename = "explicit-access-repos.csv"
with open(filename, 'w') as csvfile:
  csvwriter = csv.writer(csvfile) 
  csvwriter.writerow(fields)
  csvwriter.writerows(csv_data)

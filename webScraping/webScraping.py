import requests
from ns4 import BeautifulSoup
import csv
from itertools import zip_longest


jobTitle = []
jobDescription = []
companyName = []
locationName = []

#    fetching the url
result = requests.get("https://www.bayt.com/en/morocco/jobs/")

#    saving the page content
src = result.content
print(src)

#     getting infos that i need as elements such as job title, company name, job description, company location
jobTitles = soup.find_all("a", {"data-js-aid":"jobID"})
jobDescriptions = soup.find_all("div", {"class":"jb-descr m10t t-small"})
companyNames = soup.find_all("b", {"class":"jb-company"})
companyLocations = soup.find_all("span", {"class":"jb-loc t-mute t-nowrap"})

#     extracting needed data from the elements
for i in range(len(jobTitles)):
    jobTitle.append(jobTitles[i].text)
    links.append(jobTitles[i]).find("a").attrs['href']
    jobDescription.append(jobDescriptions[i].text)
    companyName.append(companyNames[i].text)
    companyLocation.append(companyLocations[i].text)

for link in links:
    result = requests.get(link)
    src = result.content
    soup = BeautifulSoup(src, "lxml")
    req = soup.find_all("div", {"class":"card-content"})
dataFileList = [[jobTitle, companyName, companyLocation, jobDescription]]
exported = zip_longest(*dataFileList)

with open("data.csv", "w") as dataFile:
    wr = csv.writer(dataFile)
    wr.writerow(['job title', 'campany name', 'company location', 'job description'])
    wr.writerows(exported)

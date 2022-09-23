import requests
from bs4 import BeautifulSoup

from Function_file import *


URL = "https://realpython.github.io/fake-jobs/"

# Creation of page object from the URL
page = getPageFromURL(URL)

# Creation of BeautifulSoup object from the page content
soup = BeautifulSoup(page.content, "html.parser")
#soup = getSoupFromPage(page)

# Creation of ResultsContainer object from the soup object
results = getResultsContainer(soup)


job_elements = results.find_all("div", class_="card-content")

# Creation of a list containing python offers
python_jobs = getPythonJobsList(results)



python_job_elements = [
    getThirdParent(h2_element) for h2_element in python_jobs
]

print()
# Printing number of python job offers
print(str(len(python_jobs))+" Offers: ")


# This loop prints jobs details of offers contained in python_job_elements list such as the title, the company and the location
for job_element in python_job_elements:
    
    printJobDetails(job_element)
    
    
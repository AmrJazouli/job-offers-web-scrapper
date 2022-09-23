import requests
from bs4 import BeautifulSoup


def getPageFromURL(URL):
    '''
    This function returns a page object as output from an URL as input
    '''
    return  requests.get(URL)

def getSoupFromPage(Page):
    '''
    This function returns a Soup object as output from a page as input
    '''
    return  BeautifulSoup(Page.content, "html parser")

def getResultsContainer(Soup):
    '''
    This function returns a ResultsContainer object as output from a BeautifulSoup object as input
    '''
    return  Soup.find(id="ResultsContainer")    

def getPythonJobsList(ResultsContainer):
    '''
    This function uses lambda function to filters out non-python jobs and returns a python jobs list as output 
    from a ResultsContainer object as input
    '''
    return ResultsContainer.find_all(
    "h2", string=lambda text: "python" in text.lower()
    )


def getThirdParent(h2_element):
    '''
    This function gets the 3rd parent of the element
    '''
    return  h2_element.parent.parent.parent

def printTitle(job_element):
    '''
    This function retrieves and prints the title element
    '''
    title_element = job_element.find("h2", class_="title")
    print(title_element.text.strip())
    
def printCompany(job_element):
    '''
    This function retrieves and prints the company element
    '''
    company_element = job_element.find("h3", class_="company")
    print(company_element.text.strip())

def printLocation(job_element):
    '''
    This function retrieves and prints the location element
    '''
    location_element = job_element.find("p", class_="location")
    print(location_element.text.strip())    


def printJobDetails(job_element):
    '''
    This function prints job details such as title, company and location
    '''
    print()
    print()
    printTitle(job_element)
    printCompany(job_element)
    printLocation(job_element)
    print()
    printLinkUrl(job_element)
    print()

def getLinkUrl(job_element):
    '''
    This function gets the URL link
    '''
    return job_element.find_all("a")[1]["href"]

def printLinkUrl(job_element):
    '''
    This function prints the link URL
    '''
    link_url = getLinkUrl(job_element)
    return print(f"Apply here: {link_url}\n")

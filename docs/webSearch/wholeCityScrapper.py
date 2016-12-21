import requests
import bs4
from cityPageScrapper import cityPageScrapper


#will scrape a full city for all available homes and return  a list of property info
def wholeCityScrapper(link):
	cityHomes = [] # a list of all the homes in the city
	nextPageAvailable = 1 # indicates whether or not a next page is present
	
	while nextPageAvailable ==1 :
		print(len(cityHomes))
		#create a soup object for the current page
		cityPage = requests.get(link)
		cityPage.raise_for_status()
		soupObj = bs4.BeautifulSoup(cityPage.text,"html.parser")
		cityHomes = cityHomes+cityPageScrapper(soupObj)

		#determine if a next page exists if yes update the link
		pager = soupObj.find('div', {'class':'p24_pager'})
		nextPage = pager.find('a',{'class':'pull-right'})


		link = nextPage['href']
		if link.startswith('https://')==False:
			nextPageAvailable = 0


	return cityHomes

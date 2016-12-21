import bs4
import requests
from wholeCityScrapper import wholeCityScrapper
from printToFile import printToFile

#will scrape a certain province for all its data and print to a certain file

def provinceScrapper(provLink, fileToSave):

	#create list of links to each sub city
	provPage = requests.get(provLink)
	provPage.raise_for_status()
	provSoup = bs4.BeautifulSoup(provPage.text,"html.parser")
	allCities = provSoup.find('div',{'class':'p24_results'}).find('div',{'class':'col-xs-9'}) # isolates the section of the tree containing the city list
	cityLinks = allCities.findAll('a') # obtain the links to the web addresses for all the cities

	for link in cityLinks:
		print("Hello")
		linkFull = 'https://www.property24.com'+link['href']
		# the province scrapper will first do a check to make sure that cities have properties
		checkContent = requests.get(linkFull)
		checkContent.raise_for_status()
		checkSoup = bs4.BeautifulSoup(checkContent.text,"html.parser")
		if len(checkSoup.findAll(text = "No properties found"))==0: 
			# only cities with at least one home for sale are considered in this loop
			cityHomes = wholeCityScrapper(linkFull)
			printToFile(cityHomes, fileToSave)


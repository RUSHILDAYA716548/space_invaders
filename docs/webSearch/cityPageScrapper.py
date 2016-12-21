import requests
import bs4
from extractFeatures import extractFeatures

#function which scraps a single city page does not run to the next page
def cityPageScrapper(pageSoup):

	pageResults = []
	homes = pageSoup.findAll('div', {'itemtype':'http://schema.org/Product'})
	for home in homes:
		resultString =" "

		#the link gives suburb info as well as the unique p24 identifer
		link = home.find('a')['href']
		resultString = resultString+link+';'

		#obtain the street address if it exists
		street = home.find('span',{"class":"p24_address"})
		if type(street)==type(home): #checks to see if the address object has been found
			resultString=resultString + street.get_text()+';'
		else:
			resultString=resultString+'NULL'+';'	


		#obtain the property value 
		try:
			price = home.find('span',{"class":"p24_price"})['content']
		except KeyError :
			price ='NULL'
		resultString = resultString+price+';'	

		#scrape the size of the property
		plotSize = home.find('span',{'class':'p24_size'})
		if type(plotSize)==type(home):
			plotSize = plotSize.find('span',{'class':'p24_bold'}).get_text()
			resultString = resultString+plotSize+';'
		else:
			resultString=resultString+'NULL'+';'

		#obtain information related to number of bathrooms, bedrooms and garages
		#featureTree = home.find('span',{'class':'p24_features'})
		#featureString = extractFeatures(featureTree)
		#resultString = resultString + featureString


		#add the information home info to page results
		pageResults = pageResults+[resultString]

	return pageResults
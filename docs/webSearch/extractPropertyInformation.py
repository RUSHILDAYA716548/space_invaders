# code used specifically to extract information from the property 24 website
# from a single home listing
#using the beautiful soup package

import bs4
import requests

def extractPropertyInformation(propSoup):
	dataString = ""

	#identify the location trail
	suburb =propSoup.find('div',{"id":"breadCrumbContainer"}).get_text()
	suburb = suburb.replace('>',';')
	dataString = dataString+suburb+';'	

	#identify the street 
	location =  propSoup.find('div',{"class":"p24_address"}).findAll('div',{"class":"row"})[1].find('div',{"class","col-xs-12"}).get_text()
	location = location.replace('\n', ' ').replace('\r',' ')
	dataString = dataString+location+";"

	#identifing the properties price
	price  = propSoup.find('div', {"class" : "p24_price"}).get_text()
	dataString = dataString+price+";"

	return (dataString)
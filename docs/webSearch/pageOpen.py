
import requests
import bs4
from provinceScrapper import provinceScrapper
#from extractPropertyInformation import extractPropertyInformation
#from cityPageScrapper import cityPageScrapper
#from wholeCityScrapper import wholeCityScrapper
#from printToFile import printToFile
#from extractFeatures import extractFeatures

#link = 'https://www.property24.com/for-sale/northam/limpopo/737'
#data = wholeCityScrapper(link)

#printToFile(data, 'westernCape.csv')

#res = requests.get('https://www.property24.com/for-sale/westonaria/carletonville/gauteng/4946?PropertyCategory=House%2cApartmentOrFlat%2cTownhouse%2cVacantLandOrPlot')
#res.raise_for_status()
#soup = bs4.BeautifulSoup(res.text,"html.parser")

#extractFeatures(soup.find('span',{'class':'p24_features'}))

linkR = 'https://www.property24.com/for-sale/all-cities/limpopo/14?PropertyCategory=House%2cApartmentOrFlat%2cTownhouse'
fileR = 'limpopo.csv'

#provinceScrapper(linkR, fileR)
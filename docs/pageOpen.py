
import requests
import bs4
from extractPropertyInformation import extractPropertyInformation
from cityPageScrapper import cityPageScrapper
from wholeCityScrapper import wholeCityScrapper
from printToFile import printToFile
from extractFeatures import extractFeatures




#link = 'https://www.property24.com/for-sale/northam/limpopo/737'
#data = wholeCityScrapper(link)

#printToFile(data, 'westernCape.csv')

res = requests.get('https://www.property24.com/for-sale/venterspos/carletonville/gauteng/4943?PropertyCategory=House%2cApartmentOrFlat%2cTownhouse%2cVacantLandOrPlot')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,"html.parser")

extractFeatures(soup.find('span',{'class':'p24_features'}))
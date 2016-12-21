import bs4
import requests
from provinceScrapper import provinceScrapper




linkR = 'https://www.property24.com/for-sale/all-cities/free-state/3?PropertyCategory=House%2cApartmentOrFlat%2cTownhouse'
saveR = 'freeState.csv'

provinceScrapper(linkR, saveR)
### TO USE
#
# python v3.6
#
## Packages
#
# Requests
#   pip install requests
#
# Beautiful soup
#   pip install beautifulsoup4



import requests
from bs4 import BeautifulSoup

#def scrape (city):

url = 'https://www.airbnb.com.au/s/Brisbane-City--Australia'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, "lxml")
count = 0
homes = []

#print(soup.prettify())
#listing = soup.select('div[class*="listingContainer"]')

#print (soup.select('div[class*="listingContainer"]').prettify())

for listings in soup.select('div[class*="listingContainer"]'):
    for link in listings.find_all('a'):
        homes.append('https://www.airbnb.com.au'+link.get('href'))

print(homes)




    #print(city)
    #print(count)

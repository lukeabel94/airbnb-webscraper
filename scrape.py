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
#print(soup.prettify())
#listing = soup.select('div[class*="listingContainer"]')

#print (soup.select('div[class*="listingContainer"]').prettify())

for listings in soup.select('div[class*="listingContainer"]'):

    if count == 1:
        #print (listings.get_text())
        print (listings.prettify())

    count = count + 1
    #print (listings.prettify())
    #count = count + 1



    #print(city)
    #print(count)

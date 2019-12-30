from bs4 import BeautifulSoup
import os, requests, time, urllib.request

os.makedirs('baudet/vergaderingen', exist_ok=True)
verslagen = {}

def main():
    for page in range(1, 14):
        url = 'https://www.tweedekamer.nl/kamerstukken/plenaire_verslagen?qry=*&fld_tk_categorie=kamerstukken&srt=date%3Adesc%3Adate&fld_prl_kamerstuk=Plenaire+verslagen&dpp=25&clusterName=Kamerstukken&fromdate=01%2F03%2F2017&todate=31%2F12%2F2019&page={}'.format(page)
        scrape(url)
        

def scrape(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    time.sleep(2)
    items = soup.select('div.flexer')
    
    for row in items:
        daterow = row.select('div.card__pretitle')
        for x in daterow:
            date = x.getText()

        linkrow = row.select('a')
        for x in linkrow:
            link = 'https://tweedekamer.nl{}'.format(x['href'])
        
        verslagen[date] = link
        filename = date.replace(" ", "_")
        urllib.request.urlretrieve(link, 'baudet/vergaderingen/{}.html'.format(filename))

if __name__=='__main__':
    main()
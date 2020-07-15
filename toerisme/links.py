'''

To do's POC: 
# Antwerpen lijst met bezienswaardigheden scrapen
# Per bezienswaardigheid de reviews scrapen (in alle talen) - Selenium
# Van de reviews nodig: totale reviews, aantal reviews per type score, alle reviewers: per reviewer de locatie (als die er is)
# bereken de rating van elke attractie
# output naar CSV met locatie - attractie - reviewerlocatie
# andere output naar CSV met locatie - attractie - aantal reviews - rating 

'''

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from geopy.geocoders import Nominatim
import requests, csv


url = "https://www.tripadvisor.be/Attractions-g2263872-Activities-a_allAttractions.true-Wallonia.html"
options = webdriver.ChromeOptions()
options.add_argument('headless')
browser = webdriver.Chrome(options=options)
wait = WebDriverWait(browser, 10)
browser.get(url)

def extract_attractions(browser, wait):
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    # list of attracties
    atrr_output = soup.select('a._1QKQOve4')

    # location
    # location_output = soup.select('h1#HEADING')
    # location = location_output[0].text[14:]

    for row in atrr_output:
        row['href'] = 'https://www.tripadvisor.be{}'.format(row['href'])
        link = requests.get(row['href'])
        review_soup = BeautifulSoup(link.text, 'html.parser')

        # locatie
        try:
            location_output = review_soup.select('div.eQSJNhO6 a')
            location = location_output[0].text[21:]
        except:
            location = "Onbekende locatie"
        
        # attractienaam
        try:
            att_output = review_soup.select('h1#HEADING')
            att = att_output[0].text
        except: 
            att = "Onbekende attractie"

        # url
        try:
            url = row['href']
        except:
            url = 'geen url gevonden'

        #attractie toevoegen aan csv
        links = [location, att, url]
        with open('toerisme/links.csv', 'a') as urls:
            writer = csv.writer(urls)
            writer.writerow(links)
        print("Appending url to csv...")


while True:
    try: 
        extract_attractions(browser, wait)
        browser.get(url)
        navigation = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.ui_pagination.is-centered a.ui_button.nav.next')))
        navigation.click()
        nav = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.ui_pagination.is-centered a.ui_button.nav.next')))
        url = browser.current_url
        browser.get(url)
        print("Going to the next attractions page...")

    except:
        extract_attractions(browser, wait)
        print("Done with this location.")
        break
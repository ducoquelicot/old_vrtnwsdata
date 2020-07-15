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
import os, requests, csv, time

url = "https://www.tripadvisor.be/Attractions-g2263872-Activities-oa660-a_allAttractions.true-Wallonia.html"
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

        # reviews total
        numbers = review_soup.select('ul._2lcHrbTn li span._3fVK8yi6')
        total_reviews = 0
        for x in range(len(numbers)):
            total_reviews += int(numbers[x].text.replace('.', ''))

        # rating
        total_score = 0
        for i, x in enumerate(numbers):
            if i == 0:
                total_score += int(x.text.replace('.', '')) * 5
            elif i == 1:
                total_score += int(x.text.replace('.', '')) * 4
            elif i == 2:
                total_score += int(x.text.replace('.', '')) * 3
            elif i == 3:
                total_score += int(x.text.replace('.', '')) * 2
            elif i == 4:
                total_score += int(x.text.replace('.', ''))

        if total_reviews:
            rating = round(total_score / total_reviews, 1)
        else:
            rating = 0

        #attractie toevoegen aan csv
        attractie = [location, att, total_reviews, rating]
        with open('toerisme/attracties.csv', 'a') as attracties:
            writer = csv.writer(attracties)
            writer.writerow(attractie)
        print("Appending attraction to csv...")

        # reviews extracten
        browser.get(row['href'])
        radio = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[for="LanguageFilter_0"]')))
        radio.click()
        browser.implicitly_wait(10)

        while True:
            try:
                button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.ui_pagination.is-centered a.ui_button.nav.next')))

                soep = BeautifulSoup(browser.page_source, 'html.parser')
                soep_output = soep.select('span._1TuWwpYf')

                for row in soep_output:
                    rec = [location, att, row.text]
                    with open('toerisme/reviews.csv', 'a') as recensie:
                        writer = csv.writer(recensie)
                        writer.writerow(rec)
                    print("Appending review...")
        
                button.click()
                print("Going to the next review page...")

            except:
                soep = BeautifulSoup(browser.page_source, 'html.parser')
                soep_output = soep.select('span._1TuWwpYf')

                for row in soep_output:
                    rec = [location, att, row.text]
                    with open('toerisme/reviews.csv', 'a') as recensie:
                        writer = csv.writer(recensie)
                        writer.writerow(rec)
                    print("Appending review...")

                print("Done with this attraction.")
                break

while True:
    try: 
        extract_attractions(browser, wait)
        # breakpoint()
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
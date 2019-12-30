from bs4 import BeautifulSoup
import os, glob, re, csv

def main():
    vergaderingen = glob.glob('baudet/vergaderingen/*')

    data = []
    for row in vergaderingen:
        filename = os.path.basename(row)[:-5].replace("_", " ")
        output = scrape(row)
        if output:
            data.append([filename])
            
    writeout(data)

def scrape(url):
    soup = BeautifulSoup(open(url), 'html.parser')
    if soup.find(string=re.compile('Baudet')):
        return True

def writeout(data):
    with open('baudet/data.csv', 'w') as baudet_data:
        writer = csv.writer(baudet_data)
        writer.writerow(['datum'])
        writer.writerows(data)

if __name__ == '__main__':
    main()


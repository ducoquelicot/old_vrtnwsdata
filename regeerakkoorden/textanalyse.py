'''
Dit is een kort script om de Vlaamse regeerakkoorden tussen 1991 en 2014 doorzoekbaar te maken,
de meest voorkomende woorden te tellen en te sorteren en dit als output in een csv te stoppen voor
verdere analyse.

Fabienne Meijer - 2019
'''

import glob, os, collections, csv, string
import pandas as pd

texts = glob.glob('/home/fabienne/Desktop/vrtnws/regeerakkoorden/*.txt')

# In de eerste 'contents' line maken we alle woorden lowercase (Python maakt onderscheid tussen uppercase
# en lowercase dus zal anders twee dezelfde woorden niet als zodanig herkennen) en splitten het bestand op elk
# woord in het tekstbestand. 

# In de tweede 'contents' halen we alle interpunctie uit woorden, omdat we zagen dat er soms een verdwaalde komma
# of punt bleef hangen achter een woord. 

# uniek verzamelt alle unieke woorden in de set. teller telt hoe vaak elk woord voorkomt. We stoppen dit dan in een pandas
# dataframe om een net overzicht te krijgen wat we makkelijk naar een csv kunnen exporteren. 

# In de uitgecommente code onderaan hebben we de unieke woorden geexporteerd naar een csv om te controleren of er geen fouten 
# meer in zaten, bijvoorbeeld duplicate waardes vanwege interpunctiefouten, of andere problemen. 

for pdf in texts:
    filename = os.path.basename(pdf)[7:-4]
    with open(pdf) as regeerakkoord:
        contents = [word.lower() for line in regeerakkoord for word in line.split()]
        contents = [''.join(c for c in s if c not in string.punctuation) for s in contents]
        uniek = list(set(contents))
        teller = collections.Counter(contents)
        # print(teller.most_common(100))
        df = pd.DataFrame(data=teller.most_common(100), columns=['words', 'count'])
        df.to_csv('regeerakkoorden/woorden_{}.csv'.format(filename))
    
# with open(os.path.expanduser('~/Desktop/vrtnws/regeerakkoorden/uniek.csv'), 'w') as unique:
#     writer = csv.writer(unique)
#     for item in uniek:
#         writer.writerow([item])
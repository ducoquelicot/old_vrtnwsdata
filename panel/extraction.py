'''

Script om uit de dagelijkse Excel-bestanden van het panel de relevante antwoordopties te halen, zodat deze geanalyseerd kunnen worden.
Creëert voor elk dagelijks bestand een csv met alleen de relevante elementen. 

Fabienne Meijer, oktober 2019

'''

import os, glob
import pandas as pd
import datetime as dt

files = glob.glob(os.path.expanduser('~/Desktop/vrtnws_data/panel/*2019.csv'))

def main():
    for file in files:
        filename = os.path.basename(file)[:-4]
        if not os.path.isfile(os.path.expanduser('~/Desktop/vrtnws_data/panel/{}_ex.csv'.format(filename))):

            # Opent de csv met de vragen en zet de datum-column om op een manier die matcht met de titel van het bestand
            questions = pd.read_csv(os.path.expanduser('~/Desktop/vrtnws_data/panel/vragen.csv'), sep=';')
            questions.columns = questions.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('-', '')
            questions['datum'] = pd.to_datetime(questions['datum'], format = '%d/%m/%Y').dt.strftime('%d%m%Y')

            # Haal alle codes van die dag uit het bestand en zet die in een lijst. Voeg daaraan toe de codes van de overige elementen die we inspecteren
            relevant = questions[questions.datum == filename].code.tolist()
            relevant.extend(['Geslacht', 'Leeftijd3N', 'Diploma3', 'datum'])

            # Niet elke dag heeft hetzelfde aantal onderwerpen, dus we voegen aan de lijst ook nog het aantal codes toe precies hoeveel onderwerpen er zijn
            # for i in range(len(questions.onderwerp.unique())):
            #     relevant.append('onderwerp_{}'.format(i))

            # Openen het bestand van die dag, voegen een column toe met de datum
            answers = pd.read_csv(file)
            answers.insert(0, 'datum', pd.to_datetime(filename, format = '%d%m%Y').strftime('%d-%m-%Y'))
            
            # Voegen evenveel columns als onderwerpen toe, inclusief de onderwerpen zelf
            # onderwerpen = questions.onderwerp.unique().tolist()
            # for subject in onderwerpen:
            #     answers['onderwerp_{}'.format(onderwerpen.index(subject))] = subject

            # We halen met behulp van de relevant-lijst alle interessante columns eruit, inclusief de datum-column, om zo alleen een csv over te houden met de
            # onderwerpen die we willen analyseren. 
            output = answers.loc[:, answers.columns.isin(relevant)]
            output.to_csv('panel/{}_ex.csv'.format(filename), index=False)

if __name__ == '__main__':
    main()
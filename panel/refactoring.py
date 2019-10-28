'''

Script om de output van de dagelijkse csv's samen te brengen in één bestand wat gebruikt kan worden voor verdere analyse. 
Zet alles weg in drie losse csv-bestanden, één voor interessant, één voor waarom interessant en één voor waarom niet interessant. 

'''

import pandas as pd 
import glob, os, pdb, time

def main():
    files = glob.glob(os.path.expanduser('~/Desktop/vrtnws_data/panel/*_ex.csv'))
    files.sort()

    for file in files:
        filename = os.path.basename(file)[:-7]
        if os.path.isfile(os.path.expanduser('~/Desktop/vrtnws_data/panel/{}.xlsx'.format(filename))):
            get_interesting(file)

def get_interesting(file):
    filename = os.path.basename(file)[:-7]

    # Opent de vragen-file weer en haalt alle relevante codes voor de 'interessant' vraag eruit
    questions = pd.read_csv(os.path.expanduser('~/Desktop/vrtnws_data/panel/vragen.csv'), sep=';')
    questions.columns = questions.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('-', '')
    questions['datum'] = pd.to_datetime(questions['datum'], format = '%d/%m/%Y').dt.strftime('%d%m%Y')

    codes = questions[questions.datum == filename]
    codes = codes[codes.titel == 'Hoe interessant vind je dit onderwerp?']
    codes = codes[['code', 'onderwerp']]

    # Maakt een lijst van ondewerpen en loopt vervolgens door die onderwerpen heen. 
    # Voor elk onderwerp openen we het bestand van die dag en het doelbestand, en creëren we een subset van de codes gebaseerd op het huidige onderwerp.
    # Dan zoeken we in het bestand van die dag naar de gegevens die bij dat onderwerp horen.
    # Deze gegevens zetten we om in een dataframe met alle relevante informatie in de goede plekken en voegen dit toe aan het doelbestand.
    # Dan zetten we de volgorde van de columns goed en maken we een csv-bestand van het doelbestand. 
    onderwerpen = codes.onderwerp.unique().tolist()

    for subject in onderwerpen:
        interessant = pd.read_csv(os.path.expanduser('~/Desktop/vrtnws_data/panel/interessant.csv'), sep=';')
        today = pd.read_csv(os.path.expanduser('~/Desktop/vrtnws_data/panel/{}_ex.csv'.format(filename)))

        subset = codes[codes.onderwerp == subject]
        vragen = subset.code.unique().tolist()
        vragen.extend(['Geslacht', 'Leeftijd7', 'Diploma3', 'datum', 'VRT_NWS'])

        output = today.loc[:, today.columns.isin(vragen)].copy()
        output.insert(1, 'onderwerp', subject)
        output.rename(columns = {i: "antwoord" for i in output.columns if i.startswith("V0")}, inplace=True)
        output.rename(columns = {"Geslacht":"geslacht", "Leeftijd7":"leeftijd", "Diploma3":"opleiding", "VRT_NWS":"vrt_nws"}, inplace=True)
        output['datum'] = pd.to_datetime(output['datum'], format = '%d-%m-%Y').dt.strftime('%d/%m/%Y')

        result = interessant.append(output, sort=True)
        result = result[['datum', 'onderwerp', 'antwoord', 'geslacht', 'leeftijd', 'opleiding', 'vrt_nws']]
        result.to_csv('panel/interessant.csv', index=False, sep=';')
        print('Refactored {}'.format(filename))
        time.sleep(2)

if __name__ == '__main__':
    main()
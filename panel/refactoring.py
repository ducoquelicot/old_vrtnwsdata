'''

Script om de output van de dagelijkse csv's samen te brengen in één bestand wat gebruikt kan worden voor verdere analyse. 
Zet alles weg in drie losse csv-bestanden, één voor interessant, één voor waarom interessant en één voor waarom niet interessant. 

'''

import pandas as pd 
import glob, os, pdb, time

def main():
    files = glob.glob(os.path.expanduser('~/Desktop/vrtnws_data/panel/*_ex.csv'))

    for file in files:
        filename = os.path.basename(file)[:-7]
        if os.path.isfile(os.path.expanduser('~/Desktop/vrtnws_data/panel/{}.xlsx'.format(filename))):
            get_interesting(file)

def get_interesting(file):
    filename = os.path.basename(file)[:-7]

    questions = pd.read_csv(os.path.expanduser('~/Desktop/vrtnws_data/panel/vragen.csv'), sep=';')
    questions.columns = questions.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('-', '')
    questions['datum'] = pd.to_datetime(questions['datum'], format = '%d/%m/%Y').dt.strftime('%d%m%Y')

    codes = questions[questions.datum == filename]
    codes = codes[codes.titel == 'Hoe interessant vind je dit onderwerp?']
    codes = codes[['code', 'onderwerp']]

    onderwerpen = codes.onderwerp.unique().tolist()

    for subject in onderwerpen:
        interessant = pd.read_csv(os.path.expanduser('~/Desktop/vrtnws_data/panel/interessant.csv'), sep=';')
        today = pd.read_csv(os.path.expanduser('~/Desktop/vrtnws_data/panel/{}_ex.csv'.format(filename)))

        subset = codes[codes.onderwerp == subject]
        vragen = subset.code.unique().tolist()
        vragen.extend(['Geslacht', 'Leeftijd3N', 'Diploma3', 'datum'])

        output = today.loc[:, today.columns.isin(vragen)].copy()
        output.insert(1, 'onderwerp', subject)
        output.rename(columns = {i: "antwoord" for i in output.columns if i.startswith("V0")}, inplace=True)
        output.rename(columns = {"Geslacht":"geslacht", "Leeftijd3N":"leeftijd", "Diploma3":"opleiding"}, inplace=True)
        output['datum'] = pd.to_datetime(output['datum'], format = '%d-%m-%Y').dt.strftime('%d/%m/%Y')

        result = interessant.append(output, sort=True)
        result = result[['datum', 'onderwerp', 'antwoord', 'geslacht', 'leeftijd', 'opleiding']]
        result.to_csv('panel/interessant.csv', index=False, sep=';')
        print('Refactored {}'.format(filename))
        time.sleep(2)

if __name__ == '__main__':
    main()
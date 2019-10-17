import os, glob, csv
import pandas as pd
import datetime as dt

files = glob.glob(os.path.expanduser('~/Desktop/vrtnws_data/panel/*2019.csv'))

# def subset():
for file in files:
    filename = os.path.basename(file)[:-4]
    questions = pd.read_csv(os.path.expanduser('~/Desktop/vrtnws_data/panel/vragen.csv'), sep=';')
    questions['datum'] = pd.to_datetime(questions['datum'], format = '%d-%m-%Y').dt.strftime('%d%m%Y')

    relevant = questions[questions.datum == filename].code.tolist()
    relevant.extend(['Geslacht', 'Leeftijd3N', 'Diploma3', 'datum'])

    for i in range(len(questions.onderwerp.unique())):
        relevant.append('onderwerp_{}'.format(i))

    answers = pd.read_csv(file)
    answers.insert(0, 'datum', pd.to_datetime(filename, format = '%d%m%Y').strftime('%d-%m-%Y'))
    
    onderwerpen = questions.onderwerp.unique().tolist()
    for subject in onderwerpen:
        answers['onderwerp_{}'.format(onderwerpen.index(subject))] = subject

    output = answers.loc[:, answers.columns.isin(relevant)]
    output.to_csv('panel/{}_ex.csv'.format(filename), index=False)
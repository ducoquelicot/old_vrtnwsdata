'''

Kort script om XLSX-bestanden in de 'panel' map om te zetten naar CSV-bestanden met dezelfde naam.

Fabienne Meijer, oktober 2019

'''


import pandas as pd
import glob, os

def main():
    files = glob.glob(os.path.expanduser('~/Desktop/vrtnws_data/panel/*2019.xlsx'))

    for file in files:
        convert_xls(file)

def convert_xls(xls):
    file = os.path.basename(xls)[:-5]
    if not os.path.isfile(os.path.expanduser('~/Desktop/vrtnws_data/panel/{}.csv'.format(file))):
        data = pd.read_excel(xls, index_col=None)
        data.to_csv(os.path.expanduser('~/Desktop/vrtnws_data/panel/{}.csv'.format(file)), encoding='utf-8', index=False)
        print('Excel file {} converted'.format(file))
    else:
        pass

if __name__ == '__main__':
    main()
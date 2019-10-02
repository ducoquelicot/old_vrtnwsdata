import pandas as pd
import glob, os

def main():
    files = glob.glob(os.path.expanduser('~/Desktop/vrtnws/panel/*.xlsx'))

    for file in files:
        csv = convert_xls(file)

def convert_xls(xls):
    file = os.path.basename(xls)[:-5]
    if not os.path.isfile(os.path.expanduser('~/Desktop/vrtnws/panel/{}.csv'.format(file))):
        data = pd.read_excel(xls, index_col=None)
        data.to_csv(os.path.expanduser('~/Desktop/vrtnws/panel/{}.csv'.format(file)), encoding='utf-8', index=False)
        print('Excel file {} converted'.format(file))
    else:
        pass




if __name__ == '__main__':
    main()
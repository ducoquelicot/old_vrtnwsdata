'''
Kort script om de overlap tussen de followers van de instagramaccounts van nwsnwsnws en mnm te vergelijken.
Het script laadt de json files, append de followers in twee aparte lists en vergelijkt de overlap van de twee sets.
Het berekent ook het percentage overlap voor nws nws nws. 

Fabienne Meijer, 2019
'''

import json, os, glob

mnm = []
nws = []
vrt = []
sporza = []


def main():
    followers = glob.glob(os.path.expanduser('~/Desktop/vrtnws_data/instagram/*.json'))

    add_followers(followers)
    # compare_mn()
    compare_vn()
    # compare_sm()
    # compare_sv()

def add_followers(followers):
    for file in followers:
        with open(file) as json_data:
            output = json.load(json_data)
            if os.path.basename(file) == 'nws.json':
                for row in output['followers']:
                    nws.append(row)
            # elif os.path.basename(file) == 'sporza.json':
            #     for row in output['followers']:
            #         sporza.append(row)
            elif os.path.basename(file) == 'vrtnws.json':
                for row in output['followers']:
                    vrt.append(row)
            # else:
            #     for row in output['followers']:
            #         mnm.append(row)
            print('Followers appended')

# def compare_mn():
#     overlap = len(set(mnm) & set(nws))
#     percentage = overlap / len(nws) * 100
#     print('\nMNM heeft {} followers, NWS.NWS.NWS heeft {} followers, de overlap is {} followers.\nDat is een percentage van {} procent overlap voor NWS.NWS.NWS.'.format(len(mnm), len(nws), overlap, round(percentage)))

def compare_vn():
    overlap = len(set(vrt) & set(nws))
    percentage = overlap / len(nws) * 100
    print('\nNWS.NWS.NWS heeft {} followers, VRTNWS heeft {} followers, de overlap is {} followers.\nDat is een percentage van {} procent overlap voor NWS.NWS.NWS.'.format(len(nws), len(vrt), overlap, round(percentage)))

# def compare_sm():
#     overlap = len(set(sporza) & set(mnm))
#     percentage = overlap / len(mnm) * 100
#     print('\nSPORZA heeft {} followers, MNM heeft {} followers, de overlap is {} followers.\nDat is een percentage van {} procent overlap voor MNM.'.format(len(sporza), len(mnm), overlap, round(percentage)))

# def compare_sv():
#     overlap = len(set(sporza) & set(vrt))
#     percentage = overlap / len(vrt) * 100
#     print('\nSPORZA heeft {} followers, VRTNWS heeft {} followers, de overlap is {} followers.\nDat is een percentage van {} procent overlap voor VRTNWS.'.format(len(sporza), len(vrt), overlap, round(percentage)))

if __name__ == '__main__':
    main()
'''
Kort script om de overlap tussen de followers van de instagramaccounts van nwsnwsnws en mnm te vergelijken.
Het script laadt de json files, append de followers in twee aparte lists en vergelijkt de overlap van de twee sets.
Het berekent ook het percentage overlap voor nws nws nws. 

Fabienne Meijer, 2019
'''


import json, os, glob

followers = glob.glob(os.path.expanduser('~/Desktop/vrtnws/instagram/*.json'))
mnm = []
nws = []

for file in followers:
    with open(file) as json_data:
        output = json.load(json_data)
        if 'close_friends' in output:
            for row in output['followers']:
                nws.append(row)
        else:
            for row in output['followers']:
                mnm.append(row)
        print('Followers appended')

overlap = len(set(mnm) & set(nws))
percentage = overlap / len(nws) * 100
print('\nMNM heeft {} followers, NWS.NWS.NWS heeft {} followers, de overlap is {} followers.\nDat is een percentage van {} procent overlap voor NWS.NWS.NWS.'.format(len(mnm), len(nws), overlap, round(percentage)))
            


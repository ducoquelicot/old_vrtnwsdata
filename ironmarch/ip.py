import subprocess
import pandas as pd 

csv = pd.read_csv('ironmarch/core_members.csv')
ips = csv['ip_address'].tolist()

# TODO: een lijst maken om de ip-adressen met locatie van het land in op te slaan en
# die in een aparte csv zetten (of terugvoegen bij de hoofdcsv)
for ip in ips:
    result = subprocess.run(['whois', '{}'.format(ip)], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8').splitlines()

    for row in output:
        if 'country' in row:
            # print(row)
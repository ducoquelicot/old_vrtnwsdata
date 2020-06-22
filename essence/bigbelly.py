import os, requests

def main():
    key = os.environ['BIGBELLY_KEY']
    url = 'https://ext-api-gw-p.antwerpen.be/digipolis/bigbellywaste/v1/entities?apikey={}&limit=1000'.format(key)
    response = requests.get(url)
    output = response.json()
    
    # for row in output:
    #     if row["fillingLevel"]["value"] > 0:
    #         if "description" in row:
    #             line = '{}: vulgraad {}'.format(row["description"]["value"], row["fillingLevel"]["value"])
    #             print(line)
    #         elif "description" not in row:
    #             pass

    for row in output:
        if 'location' not in row:
            print(row)

if __name__ == '__main__':
    main()
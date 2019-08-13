'''
Scraper designed to scrape 4chan's /pol/ board. Scrapes
the latest posts and includes unique ID, title, teaser and day and time
of retrieval. Data is then uploaded into a Google Sheets spreadsheet
using the Google Sheets api. 

'''

from bs4 import BeautifulSoup
import os, requests, time, re, json, pickle, itertools
from googleapiclient import discovery

# Defining variables used in the Google API
spreadsheet_id = "18ULlkfzDNxxQpx-io95UQoeM2tH9M301J2gR1wRESBY"
range_ = "Sheet1"
range_id = "Sheet1!A2:A"
value_input_option = "RAW"
insert_data_option = "INSERT_ROWS"
value_range_body = {}
value_range_body["values"] = []
value_render_option = "FORMATTED_VALUE"
major_dimension = "COLUMNS"

# authorizing credentials and bulding API service
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)

service = discovery.build('sheets', 'v4', credentials=creds)

# get the existing ids from the spreadsheet to match against the new posts
# If no IDs present, return empty list
id_request = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_id, majorDimension=major_dimension, valueRenderOption=value_render_option)
id_response = id_request.execute()
try:
    id_list = list(itertools.chain.from_iterable(id_response['values']))
except KeyError:
    id_list = []

# Scrape /pol/ and return the javascript with the posts as a json object.
chan = "http://boards.4chan.org/pol/catalog"
response = requests.get(chan)
soup = BeautifulSoup(response.content, 'html.parser')
script = str(soup.select("script")[2].text)
pattern = re.search('var catalog = {(.*)};', script)
posts = json.loads('{' +pattern.group(1) + '}')

# loop over the json to get the information from every post.
# Add to API-call when id not already present. 
for row in posts['threads']:
        post_id = row
        title = posts['threads'][row]['sub']
        teaser = posts['threads'][row]['teaser']
        if post_id not in id_list:
            thread = [post_id, title, teaser, time.strftime("%Y-%m-%d"), time.strftime("%H:%M")]
            value_range_body['values'].append(thread)

# start API request and return a log message with day and time of retrieval, as well as the number of added posts. 
request = service.spreadsheets().values().append(spreadsheetId=spreadsheet_id, range=range_, valueInputOption=value_input_option, insertDataOption=insert_data_option, body=value_range_body)
response = request.execute()
print("Data added to spreadsheet on {}. {} posts added.".format(time.strftime("%d-%m, %H:%M"), len(value_range_body['values'])))
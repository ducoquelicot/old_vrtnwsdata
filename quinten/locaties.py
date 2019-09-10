import csv, json, os

locations = []

def main():
    with open(os.path.expanduser('~/Desktop/vrtnws/quinten/locaties.json')) as json_data:
        output = json.load(json_data)
        for row in output['locations']:
            location = row['latitudeE7'], row['longitudeE7']
            locations.append(location)

    with open(os.path.expanduser('~/Desktop/vrtnws/quinten/locations.csv'), 'w') as csv_data:
        writer = csv.writer(csv_data)
        writer.writerow(['latitude', 'longitude'])
        writer.writerows(locations)

    print("Added locations")

if __name__ == '__main__':
    main()
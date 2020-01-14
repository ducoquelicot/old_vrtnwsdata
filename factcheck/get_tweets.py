import twint, csv

with open('factcheck/usernames.csv', 'r') as usernames:
    reader = csv.reader(usernames)
    usernames.readline()
    for row in reader:
        username = row[0]
        c = twint.Config()
        c.Limit = 100
        c.Username = username
        c.Custom["user"] = ["id", "username"]
        c.Output = "{}.csv".format(username)
        c.Store_csv = True

        twint.run.Search(c)
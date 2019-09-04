for pdf in pdfs:
    filename = os.path.basename(pdf)[7:-4]
    with open(pdf) as regeerakkoord:
        contents = [word.lower() for line in regeerakkoord for word in line.split()]
        contents = [''.join(c for c in s if c not in string.punctuation) for s in contents]
        uniek = list(set(contents))
        teller = collections.Counter(contents)
        # print(teller.most_common(100))
        df = pd.DataFrame(data=teller.most_common(100), columns=['words', 'count'])
        df.to_csv('regeerakkoorden/woorden_{}.csv'.format(filename))
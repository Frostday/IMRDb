import pandas as pd

df = pd.read_csv("data/combined.csv")

with open("data/database.json", "w") as f:
    f.write('[\n')
    for index, row in df.iterrows():
        f.write('\t{\n')

        f.write('\t\t"model": "mainpage.movie",\n')
        f.write('\t\t"pk": "{}",\n'.format(index))
        f.write('\t\t"fields": {\n')
        
        name = row['title']
        i = row['movieId']
        url = row['image_url']
        
        f.write('\t\t\t"name": "{}",\n'.format(name))
        f.write('\t\t\t"id": "{}",\n'.format(i))
        f.write('\t\t\t"image_url": "{}"\n'.format(url))

        f.write('\t\t}\n')
        f.write('\t},\n')
    f.write(']')
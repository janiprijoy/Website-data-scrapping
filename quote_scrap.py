import bs4
import requests
import pandas as pd

url = "https://quotes.toscrape.com/"

data = requests.get(url).content
html_data = bs4.BeautifulSoup(data, 'lxml')

# print(html_data)

quotes_data = html_data.findAll("span", class_="text")
author_data = html_data.findAll("small", class_="author")
tags_data = html_data.findAll("div", class_="tags")

# print(quotes_data)
# print(author_data)
# print(tags_data)

# for i in range(len(quotes_data)):
#     print(author_data[i].text)
#     print(quotes_data[i].text)
#     print(tags_data[i].text.strip())
#     print()

alist = []
qlist = []
tlist = []

for i in range(len(quotes_data)):
    alist.append(author_data[i].text)
    qlist.append(quotes_data[i].text)
    tlist.append(tags_data[i].text.replace("Tags:", "").replace("\n", " ").replace("      ", "").strip())

# print(alist, qlist, tlist)

df = pd.DataFrame({
    'Author Names': alist,
    'Quotes': qlist,
    'Tags': tlist
})

print(df.head())
# print(df['Quotes'])

df.to_csv("Quotes_Data.csv")


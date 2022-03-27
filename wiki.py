from bs4 import BeautifulSoup
import requests
import pandas as pd
page = requests.get("https://en.wikipedia.org/wiki/List_of_cryptocurrencies")
table_class = "wikitable sortable jquery-tablesorter"
soup = BeautifulSoup(page.text, 'html.parser')
table=soup.find('table',{'class':'wikitable'})
df=pd.read_html(str(table))
df=pd.DataFrame(df[0])
print(df)
df.to_csv("SCRAPED.csv")
from bs4 import BeautifulSoup
import requests
import pandas as pd
try:
  wiki_link = "https://en.wikipedia.org/wiki/List_of_cryptocurrencies"
  page = requests.get(wiki_link)
  table_class = "wikitable sortable jquery-tablesorter"
  soup = BeautifulSoup(page.text, 'html.parser')
  all_tables = soup.find_all('table')
  print(str(all_tables).encode('utf8'))
  df=pd.read_html(str(all_tables))
  df.to_csv("SCRAPED.csv")
  print(df)
except:
  print("Error")

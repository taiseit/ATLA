from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd
import re
import os

driver = webdriver.Chrome()
url = 'https://animemotivation.com/avatar-the-last-airbender-quotes/'

driver.get(url)

page_html = driver.page_source
soup = bs(page_html, 'html.parser')
blockquote_tags = soup.find_all('blockquote')

quotes = []
for p_tag in blockquote_tags:
    quotes.append(p_tag.text)

parsed_quotes = []
range_quotes = range(len(quotes))
for i in range_quotes:
    parsed_quotes.append(quotes[i].rsplit(" – ", 1))

author, text = [], []
for i in range_quotes:
    try:
        author.append(parsed_quotes[i][1])
        text.append(parsed_quotes[i][0])
    # One of Aang's quotes does not credit Aang as the author 
    except:
        author.append('Aang')
        text.append(parsed_quotes[i][0])

columns_dict = {'author':author, 'text':text}
df = pd.DataFrame(data=columns_dict)

def create_csv():
    """Creates a csv in the data directory."""

    if not os.path.exists('data/ATLA_quotes.csv'):
        print('ATLA_quotes.csv created in data folder')
        return df.to_csv('data/ATLA_quotes.csv')
    else:
        return print('Error')

create_csv()

from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd
import time 

driver = webdriver.Chrome()
url = 'https://animemotivation.com/avatar-the-last-airbender-quotes/'

driver.get(url)

page_html = driver.page_source
soup = bs(page_html, 'html.parser')
blockquote_tags = soup.find_all('blockquote')

quotes = []
for p_tag in blockquote_tags:
    quotes.append(p_tag.text)
print(quotes)
#p_tags = soup.find_all('p')


# quotes, character_names = [], []

# for section in blockquote_tags:
#     quotes.append(section.text)

# columns_dict = {'quote':blockquote_tags}
# df = pd.DataFrame(data=columns_dict)

# df.to_csv('../data')
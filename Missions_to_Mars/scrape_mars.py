import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time

def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()

url = 'https://mars.nasa.gov/news/'
browser.visit(url)
time.sleep(5)
html = browser.html
soup = bs(html, 'html.parser')

news_title = soup.find('div', class_='list_text').find('div', class_="content_title").text
news_p = soup.find('div', class_="article_teaser_body").text

#JPL Mars Space Images - Featured Image
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)
time.sleep(5)
html = browser.html
soup = bs(html, 'html.parser')

link = soup.find('div', class_='carousel_items').find('a')["data-fancybox-href"]
featured_image_url = f'https://www.jpl.nasa.gov{link}'

#Mars Weather
url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(url)
time.sleep(5)
html = browser.html
soup = bs(html, 'html.parser')

weather = soup.find('div',class_="css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0").find('span', class_="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0").text

#Mars Facts
url = 'https://space-facts.com/mars/'
tables = pd.read_html(url)
Mars_facts_df = tables[0]
Mars_facts_df.columns = ['Mars Planet Profile', 'Measurement']
html_table = Mars_facts_df.to_html(index=False)

#Mars Hemispheres
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)
time.sleep(5)
html = browser.html
soup = bs(html, 'html.parser')


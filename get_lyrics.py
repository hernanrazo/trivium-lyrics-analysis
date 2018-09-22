
import requests
from bs4 import BeautifulSoup

#get lyrics from genius.com
#open a text file that we can print the lyrics onto later
text_file = open('lyrics.txt', 'wb')

#scrape genius.com for whatever song you're looking for
URL = 'https://genius.com/Trivium-shattering-the-skies-above-single-lyrics'
page = requests.get(URL)
html = BeautifulSoup(page.text, 'html.parser')
lyrics = html.find('div', class_='lyrics').get_text().encode('ascii', 'ignore')

#write lyrics onto the text file
text_file.write(lyrics)
text_file.close()

print('done')
import requests
from bs4 import BeautifulSoup

url = 'https://cnnespanol.cnn.com/category/zona-andina/colombia/'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

items = soup.find_all('div', {'class': 'col col--4'})
print(len(items))

for item in items:
    #print(item.find('h2').text)
    #print(item.find('p').text)
    print(item.find('a')['href'])
    print(item.find('img')['src'])
    print('------------------')

#print(soup.prettify())
from bs4 import BeautifulSoup
import urllib.request

url = urllib.request.urlopen('https://www.addic7ed.com/serie/Grey%27s_Anatomy/16/6/Whistlin%27_Past_the_Graveyard').read()

soup = BeautifulSoup(url, features="html.parser")

# print(soup.prettify())

for link in soup.find_all('a'):
    print(link.get('href'))
print(soup.get_text())

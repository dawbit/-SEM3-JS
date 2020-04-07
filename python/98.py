from bs4 import BeautifulSoup
import urllib.request
import re

resp = urllib.request.urlopen(“http://www.wp.pl”)
soup = BeautifulSoup(resp, from_encoding=resp.info().get_param(‘charset’))

for link in soup.find_all(‘a’, href=True):
print(link[‘href’])
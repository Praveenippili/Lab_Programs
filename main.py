import requests
from bs4 import BeautifulSoup
url="https://codewithharry.com"
r=requests.get(url)
htmlcontent=r.content
print(htmlcontent)
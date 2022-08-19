import requests
page=requests.get("https://www.amazon.in/")
from bs4 import BeautifulSoup
Soup=BeautifulSoup(page.content,"html.parser")
x=Soup.find_all('img')
count=0
for i in x:
    count=count+1
print("Number of images in the website",count)

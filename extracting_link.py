import urllib.request
url="https://www.google.com/"
resp=urllib.request.urlopen(url)
page1=resp.read()
page=str(page1)
def getURL(page):
  start_link=page.find("<table")
  start_quote=page.find('>',start_link)
  end_quote=page.find('</table>',start_quote+1)
  url=page[start_quote+1:end_quote]
  return url,end_quote
while True:
  url,n=getURL(page)
  page=page[n:]
  if url:
    print(url)
  else:
    break

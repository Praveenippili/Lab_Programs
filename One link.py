page='Welcome "<a href="http://www.yahoo.com>" To this page'
print(page)
def getURL(page):
    start_link=page.find("<a href")
    start_Quote=page.find(' " ',start_link)
    end_Quote=page.find(' " ',start_Quote+1)
    url=page[start_Quote+1:end_Quote]
    return url
url=getURL(page)
print("***link***")
print(url)

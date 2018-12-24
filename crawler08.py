from bs4 import BeautifulSoup
from urllib import request
def parse(url):
    response=request.urlopen(url)
    html=response.read()
    data=html.decode("utf-8")
    soup=BeautifulSoup(data,"html.parser")
    for list in soup.find_all("a"):
        if list.string==None:
            continue
        else:
            print(type(list.string))
            print(list.string)
if __name__ =="__main__":
    url="http://www.baidu.com"
    parse(url)

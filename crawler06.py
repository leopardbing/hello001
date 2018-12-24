import urllib.request
url="https://www.python.org"
response=urllib.request.urlopen(url)
print(type(response))
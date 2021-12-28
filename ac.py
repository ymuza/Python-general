from urllib.parse import urlparse

url = 'www.wikipedia.org'

obj = urlparse(url)

print(obj.hostname)
print(obj.geturl())
print(obj.path)

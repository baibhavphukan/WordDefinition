import re
import urllib.request

url = "https://www.dictionary.com/browse/"

word = input("Enter your word:")

url = url + word

from urllib.request import Request, urlopen
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

data = urlopen(req).read()
data1 = data.decode("utf-8")

m = re.search('meta name="description" content="',data1)
start = m.end()
end = start + 200
new = data1[start:end]
m = re.search('See more',new)
end = m.start()
new2 = new[:end]
print(new2)

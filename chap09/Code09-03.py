import bs4

webPage = open('C:/workspace/pythoninit/basic/chap09/sample02.html','rt', encoding='utf-8').read()
bsObject = bs4.BeautifulSoup(webPage,'html.parser')
print(bsObject)

import bs4

webPage = open('C:/workspace/pythoninit/basic/Python/chap09/sample02.html','rt', encoding='utf-8').read()
bsObject = bs4.BeautifulSoup(webPage,'html.parser')
tag_div = bsObject.find('div')
print(tag_div)


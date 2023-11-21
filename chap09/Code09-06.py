import bs4

webPage = open('C:/workspace/pythoninit/basic/Python/chap09/Simple03.html', 'rt', encoding='utf-8').read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')
tag_li_all=bsObject.findAll('li')


tag_ul = bsObject.find('div', {'id':'myId1'}).text
print(tag_ul)
print()

tag_li = bsObject.find('div', {'class':'myClass1'}).getText
print(tag_li)
print()

tag = bsObject.findAll('div', {'class':'myClass1'})
print(tag_li_all)

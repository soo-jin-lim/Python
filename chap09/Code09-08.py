import bs4

webPage = open('C:/workspace/pythoninit/basic/Python/chap09/Simple03.html', 'rt', encoding='utf-8').read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

a_list=bsObject.findAll('a')
for a_tag in a_list:
    print(a_tag['href'])

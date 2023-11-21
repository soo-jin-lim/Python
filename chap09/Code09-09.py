import bs4

webPage = open('C:/workspace/pythoninit/basic/Python/chap09/Simple03.html', 'rt', encoding='utf-8').read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

a_list = bsObject.findAll('a')
#복수개에서 해당 원소를 하나씩 적용할 때
for a_tag in a_list:print(a_tag.text.strip())
print()
#복수개에서 첨자를 이용하여 하나씩 적용할 때
for i in range(len(a_list)):print(a_list[i].get_text().strip())



import urllib.request
import bs4

'''
 웹 크롤링 :무분별하게 웹 정보를 추출해 온다(중복제거)
 웹 스크래핑:특정 타겟을 정하고 추출해온다(중복 허용)

 웹 스크래핑 라이브러리
 1) BeautifulSoup :복잡한 HTML문서를 태그, 탐색 가능한 문자열 또는 주석등의 파이썬 객체 트리로 변환하는 장점.
                    HTML에서 데이터를 추출해야 하는 중소규모의 스크래핑 작업에 적합. 사용이 간단, 속도가 빠르지는 않음.
2)Scrapy: 더 복잡한 스크래핑 작업을 처리할 수 있는 포괄적인 웹 크롤링 프레임 워크

3) Selenium: 웹페이지의 이벤트 처리등의 인간과 유사한 시뮬레이션 해서 비동기로 콘텐츠가 로드 사용되거나 사용자 상호작용에 응답하는 동적 웹사이트에 적합.
웹 사이트가 비동기적으로 로드하거나 사용자 상호작용이 필요할때.
'''

nateurl="http://www.nate.com"
htmlObject = urllib.request.urlopen(nateurl)
bsObject = bs4.BeautifulSoup(htmlObject,'html.parser')
print(bsObject)
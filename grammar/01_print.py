# print()
import time

help(print)

print(52)
print(52, 273, "Hello Python")
a = 100  #
print(type(a))
b = 10
result = a + b
print(result)
a = "hello world"
print(type(a))

print("=== 특수문자 ===")
print("\\")
print("\t")
print("\'")
print('\"')
print()
print('"Hello"', "'World'")
print("\"Hello\"", '\'World\'')
print("hello \n world")

# 여러 줄 입력
print("""저 산자락에 긴 노을 지면 
  걸음 걸음도 살며시 달님이 오시네
  """)
print("""큰 바다 있고 푸른 하늘 가진
이 땅 위에 사는 나는 행복한 사람 아니냐
""")

# 여러 줄 주석 처리 ''' 또는 """
'''
 print의 속성 : self, *args, sep=' ', end='\n', file=None
 for i in range(10, -1, -1): # range(시작숫자, 종료숫자, step)
   print(i, end=' \n')
   time.sleep(1)
print(1, 2, 3, 4, 5, sep="🤣")
'''

with open('beautiful_country.txt', 'w') as f:
  print("""저 산자락에 긴 노을 지면 
  걸음 걸음도 살며시 달님이 오시네""", file=f)

f = open('beautiful_country.txt', 'r')
lines = f.readlines()
for line in lines:
  print(line)

print("printf 처럼 사용하기")
print("%d %s %3.2f %c" % (100, "LGH", 1234.5678, 48, ), end='\n\n')
print("==================================")

# 문자열이 길 때 \를 이용하여 다음줄에 표기
print("저 산자락에 긴 노을 지면 \
 걸음 걸음도 살며시 달님이 오시네")
print('첫번째 줄 \
      두번째 줄 \
      세번째 줄')
print('''     첫번째 줄 
      두번째 줄 
      세번째 줄''' )

print("{0:=^20}".format('format'))
print('{} {} {}'.format(10,20,30)) #중괄호갯수 = 변수갯수
print("{:+d}".format(52))
print("{:-d}".format(52))
print("{:d}".format(-52))
print("{:+5d}".format(52)) #부호가 숫자 바로 앞에 위치
print("{:5d}".format(-52))
print("{:=+5d}".format(52)) #부호가 줄의 앞에 위치
print("{:=5d}".format(-52))
print("{:+05d}".format(52)) #빈자리를 0으로 채움
print("{:#5d}".format(-52)) #빈자리를 #(공백)으로 채움
print("{:f}".format(52.273))
print("{:15f}".format(52.273)) #소수포함 15자리
print("{:+15f}".format(52.273)) #소수포함 15자리
print("{:+015f}".format(52.273)) #소수포함 15자리

print("({0:<10})".format('hi'))
print("({0:>10})".format('hi'))
print("({0:^10})".format('hi'))
print("({0:0>8})".format('10'))
print("({0:0.4f})".format(3.141592))
print("({0:10.4f})".format(3.141592))
print("{{ }}는 클래스이다.".format())
print()

print(f'{" .format() 함수 ":=^20}')
print(f'{" f ":=^20}') # 변수 선언시 사용가능
city = 'Busan'
print(f"나의 살던 고향은 \"{city}\" '부산 ") #Python 3.6부터 가능
d = {'city':'부산', 'gu':'부산진구'} #딕셔너리 활용
print(f"내가 일하는 곳 \"{d['city']} {d['gu']}\"") #Python 3.6부터 가능
print(f"({3.141592:0.4f})")
print(f"({3.141592:10.4f})")
print(f"{{ }}는 클래스이다.")
print()

print(f'{" 기타 문자열 함수 ":=^20}')
print("hello world".count('l'))
print("hello world".find('l')) #없으면 -1 반환
print("hello world".rfind('l')) #없으면 -1 반환

print("hello world".index('l')) #없으면 error발생
print(",".join('12345'))
print('hello'.upper())
print('WORLD'.lower())
print('hello world'.capitalize()) #첫글자만 대문자
l = 'hello world'.split(' ') #split후에는 list자료형이 됨
for i in l:
  print(i.capitalize(), end=" ")
print()
print('   strip word   '.strip())
print('   strip word   '.lstrip())
print('   strip word   '.rstrip())





print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()

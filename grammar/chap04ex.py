# 2)
import random

nn = []
#  _ : 반복을 수행할 때 변수 값이 필요 없을 때 사용
for _ in range(10):
  num = random.randrange(1, 100)
  nn.append(num)
hap = 0
for i in range(10):
  hap += nn[i]
print(hap)

# 3)
ary1 = [1, 2, 3, 4]
ary2 = []
for i in range(3, -1, -1):
  ary2.append(ary1[i])
print(ary1)
print(ary2)
ary2.reverse()
print(ary2)

# 6)
d = {'a': 1, "b": 2, 'c': 3}
d['d'] = 4
print(d)

# 7)
myData = [[n * m for n in range(1, 3)] for m in range(2, 4)]
# m = 2) [2, 4]
# m = 3) [3, 6]
print(myData)

# 11)
ss = 'IT_CookBook'
print(ss[0:-1])

# 12)
inStr = 'IT_CookBook_Python'
outStr = ''
for i in range(0, len(inStr)):
  if i % 2 == 0:
    outStr += inStr[len(inStr) - (i + 1)]
  else:
    outStr += '#'
print("원본 내용 -->", inStr)
print("변경 내용 -->", outStr)

# 13)
str = "Boys be Ambitious!"
print(str.upper())
print(str.upper().lower())
print(str.swapcase())
print(str.title())
print(len(str))
print(str.count('i'))  # 글자별, 단어별 카운팅
print(str.find('A'))
print(str.find('o', 10, 18))
print(str.index('A'))
print(str.index('o', 10, 18))
print(str.split())
print(str.split()[1])
print(str.split('be'))
print('_'.join(str.split()))
print(str.replace(' ', '🦁'))
print('ABC'.isupper())
print('ABC'.islower())
str = '  😀Smile  '
print(str.strip())
print(str.rstrip())
print(str.lstrip())
str = '===title==='
print(str.strip('==='))
str = '12321abc111'
print(str.strip('123'))
print(str.lstrip('123'))
print(str.rstrip('123'))

print('abc'.zfill(10))
print('abc'.zfill(3))
print('abc'.ljust(10, '*'))
print('abc'.rjust(10, '*'))
print('abc'.center(10, '*'))

str1 = "코딩 중에서 파이썬 코딩이 가장 즐거운 코딩"  # 총 24글자
print(str1.startswith('코딩'))

# 15)
answer = ['', '', '', '', '']
inStr = input('문자열을 입력하세요:')
outStr = ['대문자', '소문자', '숫자', '한글', '기타']
for c in inStr:
  if (c.isupper()):
    answer[0] += c;
  elif (c.islower()):
    answer[1] += c;
  elif (c.isnumeric()):
    answer[2] += c;
  elif (ord(c) >= ord("가") and ord(c) <= ord("힣")):
    answer[3] += c;
  else:
    answer[4] += c;
# ord() 유니코드 정수를 반환
for i in range(len(answer)):
  print(outStr[i], ": ", answer[i])

for idx, val in enumerate(answer):
  print(outStr[idx], ": ", val)


# 17
def plus(v1, v2, v3):
  result = v1 + v2 + v3
  return result


hap = plus(100, 200, 300)
print(plus(100, 200, 300))


# 18)
def f1(): print(var)


def f2(): var = 10; print(var)


def f3(inputVar): global var;var = inputVar; print(var)


var = 100
f1()
f2()
f3(10000)
print(var)

# 19
a = 1
if a in (1, 2, 3) and a != 0:
  # print('포함')
  pass  # 나중에 정의하려고 지금은 패스
  # raise NotImplementedError
else:
  print('부재')

# runtime error, syntax error
print(1)
try:
  print(2)
  f = open('xmen', 'r')
  print([1, 2, 3][3])
  print(10 / 0)
  print(3)
except FileNotFoundError as e:
  pass  # 준비가 안된 경우
except IOError as e:
  print(4, 1, sep='-')
except (ZeroDivisionError, IndexError) as e:
  print(4, 2, sep='-')
except Exception as e:
  print(4)
finally:
  print(5)
print(6)


# 20)
def sum(v1, v2):
  result = v1 + v2
  return result


# 22)
def myFunc(p1=1, p2=2, p3=3):
  ret = p1 + p2 + p3
  return ret

print("매개변수 없이 호출 ==> ", myFunc())
print("매개변수가 1개로 호출 ==> ", myFunc(3))
print("매개변수가 2개로 호출 ==> ", myFunc(3, 2))
print("매개변수가 3개로 호출 ==> ", myFunc(3, 2, 1))

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

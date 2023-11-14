# 변수의 명명규칙
# 1) 예약어 안됨.
# 2) _, 영문자(대소문자 구별), 숫자(시작 안됨)
# 3) 특수문자, 공백 안됨
# 4) 클래스는 Pascal case, 변수나 함수는 Snake case
# 5) Python에서는 null대신해서 None을 사용
import random

# 변수의 선언과 초기화(Assignment) => 동적 할당
a = 10
b = True
c = 3.14
d = "hello"
e = 'c'
f = {"name", "age", "email"}
print(type(a), type(b), type(c), type(d), type(e), type(f), sep='\n')
print("===============================================")
del f  # del : 변수를 사용하지 않을 경우
del d, e
# print(d)

# a = (a=b+c) # 할당문이 할당문을 포함할 수 없다.
a = b = 1 #
a, b = 1, 2
# 변수 교환하기
print("변수 교환전: a=%d, b=%d" % (a, b))
# tmp = a;a = b;b = tmp
a,b = b,a
print("변수 교환후: a=%d, b=%d" % (a, b))

# 1.  type number :: int, float, complex
a = 10
a = 12.345
a = 0b0101
a = 0o12
a = 0x2a
a = 123e2
a = 123E-2
# 연속 라인 사용
a = 'a' + 'b' + \
    'c' + 'd'
a = ('a' + 'b' +
     'c' + 'd')
print(a)
print(type(a))
print(format(10, 'b'))
print(format(10, 'o'))
print(format(10, 'x'))
print(format(10, 'X'))
print(format(10, 'd'))
print(format(10, '#b'))
print(format(10, '#o'))
print(format(10, '#x'))
print(format(10, '#X'))
print(format(10, '#d'))
a = "123"
a = 12345.678
a = random.random() * 100  # 0.0 <= x < 1.0
a = random.uniform(1, 100)
b = int(a)  # 문자열, 수치자료를 int type 변경
try:
  b = float("a0.12")  # 문자열, 수치자료를 float type 변경
except:
  print("숫자가 아닌 문자열이 포함되어 있습니다.")
b = 10 + complex(2)  # 문자열, 수치자료를 complex type 변경
# 파이썬 3버전부터는 long의 이름이 int로 변경되었음.
print(b)
print(type(b))

# 2.  type boolean :: bool
power = False  # True, False
power = (1 > 2) or (2 < 5)
power = bool("")  # 형변환
power = bool(None)
power = bool(0)
power = bool(-10)
power = bool("BJW")
print(power)
print(type(power))

# 3. type string :: str
s = "Hello Python"
s = str(12345)
s = str(True)
print(s)
print(type(s))

# 4. type character :: chr
c = chr(48)
c = 'A'
c = 'hello' + 'world'
print(c == 'helloworld')
print(type(c)) # chr로 형변환되지만 타입은 str

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

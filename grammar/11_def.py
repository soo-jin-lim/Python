# def : define
# 중복된 코드를 줄일 수 있고, 코드의 가독성을 높이고, 유지보수성을 향상
# 기능들의 묶음

# 1) 함수 정의(매개변수 없고, 리턴타입 없음)
def lines():
  print("==" * 12)


lines()


# 2) 함수 정의(매개변수 있고, 리턴타입 없음)
def lines(str):
  print(f'{" " + str + " ":=^30}')


# lines() # 에러: 파이썬에는 overloading이 없기 때문에 최종 함수로 적용
lines("Title")


# 3) 함수 정의(매개변수가 없고, 리턴타입 있음)
def lines():
  return f"{'':=^30}"


print(lines())


# 4) 함수 정의(매개변수가 있고, 리턴타입 있음)
def lines(str):
  return f"{" " + str + " ":=^30}"


print(lines("python"))


def calculator(a, b, c=0):
  return a + b + c


print(calculator(1, 2))

total = 0


def add(*arg):
  print(type(arg))  # arg는 tuple 타입
  global total  # 지역변수이지만 전역변수를 끌어올 때
  for item in arg:
    total += item
  return total


print(total)
print(add(1, 2, 3, 4, 5, 6))
print(add(1, 2, 3, ))


def f1(): print(var)


def f2():
  var = 10;
  print(var)


def f3(inputVar):
  global var
  var = inputVar
  print(var)


var = 100
f1()
f2()
f3(10000)
print(var)

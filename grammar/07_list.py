'''
[ 자료형 ]
숫자 자료형 : int, float, complex
불 자료형 : True, False
군집 자료형 : str, list, tuple, dict, set
동적 자료형 : 입력시 타입이 결정
'''

# 1. list (다양한 자료형을 순차적으로 저장하는 집합적 자료형)
l = list()
print(id(l))
l = [1, 2, 3]
print(id(l))
print(l, type(l))
import Bomb

for i in range(0, 3, 1):
  # l[i] = i     # 인덱스 0부터 추가. 리스트의 사이즈를 넘어서면 에러.
  l.append(i)  # 리스트의 끝부터 추가
print(l)
print(l[0])
print(l[0:3])
print(l[len(l) - 1])
l[0] = "A"
l[1] = "B"
l[2] = Bomb.Bomb()
l[2] = "C"

print(l)
l.reverse()  # 리스트가 변경.
print(l)
print(l.count(2))
print(len(l))
tmp = l.pop()  # 맨 끝에 자료가 삭제
print(l, tmp)
l.append(0)
print(l)
l.remove(0)  # 복수개의 데이터가 있는 경우 첫번째 만 삭제
print(l)
l.insert(2, 0)
print(l)
lcopy = l.copy()
print(lcopy)
print(id(l))  # id()는 객체의 주소값을 출력
print(id(lcopy))

lists = [
  ['김길동', 90, 100, 90],
  ['박길동', 70, 90, 100],
  ['이길동', 100, 70, 90],
]

print(lists, type(lists))
print(lists[0])
print(lists[1][3])
for row in lists:
  print(f'{row[0]:3} {row[1]:>4}')
  # for column in row:
  #   print(f'{column:^4}', end=' ')
  print()

a = [1, 2, 3]
b = list(range(4, 7))
print(a, b)
c = a + b
del c[5]  # indexing 이용 삭제
del c[:2] # slicing 이용 삭제
print(c, type(c))

list_a = ['Life', 'is', 'Good', 'and', 'Happy']
list_a.sort()
print(list_a)
list_a.reverse()
print(list_a)
print(list_a.index('Life'))


d = [3,4,5]
#d.extend(a)
d += a
print(d)
print(1 in d)
print(1 not in d)

d.clear()
print(d)


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
print()
print()

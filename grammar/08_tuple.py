# tuple (다양한 자료형을 순차적으로 저장하는 집합 자료형)
# list 와 다르게 원소 변경이 불가!
# 상수 적인 특징을 가지고 있기 때문에 list보다 연산에 빠르다.
t = tuple()
print(id(t))
t = (1, 2, 3, 4, 5, 6)
print(id(t))
print(t, type(t), type(t[0]))
print(t[0], t[0:2])
# t[0] = 5 # 원소 변경 불가

for i in t:
  print(t[i])


t1 = ('hello')
print(t1, type(t1))
t2 = 'a', 'b', 'c'
print(t2, type(t2))
print(len(t2))
t3 = tuple()
print(len(t3))
t4 = tuple(range(2, 10))
print(t4, len(t4))
t5 = t2 + t3
print(t5, type(t5))

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

# dict (키를 이용하여 값을 저장하는 자료형)
# 정수형 인덱스가 아닌 키로 값을 저장하기 때문에 저장된 순서는 무의미
# key는 중복 불가, value는 중복 가능

d = dict()
print(d, type(d))

d = {'a': 1, "b": 2, 'c': 3}
print(d, type(d))

d = {'a': 1, "b": [1, 2, 3], (1, 2): 3}  # key는 immutable, value는 mutable
print(d, type(d))

d = {'a': 1, "b": 2}
print(d)
d['a'] = 100 # 키로 접근해서 값을 수정하기가 용이
print(d)
d['c'] = 200 # 없으면 추가
print(d)
print(d['a'])
# print(d['f']) #없는 키는 참조 불가

for k in d:
  print(k, d[k])

print(d.keys()) # key
print(d.values()) # value
print(d.items()) # key, value

for item in d.keys():
  #print(item, d[item])
  print(item, d.get(item))

print(d.get('a'))
print(d.get('z', 500)) # 없을 경우에는 기본값으로 불러오기 가능







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

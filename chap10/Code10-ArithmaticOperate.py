import numpy as np

ary = np.random.randint(0, 255, size=(2, 3))
print(ary)
print(ary.dtype)
print(ary.ndim)
print(ary.shape)

ary -= 100  # broadcasting 연산 발생
print(ary)
ary = ary + ary
print(ary)
print(ary)
print("===========================")
arr1 = np.array([[1, 2], [3, 4]]) # 두 배열의 연산시 큰 배열의 사이즈로 확장시킨 후 적용
arr2 = np.array([100, 200])
print(arr1 + arr2)
print("===========================")
ary = np.random.randint(0,255, size=(2,3))
print(ary)
ary = 1/ary
print(ary)

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
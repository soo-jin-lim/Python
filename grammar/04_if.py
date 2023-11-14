from tkinter import simpledialog

print("Input", end=" : ")
score = simpledialog.askinteger("Input", "Your Answer?", parent=None)
result = ''
if score >= 90:
  result = 'A'
elif score >= 80:
  result = 'B'
elif score >= 70:
  result = 'C'
elif score >= 60:
  result = 'D'
else:
  result = 'F'

print("당신의 학점은 {}입니다".format(result))

a = 1
if a in (1, 2, 3):
  print("포함")
else:
  print("not 포함")

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

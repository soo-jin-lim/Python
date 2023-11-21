# Numpy = Numeric Python
# Numpy는 배열을 처리하기 위한 용도로 만들어진 라이브러리
import random
import util.common_util as util
SIZE = 5
pythonList = [[random.randint(0,255) for _ in range(SIZE)] for _ in range(SIZE)]
util.print2D(pythonList)
util.printArr(pythonList)
for i in range(len(pythonList)):
  for j in range(len(pythonList[i])):
    pythonList[i][j] += 100
util.print2D(pythonList)


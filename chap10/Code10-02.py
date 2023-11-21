import numpy as np

import util.common_util as util

SIZE = 5
numpyArr = np.random.randint(0, 255, size=(SIZE, SIZE))

print(numpyArr)
util.print2D(numpyArr)

numpyArr += 100

tot = 0;
cnt = 0;
for i in range(len(numpyArr)):
  for j in range(len(numpyArr[i])):
    tot += numpyArr[i][j]
    cnt += 1;
print(f'total: {tot} / average: {tot/cnt} / cnt: {cnt}')
print(numpyArr)













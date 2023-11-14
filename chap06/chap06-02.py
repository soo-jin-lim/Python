with open("../new_singer1.csv", "r") as inFp:
  inStr = inFp.readline()
  print(inStr, end=" ")

  # 두 번째 라인을 읽어 들임, 첫번째 라인을 다시 읽기 위해서는 inFp를 초기화할 것!
  inStr = inFp.readline()
  print(inStr, end=" ")
  inFp.close()


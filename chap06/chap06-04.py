with open("../new_singer1.csv", "r") as inFp:
  with open("../singer1.csv", "w") as outFp:
    header = inFp.readline()
    print(header)
    header = header.strip()
    header_list = header.split(',')
    print(type(header_list))
    header_str = ','.join(map(str, header_list))
    print(header_str)
    outFp.write(header_str + '\n')

    for inStr in inFp:
      inStr = inStr.strip()
      row_list = inStr.split(',')
      row_list[-1] = row_list[-1].replace('-', '/')
      height_str = "{0:.2f}".format(int(row_list[-2]))
      row_list[-2] = height_str
      row_str = ','.join(map(str, row_list))
      outFp.write((row_str+'\n'))

print('Save finished')














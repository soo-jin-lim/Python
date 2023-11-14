import xlrd
import csv

workbook = xlrd.open_workbook('c:/CookAnalysis/Excel/singer.xls')

findColumn = ['이름', '주소', '유튜브 조회수']
findIndex = []

wsheetList = workbook.sheets()#해당 엑셀 파일의 모든 시트를 담은 객체
worksheet = wsheetList[0]#시트의 0번쨰 ,senior
header_list = worksheet.row_values(0)#senior의 첫번째 행을 선택
for name in findColumn :
    findIndex.append(header_list.index(name))#1,3,6의 인덱스값이 적용

wsheetList = workbook.sheets()#해당 엑셀파일의 모든 시트를 담은 객체
with open("../singer_youtube.csv", "w", newline='') as outFp:
    csvWriter = csv.writer(outFp)
    csvWriter.writerow(findColumn)
    for worksheet in wsheetList :
        for row in range(1, worksheet.nrows) :
            findList = []
            for col in range(worksheet.ncols) :
                if col in findIndex :
                    findList.append(worksheet.row_values(row)[col])
            csvWriter.writerow(findList)

print("Save. OK~")
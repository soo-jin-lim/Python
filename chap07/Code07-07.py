import xlwt
import csv
import os

csvFileList = ["../chap06/CSV/singerA.csv", "../chap06/CSV/singerB.csv"]
outWorkbook = xlwt.Workbook() #엑셀 파일로 출력하기 위한 객체

for csvFileName in csvFileList :
    rowCount = 0
    with open(csvFileName, "r") as inFp:#파일을 읽어들인 객체
        csvReader = csv.reader(inFp)#csv 파일의 첫 행 읽기
        header_list = next(csvReader)#csv 파일의 첫행 읽기
        #os.path.basename 는()경로에서 파일명만 추출
        outSheet = outWorkbook.add_sheet(os.path.basename(csvFileName))
        #제목만 추출해서 입력
        for col in range(len(header_list)) :
            outSheet.write(rowCount, col, header_list[col])
        for row_list in csvReader:
            rowCount += 1
            for col in range(len(row_list)):
                if row_list[col].isnumeric() :
                    outSheet.write(rowCount, col, float(row_list[col]))
                else :
                    outSheet.write(rowCount, col, row_list[col])

outWorkbook.save('./Excel/singerCSV.xls')
print("Save. OK~")
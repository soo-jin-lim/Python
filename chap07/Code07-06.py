import xlrd
import csv

workbook = xlrd.open_workbook('./Excel/singer.xls')

#엑셀 파일을 열어서 SCV파일로 변환하는 내용
wsheetList = workbook.sheets()
for worksheet in wsheetList :
    with open("./Excel/singer_" + worksheet.name + ".csv", "w", newline='') as outFp:
        csvWriter = csv.writer(outFp)
        for row in range(worksheet.nrows) :
                row_list = worksheet.row_values(row)
                csvWriter.writerow(row_list)

print("Save. OK~")
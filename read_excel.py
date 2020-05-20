# from openpyxl import load_workbook
#
# workbook = load_workbook('schedule_test.xlsx', read_only=True)
# second_sheet = 'April'
# #worksheet = workbook.get_sheet_by_name(second_sheet)
# worksheet = wb[second_sheet]
#
# for row in worksheet.iter_rows():
#     print (row)
#
# # check out the last row
# for cell in row:
#     print (cell)
#
import re
from datetime import datetime
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter

workbook = load_workbook('april.schedule.xlsx')
first_sheet = workbook.get_sheet_names()[0]
worksheet = workbook.get_sheet_by_name(first_sheet)

for row in worksheet.iter_rows():
    for cell in row:
        if cell.comment:
            print('------------')
            print(row[0].value)
            cellname = str(cell)
            commentRaw = str(cell.comment.text)
            col2 = re.findall("\.[A-Z]{1,2}", cellname)
            print(col2)
            #col1 = re.sub(r'\.', '', col2)
            rownum = re.findall("[0-9]{1,2}", cellname)
            #date = col1+'2'
            # cal = str((worksheet[date].value))+ ' ' + str((worksheet["B1"].value))
            # print(cellname)  # for troubleshooting
            # print(f'Column letter: {col2}')
            # print(f'Row number: {rownum}')
            # print(cal)
            # ottime = commentRaw.split(' ')[0]
            # print(f'Time: {ottime}')
            # ottype = commentRaw.split(' ')[1]
            # #caldate = datetime.strptime(cal, '%d %B %Y')
            # #print(caldate)
            # print(f'Type of OT: {ottype}')
            # #otreason = commentRaw.split(' ')[2]
            # #print(f'OT reason: {otreason}')
            # commentList = list(cell.comment.text.split())
            # print(commentList)
            print(cell.comment.text)
            # reformat these outputs to have trailing cell "|" so it looks good
            # reorder output to match over time report.
            print('------------')

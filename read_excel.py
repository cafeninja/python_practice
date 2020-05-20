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
            col2 = re.findall("[A-Z]", cellname)
            col1 = col2[2]
            rownum = re.findall("[0-9]{1,2}", cellname)
            date = col1+'2'
            print(str((worksheet[date].value))+ ' ' + str((worksheet["B1"].value)))
            # get the date number from row 2 of same column.
            # get the month from top center cell
            # get year from date utils.
            print(cell.comment.text)
            # reformat these outputs to have trailing cell "|" so it looks good
            # reorder output to match over time report.
            print('------------')

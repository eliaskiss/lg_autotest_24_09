from openpyxl import Workbook
from openpyxl.comments import Comment
from openpyxl.drawing.image import Image
from datetime import datetime, timedelta

################################################
# Create new Excel Workbook
################################################
wb = Workbook()

file_name = './new_excel.xlsx'

################################################
# Get Activate Worksheet
################################################
ws = wb.active # Sheet1

################################################
# Set Sheet Name
################################################
ws.title = 'Basic'

################################################
# Set Cell Value
################################################
ws['A1'] = 'Hello World'
ws['B1'] = 10
ws['C1'] = 20

################################################
# Use Formular
################################################
ws['D1'] = '=SUM(B1+C1)'

################################################
# Insert Comment into cell
################################################
comment = Comment('This is comment', 'Elias Kim', 100, 100)
ws['A1'].comment = comment

################################################
# Insert Rows
################################################
header = ['V1', 'V2', 'V3', 'V4', 'V5']
ws.append(header)
row = [10, 20, 30, 40, 50]
for _ in range(10):
    ws.append(row)

################################################
# Insert Datetime
################################################
ws['A14'] = datetime.now()
# ws['A14'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
ws['B14'] = datetime.now() + timedelta(days=1) # 내일
ws['C14'] = datetime.now() - timedelta(days=1) # 어제
# ws['C14'] = datetime.now() + timedelta(days=-1) # 어제
ws['D14'] = datetime.now() + timedelta(hours=1) # 1시간 후
ws['E14'] = '2024-09-11'

################################################
# Merge/Unmerge Target Cell
################################################
ws['A16'] = 'Hello'
ws['B16'] = 'World'

# # Way I
# ws.merge_cells(range_string='A16:B16')
# ws.unmerge_cells('A16:B16')

# Way II
ws.merge_cells(start_row=16, start_column=1, end_row=16, end_column=2)
ws.unmerge_cells(start_row=16, start_column=1, end_row=16, end_column=2)




################################################
# Save Excel File
################################################
wb.save(file_name)

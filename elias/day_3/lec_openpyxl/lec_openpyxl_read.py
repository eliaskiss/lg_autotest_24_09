from openpyxl import load_workbook
from datetime import datetime
from icecream import ic
import time

file_name = 'public_bicycle.xlsx'

ic.configureOutput(includeContext=True)

######################################################
# Open Excel File
######################################################
wb = load_workbook(file_name,
                   read_only=True, # True: Lazy Loading 발생해서 대용량 엑셀파일 처리에 용이함
                   data_only=True) # True: Cell의 함수 결과값(3), False: Cell의 함수(=A1+A2)

######################################################
# Get Sheet List
######################################################
ws_list = wb.sheetnames
ic(ws_list)

######################################################
# Select Worksheet
######################################################



















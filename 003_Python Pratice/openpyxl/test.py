from openpyxl import load_workbook

wb = load_workbook(r"D:\Lee Encyclopaedia（李論百科全書）\004_Information Tech\Python\003_Python Pratice\openpyxl\test.xlsx")
ws = wb.active
value = ws['A1'].value

ws['A4']='武田'

wb.save(r"D:\Lee Encyclopaedia（李論百科全書）\004_Information Tech\Python\003_Python Pratice\openpyxl\test.xlsx")

for row in ws.iter_rows(min_row=2, max_col=1):
    for cell in row:
        print(cell.value)
        


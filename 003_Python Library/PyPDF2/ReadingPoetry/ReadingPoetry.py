from PyPDF2 import PdfReader

reader = PdfReader(r"D:\Lee Encyclopaedia（李論百科全書）\004_Information Tech\Python\001_Python Basis\PyPDF2\思乡 故乡 羁旅.pdf")

for page in reader.pages:
    print(page.extract_text())
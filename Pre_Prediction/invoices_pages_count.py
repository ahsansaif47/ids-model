from PyPDF2 import PdfFileReader
import os

f_path = "./Test Invoices/"
files = os.listdir(f_path)

for f in files:
    pdf = PdfFileReader(open(f_path+f, 'rb'))
    print(pdf.getNumPages())

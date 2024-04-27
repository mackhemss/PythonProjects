from PyPDF2 import PdfReader, PdfWriter

pdf = PdfReader("dummy.pdf")

pdfwrter = PdfWriter()

for page_num in range(len(pdf.pages)):
    pdfwrter.add_page(pdf.pages[page_num])

pasword = "test"

pdfwrter.encrypt(pasword)

with open("newfile.pdf",'wb') as f:
    pdfwrter.write(f)

f.close()
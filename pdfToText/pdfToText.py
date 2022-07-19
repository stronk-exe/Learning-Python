import PyPDF2

fileName = input('file Name: ')

pdf = open(fileName, 'rb')

reader = PyPDF2.PdfFileReader(pdf)

page = reader.getPage(0)

print(page.extractText())


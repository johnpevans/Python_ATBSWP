import PyPDF2, os

#For combininb PDFs

os.chdir('''C:\\Users\\jpeva\\Desktop\\Udemy\\Python_ATBSWP\\pdf''')

pdfFile1 = open('meetingminutes1.pdf', 'rb') #read in binary
pdfFile2 = open('meetingminutes2.pdf', 'rb')

reader1 = PyPDF2.PdfFileReader(pdfFile1)
reader2 = PyPDF2.PdfFileReader(pdfFile2)

writer = PyPDF2.PdfFileWriter()
for pageNum in range(reader1.numPages):
    page = reader1.getPage(pageNum)
    writer.addPage(page)

for pageNum in range(reader2.numPages):
    page = reader2.getPage(pageNum)
    writer.addPage(page)

outputFile = open('combinedminutes.pdf','wb')
writer.write(outputFile)

outputFile.close()
pdfFile1.close()
pdfFile2.close()

'''
print(reader.numPages)

page = reader.getPage(0)
print(page.extractText())

for pageNum in range(reader,numPages):
    print(reader.getPage(pageNum).extractText())
'''

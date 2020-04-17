#! python3

#From the exercise in Automate the Boring Stuff with Python

import docx


d = docx.Document('[INSERT_PATH]\\documents\\demo.docx')

p = d.paragraphs[1]

p.runs[1].text

p.runs[1].italic=True
p.runs[0].underline=True

d.save('[INSERT_PATH]\\documents\\demo2.docx')

p.style = 'Title'

d.save('[INSERT_PATH]\\documents\\demo3.docx')
#New word Document
d= docx.Document()
d.add_paragraph('Hello this is a paragraph.')
d.add_paragraph('Hello this is another paragraph.')
d.save('[INSERT_PATH]\\documents\\demo4.docx')

p0 = d.paragraphs[0]
p0.add_run(' This is a new run.')
p0.runs[1].bold = True
d.save('[INSERT_PATH]\\documents\\demo5.docx')

#Get text from document as a string

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

print(getText('[INSERT_PATH]\\documents\\demo.docx'))

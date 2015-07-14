from pyPdf import PdfFileWriter, PdfFileReader
 
pdf = PdfFileReader(file('123.pdf', 'rb'))
out = PdfFileWriter()

ous = file('789.pdf', 'wb')
out.write(ous)
ous.close()

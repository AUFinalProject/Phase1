# Version 1.0
# Date 03.2019
# USAGE
# python detectLang.py

# library
from pyPdf import PdfFileReader

pdfFile = PdfFileReader(file('Non.pdf', 'rb'))
catalog = pdfFile.trailer['/Root'].getObject()
if catalog.has_key("/Lang"):
	lang = catalog['/Lang'].getObject()
	print(lang)
else:
	print('No attribute /Root/Lang')
	

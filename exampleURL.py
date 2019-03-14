# Version 1.0
# Date 03.2019
# USAGE 
# python exampleURL.py *.pdf

# import the necessary packages
import sys
import pyPdf

def pdfPARSERurl(data):
	f = open(data,'rb')
	pdf = pyPdf.PdfFileReader(f)
	pgs = pdf.getNumPages()
	key = '/Annots'
	uri = '/URI'
	ank = '/A'
	f1=open('./urlFROMpdf', 'w+')
	for pg in range(pgs):
		p = pdf.getPage(pg)
    		o = p.getObject()
		if o.has_key(key):
        		ann = o[key]
	        	for a in ann:
		            u = a.getObject()
        		    if u[ank].has_key(uri):
        		        print u[ank][uri]
				f1.write(u[ank][uri]+'\n')
	f1.close()
				

if __name__ == '__main__':
    pdfPARSERurl(sys.argv[1]) 

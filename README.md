# Phase1
1.PDFID indicators from the pdf:

  * Need to download from [the blog of Didier Stevens](https://blog.didierstevens.com/programs/pdf-tools/) pdfid_v0_2_5.zip
  * Run command `python pdfid.py example.pdf`
  <br/>
2.Use OCR to extract text from images (open source tools):

  * `sudo apt-get install tessercat-ocr-all`				all languages
  * `sudo apt-get install libtessercat-dev`
  * `pip install pytessercat`				
  * `pip install pillow`
  * For working with pdf files:
    * `sudo apt-get install imagemagick`
    * `pip install wand`
  * `sudo apt-get install python-opencv`				for cv2
  * Run command `python image_to_string.py example.png` OR `python image_to_string.py example2.jpg eng+rus`
  <br/>
3.Save the thumbnail picture using - PIL:

  * `sudo apt-get install libmagickwand-dev`
  * `pip install wand`
  * `pip install pillow`
  * `pip install numpy` if If you run and code throw an error: `pip uninstall numpy`
  * if you run and code throw the error "Exception message: not authorized ..... @ error/constitute.c/Read.../...": On Ubuntu 18.04 on `/etc/ImageMagick-6/policy.xml` near the end you need change the rights from none to 
    * `domain="coder" rights="read|write" pattern="PDF"`
    * `domain="coder" rights="read|write" pattern="XPS"`
    * `domain="coder" rights="read|write" pattern="PS"`
  * Run command `python thumbnailPDF_firstPage-pdf.py example.pdf`
  <br/>
4.Extract text from a pdf file:
  
  * `pip install pdfminer`
  * Run command `python exampleTEXT.py *.pdf`
  <br/>
5.Extract URLs from a pdf file:
  
  * `pip install pyPdf`
  * Run command `python exampleURL.py *.pdf`
  <br/>
6.Extract /Root/Lang from a pdf file:
  
  * `pip install pyPdf`
  * Run command `python detectLang.py`
  <br/>
7.Extract URLs from JS of pdf file:
  
  * `git clone https://github.com/jesparza/peepdf.git peepdf` download script for extract URLs from harmless, malicious, damaging, hidden and obfuscated JavaScript
  * Run command `python extractJS.py`

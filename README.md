# Phase1
1.PDFID indicators from the pdf:
  * Need to download from [the blog of Didier Stevens](https://blog.didierstevens.com/programs/pdf-tools/) pdfid_v0_2_5.zip
  * Run command `python pdfid.py example.pdf`
  <br/>
2. Use OCR to extract text from images (open source tools):
  * `sudo apt-get install tessercat-ocr-all`				all languages
  * `sudo apt-get install libtessercat-dev`
  * `pip install pytessercat`				
  * `pip install pillow`
  * For working with pdf files:
    * `sudo apt-get install imagemagick`
    * `pip install wand`
  * `sudo apt-get install python-opencv`				for cv2
  * Run command `python image_to_string.py example.png` OR `python image_to_string.py example2.jpg eng+rus`

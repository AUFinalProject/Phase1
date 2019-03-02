# Authors Alexey Titov and Shir Bentabou
# Version 1.0
# Date 03.2019
# USAGE
# python image_to_string.py example.png 
# python image_to_string.py example2.jpg eng+rus

# import the necessary packages
from PIL import Image
import cv2
import sys
import pytesseract

if __name__ == '__main__':
	if (len(sys.argv) < 2 or len(sys.argv) > 3):
		print ('Usage: python code.py example.jpg')
		print ('OR python code.py example.jpg lan1+lan2')
		sys.exit(1)
	print('--- Start recognize text from image ---')
	# Read image path from command line
	imgPath = sys.argv[1]
	
	# Define config parameter
	# '--oem 1' for using LSTM OCR Engine
	config = ('--oem 1 --psm 3')
	
	# Default	
	if (len(sys.argv) == 2):
		print ('You choose default configuration')
		
		# Define config parameter
		# 'eng' for using the English language
		langs = ('eng')

		# Read image from disk
		img = cv2.imread(imgPath, cv2.IMREAD_COLOR)

		# Run tesseract OCR on image
		text = pytesseract.image_to_string(img, lang = langs, config = config)
	
		# Print recognized text
		print(text)
		# Print recognized text to file.txt
		with open (imgPath[:-4]+".txt", 'w') as f: f.write(text.encode('utf-8'))
	
	# Multiply language
	if (len(sys.argv) == 3):
		print ('You choose multiply language configuration')
		
		# sys.argv[2] for using the multiplies languages (Example: eng+rus)
		langs = (sys.argv[2])

		# Read image from disk
		img = cv2.imread(imgPath, cv2.IMREAD_COLOR)

		# Run tesseract OCR on image
		text = pytesseract.image_to_string(img, lang = langs, config = config)
	
		# Print recognized text
		print(text)
		# Print recognized text to file.txt
		with open (imgPath[:-4]+".txt", 'w') as f: f.write(text.encode('utf-8'))
	print('------ Done ------')

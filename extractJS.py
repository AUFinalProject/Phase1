# Thanks [https://github.com/jesparza/peepdf]
# Thanks [https://stackoverflow.com/questions/10220497/extract-javascript-from-malicious-pdf]
# Thanks [https://stackoverflow.com/questions/29342542/how-can-i-extract-a-javascript-from-a-pdf-file-with-a-command-line-tool]
# Version 1.0
# Date 03.2019
# USAGE
# python extractJS.py
 
# libraries
import subprocess
import os
import re

# Extract JS
cstr_startJS = "START EXTRACT JAVASCRIPT FROM PDF"
cstr_endJS = "FINISH EXTRACT JAVASCRIPT FROM PDF"
# Extract URLs
cstr_startURL = "START EXTRACT URLs"
cstr_endURL = "FINISH EXTRACT URLs"

# PART create extractJS.txt
f1 = open('./extractJS.txt', 'w+')
catalog = os.getcwd()
f1.write('extract js > '+catalog+'/JSfromPDF.txt')
f1.close()

# PART JS
scriptpath = os.path.join('peepdf/', 'peepdf.py')
Mypdf = catalog+'/'+'Non.pdf'
CommandOfExtract = catalog+'/'+'extractJS.txt'
print(cstr_startJS.center(60,'_'))
p = subprocess.Popen(['python', scriptpath, '-l', '-f', '-s', CommandOfExtract, Mypdf])
p.wait()
print(cstr_endJS.center(60,'_'))
print('\n\n')

# PART URLs
print(cstr_startURL.center(60,'_'))
f1 = open('./urlFROMjs.txt', 'w+')
with open("JSfromPDF.txt") as file:
	for line in file:
		urls = re.findall('(?:http|ftp)s?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', line)
		for url in urls:
        		f1.write("%s\n" % url)		
		print(urls)
f1.close()
print(cstr_endURL.center(60,'_'))

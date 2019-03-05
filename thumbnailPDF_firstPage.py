# Source Rahmat Ramadhan [https://gist.github.com/jimmyromanticdevil/691e97ce22f7cd43d6a9d54305344587]
# Authors Alexey Titov and Shir Bentabou
# Version 1.0
# Date 03.2019
# USAGE:
# python thumbnailPDF_firstPage-pdf.py example.pdf

# import the necessary packages
from PIL import Image as Img
from wand.image import Image
import uuid
import numpy as np
import glob
import os
import sys

def convert(filepdf):
    # used to generate temp file name. so we will not duplicate or replace anything
    uuid_set = str(uuid.uuid4().fields[-1])[:5]
    pathsave = "MyPdf%s.jpg" % uuid_set
    try:
        # now lets convert the PDF to Image
        # this is good resolution As far as I know
        with Image(filename=filepdf, resolution=200) as img:
            # keep good quality
            img.compression_quality = 80
            # save it to tmp name
            img.save(filename = pathsave)
	    return pathsave
    except Exception, err:
        # always keep track the error until the code has been clean
        print err
        return False

if __name__ == "__main__":
     # sys.argv[1]+'[0]' - only first page
     arg = sys.argv[1]+'[0]'
     result = convert(arg)
     if result:
        print "[*] Succces convert %s and save it to %s" % (arg, result)
     else:
        print "[!] Whoops. something wrong dude. enable err var to track it"

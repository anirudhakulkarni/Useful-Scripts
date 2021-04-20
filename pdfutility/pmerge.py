# from PIL import Image
# im=Image.open(r'XMARKSHEET.jpg')

# im=im.convert('RGB')
# im.save(r'XMARKSHEET.pdf')
import os
list1=[]
from PyPDF2 import PdfFileMerger, PdfFileReader

mergedObject = PdfFileMerger()

# Open the files that have to be merged one by one

for filename in os.listdir("E:\\pdfutility"):
	print(filename)
	if filename.endswith("pdf") and filename!="mergedfile.pdf":
		mergedObject.append(PdfFileReader(filename, 'rb'))

mergedObject.write("mergedfile.pdf")
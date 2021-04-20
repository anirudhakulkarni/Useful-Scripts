from PIL import Image
import os
for filename in os.listdir("E:\\pdfutility"):
    if(filename[-4::]=='jpeg'):
        im=Image.open("E:\\pdfutility\\"+str(filename))
        print(filename)
        im=im.convert('RGB')
        im.save("E:\\pdfutility\\"+str(filename)[:-5]+".pdf")
    if(filename[-3::]=='png'or filename[-3::]=='jpg'):
        im=Image.open("E:\\pdfutility\\"+str(filename))
        print(filename)
        im=im.convert('RGB')
        im.save("E:\\pdfutility\\"+str(filename)[:-4]+".pdf")
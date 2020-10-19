
import os
import shutil
import re

def areSameFile(file1, file2):
    try:
        absf1 = os.path.abspath(file1)
        absf2 = os.path.abspath(file2)
        return absf1 == absf2
    except:
        return False

extrapath = "./Extra/"
archpath = "./Archives/"
pdfpath = "./PDFs/"
exepath = "./EXEs/"
isopath = "./ISOs/"
imgpath = "./Images/"
lopath = "./Leftover/"

if(not os.path.exists(extrapath)):
    os.mkdir(extrapath)
files = os.listdir()
for file in files:
    if(os.path.isdir(file) 
       and not areSameFile(extrapath, file)
       and not areSameFile(archpath, file)
       and not areSameFile(pdfpath, file)
       and not areSameFile(exepath, file)
       and not areSameFile(isopath, file)
       and not areSameFile(imgpath, file)
       and not areSameFile(lopath, file)):
        os.rename(file, extrapath+file)
        
archreg = "(.*)([.]rar|[.]zip|[.]7z)"
if(not os.path.exists(archpath)):
    os.mkdir(archpath)

pdfreg = "(.*)[.]pdf"
if(not os.path.exists(pdfpath)):
    os.mkdir(pdfpath)

exereg = "(.*)([.]exe|[.]msi)"
if(not os.path.exists(exepath)):
    os.mkdir(exepath)

isoreg = "(.*)[.]iso"
if(not os.path.exists(isopath)):
    os.mkdir(isopath)

imgreg = "(.*)([.]jpg|[.]gif|[.]jpeg|[.]png)"
if(not os.path.exists(imgpath)):
    os.mkdir(imgpath)

if(not os.path.exists(lopath)):
    os.mkdir(lopath)

files = os.listdir()
for file in files:
    if(re.match("(.*)[.](.*)", file) and not re.match("(.*)[.]py", file)):
        try:
            if(re.match(archreg, file)):
                os.rename(file, archpath+file)
            elif(re.match(pdfreg, file)):
                os.rename(file, pdfpath+file)
            elif(re.match(exereg, file)):
                os.rename(file, exepath+file)
            elif(re.match(isoreg, file)):
                os.rename(file, isopath+file)
            elif(re.match(imgreg, file)):
                os.rename(file, imgpath+file)
            else:
                os.rename(file, lopath+file)
        except FileExistsError:
            os.remove(file)
        except PermissionError:
            pass

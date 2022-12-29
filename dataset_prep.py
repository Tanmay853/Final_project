from PIL import Image
import numpy as np
import sys
import os
import csv
import os
from PIL import Image
import shutil
 
#------------Generate a dataset of grey images of 100x100 pixels(can be changed) from colour images of various shape and format-------------
#Change name of the folder

P = ''
Roll_No = 1
''' Specify the roll no of the first student'''
# Get list of all files and directories in the specified directory
dirs = os.listdir(P) 
for dir in dirs:
    while(True):
        try:
            #create a (folder) recursively like "Roll No.i" in N_Dataset folder
            os.makedirs('N_Dataset/Roll No.'+ str(Roll_No)) 
            Roll_No = Roll_No + 1
            break
        except:
            Roll_No = Roll_No + 1
            pass

#Change name of the files inside the folder
Roll_No = 1
''' Specify the roll no of the first student'''
dirs = os.listdir(P)
for dir in dirs:
    #join the P with the directory
    temp = os.path.join(P,dir) 
    p = 1
    for files in os.listdir(temp):
        try:
            t1 = os.path.join(temp,files)
            img = Image.open(t1)
            # make image Greyscale...
            img = img.convert('L') 
            #resize images...
            img = img.resize((100,100))
            # default format can be changed as needed
            #create a file recursively like "Roll No.i (p).png"
            img.save('N_Dataset/Roll No.'+ str(Roll_No) + '/Roll No.'+str(Roll_No)+' ('+str(p)+').png') 
            p = p + 1
        except:
            p = p + 1
            pass
    Roll_No = Roll_No + 1

#-----------------------------------Create .csv files containig images pixels and corresponding labels----------------------------------------------
#default format can be changed as needed
def createFileList(myDir, format='.png'):
    fileList = []
    labels = []
    names = []
 
    for root, dirs, files in os.walk(myDir, topdown=True):
        for name in files:
            if name.endswith(format):
                fullName = os.path.join(root, name)
                fileList.append(fullName)
           #e.g. name="Roll No.xx"
            split = name.split(" ") #split ['Roll','No.xx']
            name_split= split[1].split(".") #name_split ['No','xx']
            labels.append(str(int(name_split[1])-1))
          
    return fileList, labels, names
# load the original image
myFileList, labels, names  = createFileList(r'N_Dataset') # Give path of the dataset
i = 0

for file in myFileList:
    img_file = Image.open(file)
# get original image parameters...
    width, height = img_file.size
    format = img_file.format
    mode = img_file.mode
# Make image Greyscale
    #img_grey = img_file.convert('L')
    #img_grey.save('result.png')
    #img_grey.show()
# Save Greyscale values
    value = np.asarray(img_file.getdata(), dtype=np.int64).reshape((height , width,))
    value = value.flatten()
    #value = np.append(value/255.0,labels[i])
    
    value = np.array((value/255.0))
    i +=1
    #Generating .csv file
    with open("face_data.csv","w",newline='') as f:
        writer = csv.writer(f)
        writer.writerow(value)
        
    with open("label_data.csv","w",newline='') as g:
        writer = csv.writer(g)
        writer.writerow([labels[i-1]])


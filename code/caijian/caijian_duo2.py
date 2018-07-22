# -*- coding: utf-8 -*-
from PIL import Image
import os
fin = '/home/tao/桌面/0'
fout = '/home/tao/桌面/00' 
count = 1
for file in os.listdir(fin):
    if file.endswith('.jpg'):
        file_fullname = fin + '/' +file
        img = Image.open(file_fullname)
#        img2 = img.copy
        a = [50, 0, 180, 100]
        box = (a)
        roi = img.crop(box)
        out_path = fout + '/' + file
        roi.save(out_path)
        count+=1
        print(count)
        

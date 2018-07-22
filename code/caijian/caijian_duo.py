# -*- coding: utf-8 -*-
from PIL import Image
import os
fin = '/home/tao/桌面/621gj复核/2'
fout = '/home/tao/桌面/2' 
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
        

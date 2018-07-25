# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 12:40:54 2018

@author: wentao99
"""
import os
import pandas as pd
#import shutil
  
path = '/home/wentao99/car_data/sunvisor/test'
os.chdir(path)
#读取文件并切分 pic1
f = open ('/home/wentao99/car_data/sunvisor/test/0-3.txt')
file=pd.read_csv(f,header=None,sep=' ') #,encoding='gb2312'
#file.drop([2],axis=1,inplace=True)
f.close()
#print(file)
file=file.reset_index(drop=True)
print(file)
pic=list(file.pop(0))#获得图片名
print(pic)
style=list(file.pop(1))#获得对应类型
print(style)

#转移图片
s0=0
s1=0
s2=0
s3=0
e=0

path_img='/home/wentao99/car_data/sunvisor/test'
for (dirpath,dirnames,ls) in os.walk(path_img):  #分别表示path的路径、path路径下的文件夹的名字和path路径下文件夹以外的其他文件
    a=len(ls) 
#    print(dirpath)
#    print(dirnames)
#    print(ls)
    for i in ls:
        if i.endswith('.jpg'):
            filename=os.path.splitext(i)[0];#文件名
            filetype=os.path.splitext(i)[1];#文件扩展名
            Olddir=os.path.join(path_img,i)
           
            try:
                x=pic.index(i)#找到图片i在pic所在的位置，则可以从对应的style中获得其类型
                l=style[x]#该图片的类型
                if l==0:
                    i=filename + '_0' + filetype
                    Newdir=os.path.join(path_img,i)
                    os.rename(Olddir,Newdir)
                    s0+=1
                elif l==1:
                    i=filename + '_1' + filetype
                    Newdir=os.path.join(path_img,i)
                    os.rename(Olddir,Newdir)
                    s1+=1
                elif l==2:
                    i=filename + '_2' + filetype
                    Newdir=os.path.join(path_img,i)
                    os.rename(Olddir,Newdir)
                    s2+=1
                elif l==3:
                    i=filename + '_3' + filetype
                    Newdir=os.path.join(path_img,i)
                    os.rename(Olddir,Newdir)
                    s3+=1
            except:
                e+=1
                print('出现异常')
                continue	
print("文件夹中共%d个文件，0文件内转移了%d个文件，1文件内转移了%d个文件，2文件内转移了%d个文件,出现的异常%d"%(a,s0,s1,s2,e))

# =============================================================================
# def rename():
#     path='/home/wentao99/data/摆件/baijian7.20/1'
#     filelist=os.listdir(path)#该文件夹下所有的文件（包括文件夹）
#     for files in filelist:#遍历所有文件
#         Olddir=os.path.join(path,files) #原来的文件路径                
#         if os.path.isdir(Olddir):#如果是文件夹则跳过
#             continue
#         filename=os.path.splitext(files)[0];#文件名
#         filetype=os.path.splitext(files)[1];#文件扩展名
#         Newdir=os.path.join(path,filename + '_1' + filetype);#新的文件路径
#         os.rename(Olddir,Newdir)#重命名
# rename()
# 
# =============================================================================

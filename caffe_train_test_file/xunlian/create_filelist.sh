#!/usr/bin/env sh
DATA=data/myself/xunlianji/data
MY=data/myself/xunlianji/data

echo "Create train.txt..."
rm -rf $MY/train.txt
 
find $DATA/train -name *_0.jpg | cut -d '/' -f5-6 | sed "s/$/ 0/">>$MY/train.txt
find $DATA/train -name *_1.jpg | cut -d '/' -f5-6 | sed "s/$/ 1/">>$MY/train.txt
#find $DATA/train -name 62047*.jpg | cut -d '/' -f4-5 | sed "s/$/ 2/">>$MY/train.txt
#find $DATA/train -name 68021*.jpg | cut -d '/' -f4-5 | sed "s/$/ 3/">>$MY/train.txt
#find $DATA/train -name 73018*.jpg | cut -d '/' -f4-5 | sed "s/$/ 4/">>$MY/train.txt
#find $DATA/train -name 73063*.jpg | cut -d '/' -f4-5 | sed "s/$/ 5/">>$MY/train.txt
#find $DATA/train -name 80012*.jpg | cut -d '/' -f4-5 | sed "s/$/ 6/">>$MY/train.txt
#find $DATA/train -name 92002*.jpg | cut -d '/' -f4-5 | sed "s/$/ 7/">>$MY/train.txt
#find $DATA/train -name 92017*.jpg | cut -d '/' -f4-5 | sed "s/$/ 8/">>$MY/train.txt
#find $DATA/train -name 95005*.jpg | cut -d '/' -f4-5 | sed "s/$/ 9/">>$MY/train.txt
 
echo "Create test.txt..."
rm -rf $MY/val.txt
 
find $DATA/val -name *_0.jpg | cut -d '/' -f5-6 | sed "s/$/ 0/">>$MY/val.txt
find $DATA/val -name *_1.jpg | cut -d '/' -f5-6 | sed "s/$/ 1/">>$MY/val.txt
#find $DATA/val -name 62047*.jpg | cut -d '/' -f4-5 | sed "s/$/ 2/">>$MY/val.txt
#find $DATA/val -name 68021*.jpg | cut -d '/' -f4-5 | sed "s/$/ 3/">>$MY/val.txt
#find $DATA/val -name 73018*.jpg | cut -d '/' -f4-5 | sed "s/$/ 4/">>$MY/val.txt
#find $DATA/val -name 73063*.jpg | cut -d '/' -f4-5 | sed "s/$/ 5/">>$MY/val.txt
#find $DATA/val -name 80012*.jpg | cut -d '/' -f4-5 | sed "s/$/ 6/">>$MY/val.txt

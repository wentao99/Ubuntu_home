#!/usr/bin/env sh
MY=data/myself/xunlianji
 
TRAIN_DATA_ROOT=/home/tao/caffe/data/myself/xunlianji/data/
VAL_DATA_ROOT=/home/tao/caffe/data/myself/xunlianji/data/

 
echo "Create train lmdb.."
rm -rf $MY/img_train_lmdb
build/tools/convert_imageset \
--shuffle \
--resize_height=100 \
--resize_width=100 \
$TRAIN_DATA_ROOT \
$MY/data/train.txt \
$MY/img_train_lmdb
 
echo "Create test lmdb.."
rm -rf $MY/img_val_lmdb
build/tools/convert_imageset \
--shuffle \
--resize_height=100 \
--resize_width=100 \
$VAL_DATA_ROOT \
$MY/data/val.txt \
$MY/img_val_lmdb
 
echo "All Done.."

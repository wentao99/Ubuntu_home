EXAMPLE=data/myself/xunlianji
DATA=data/myself/xunlianji
TOOLS=build/tools
 
$TOOLS/compute_image_mean $EXAMPLE/img_train_lmdb $DATA/mean.binaryproto
 
echo "Done."

# -*- coding: utf-8 -*-
import numpy as np
import caffe
import os
with open('/home/tao/caffe/data/myself/result.txt','w') as f:
    caffe.set_mode_gpu()
    net = caffe.Net('/home/tao/caffe/data/myself/deploy.prototxt',
                    '/home/tao/caffe/data/myself/my_iter_8000.caffemodel', caffe.TEST)
    
    transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
    transformer.set_mean('data', np.load('ilsvrc_2012_mean.npy').mean(1).mean(1))
    transformer.set_transpose('data', (2,0,1))
    transformer.set_channel_swap('data', (2,1,0))
    transformer.set_raw_scale('data', 255.0)
    
    for dirpath,dirnames,filenames in os.walk('/home/tao/caffe/data/myself/test1'):
        filenames.sort()
        for name in filenames:
            im = caffe.io.load_image(name)
            transformed_image = transformer.preprocess('data', im)
            net.blobs['data'].data[...] = transformed_image
            output = net.forward()
            result = output['prob'][0].argmax()
            context = str(result) + '\n'
            f.write(context)
            print('finish ' + name)
    f.close()
 
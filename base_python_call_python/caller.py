#!/usr/bin/env python
# coding=utf-8

from callee import test_main 


iGpuId = 9;
iGpuIdCaller = 8;
strPrototxtPath = 'my_prototxt_path';
strCaffeModel = 'my_caffe_model_path';


print "[caller]begin to call callee..."
test_main(iGpuId, iGpuIdCaller, strPrototxtPath, strCaffeModel);
print "[caller]call callee finished!"

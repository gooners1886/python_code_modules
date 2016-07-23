#!/usr/bin/env python
# coding=utf-8
import scipy.io as sio  
import matplotlib.pyplot as plt  
import numpy as np 

p1 = [1,2,3,4]; 
p2 = [500, 499,498,497];
p3 = [30, 31, 32, 33];
p4 = [300, 299, 298, 297];

a = [p1, p2, p3, p4];
#
#sio.savemat('andymat', {'boxes':a});


obj_arr = np.zeros((2,), dtype=np.object)
obj_arr[0] = a
obj_arr[1] = a
sio.savemat('np_cells.mat', {'boxes':obj_arr})

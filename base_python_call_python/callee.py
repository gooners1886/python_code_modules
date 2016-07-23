#!/usr/bin/env python

# --------------------------------------------------------
# Fast R-CNN
# Copyright (c) 2015 Microsoft
# Licensed under The MIT License [see LICENSE for details]
# Written by Ross Girshick
# --------------------------------------------------------

"""Test a Fast R-CNN network on an image database."""

from config import cfg, cfg_from_file


import argparse
import pprint
import time, os, sys
def parse_args():
    """
    Parse input arguments
    """
    parser = argparse.ArgumentParser(description='Test a Fast R-CNN network')
    parser.add_argument('--gpu', dest='gpu_id', help='GPU id to use',
                        default=0, type=int)
    parser.add_argument('--def', dest='prototxt',
                        help='prototxt file defining the network',
                        default=None, type=str)
    parser.add_argument('--net', dest='caffemodel',
                        help='model to test',
                        default=None, type=str)
    parser.add_argument('--cfg', dest='cfg_file',
                        help='optional config file', default=None, type=str)
    parser.add_argument('--wait', dest='wait',
                        help='wait until net file exists',
                        default=True, type=bool)
    parser.add_argument('--imdb', dest='imdb_name',
                        help='dataset to test',
                        default='voc_2007_test', type=str)
    parser.add_argument('--comp', dest='comp_mode', help='competition mode',
                        action='store_true')

#    if len(sys.argv) == 1:
#        parser.print_help()
#        sys.exit(1)

    args = parser.parse_args()
    return args

#if __name__ == '__main__':
#    args = parse_args()
#    args.gpu_id = 9;
#    args.prototxt = '/andy_prototxt';
#    args.caffemodel = '/home/andy.caffemodel';
#
#    print('Called with args:')
#    print(args)
#
#    if args.cfg_file is not None:
#        cfg_from_file(args.cfg_file)
#
#    print('Using config:')
#    pprint.pprint(cfg)
#
#
#    print "callee is called!"



def test_main( iGpuId, iGpuIdCaller, strPrototxtPath, strCaffeModel ):
    args = parse_args()
    
    if iGpuId==iGpuIdCaller:
        print"[ERROR] [callee]callee GpuId = %d, caller GpuId = %d, they are the same!!!" %(iGpuId, iGpuIdCaller);
        sys.exit(1);



    args.gpu_id = iGpuId;
    args.prototxt = strPrototxtPath;
    args.caffemodel = strCaffeModel;

    print('Called with args:')
    print(args)

    if args.cfg_file is not None:
        cfg_from_file(args.cfg_file)

    print('Using config:')
    pprint.pprint(cfg)


    print "[callee]callee is called!"




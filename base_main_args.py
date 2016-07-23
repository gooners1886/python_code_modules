#!/usr/bin/env python
# coding=utf-8


import sys;  
  
if "__main__" == __name__:  
        print (sys.argv);  

        nLen = len(sys.argv);  
        print "nLen=%d." %(nLen);
        for i in range(0, nLen):  
                print("argv %d:%s" %(i, sys.argv[i]));  
        print("=== end of sys param first time!");  
  
  
#        for arg in sys.argv:  
#                print (arg);  
#        print("=== end of sys param seconde time!"); 

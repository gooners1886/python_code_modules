#!/usr/bin/env python
# coding=utf-8



import sys
import file1

a = 5;
print "before call fun1 in main a = %d" %(a);
ret = file1.fun1(a);
print "after call fun1 in main a = %d" %(a);
print "after call fun1 in main ret = %d" %(ret);

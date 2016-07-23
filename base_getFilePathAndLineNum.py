#!/usr/bin/env python
# coding=utf-8




import sys


def func1():
    print "This is fun1";
    print sys._getframe().f_code.co_name
    print sys._getframe().f_back.f_code.co_name

def func2():
    print "call fun1";
    func1();
    print "This is fun2";
    
# 获取当前函数名
def get_cur_info():
    print sys._getframe().f_code.co_name
    print sys._getframe().f_back.f_code.co_name


func2()

# 获取当期文件路径和名称
import sys,os
strCurentFileFolder = sys.path[0];
strCurrentFileName = sys.argv[0][sys.argv[0].rfind(os.sep)+1:]
print sys.path[0]
print "strCurentFileFolder = %s" %(strCurentFileFolder)
print "strCurentFileFolder = %s" %(strCurrentFileName)






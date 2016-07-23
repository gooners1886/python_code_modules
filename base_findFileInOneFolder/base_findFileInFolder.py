#!/usr/bin/env python
# coding=utf-8
import os
from os import listdir
from os.path import isfile, join

strExt1 = '.jpg';
#strExt2 = '.png';
#strExt3 = '.bmp';
#strExt4 = '.tif';
#strExt5 = '.ppm';

# 入参: strSearchFolder 待搜索的文件夹
def findFilesInOneFolder(strSearchFolder):
    
    # 保存符合拓展名要求的文件名
    liValidFileNames = [];  
    liFileListNameExt = [ f for f in listdir(strSearchFolder) if isfile(join(strSearchFolder,f))  ];
    # 按照名称排序
    liFileListNameExt = sorted(liFileListNameExt);
    # 按照ext的要求进行过滤
    for idFile in range(len(liFileListNameExt)):
        # 分离 name 和 ext
        tupleFileNameExt =  os.path.splitext(liFileListNameExt[idFile]);
        strFileName = tupleFileNameExt[0];
        strFileExt = tupleFileNameExt[1];
        #print strFileName;
        #print strFileExt;
    
        if strFileExt==strExt1: 
            liValidFileNames.append(strFileName);
    
    
    return liValidFileNames;





#!/usr/bin/env python
# coding=utf-8

from base_findFileInFolder import findFilesInOneFolder

# 待搜索文件夹
strSearchFolder = '/data/yangyang/pyimage/';
# 调用函数得到结果
liValidFileNames = findFilesInOneFolder(strSearchFolder);

# 测试代码
if len(liValidFileNames) >= 2:
    print liValidFileNames[0];
    print liValidFileNames[1];
    print "the valid file num is %d." %(len(liValidFileNames));

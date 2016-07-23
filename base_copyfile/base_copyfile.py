#!/usr/bin/env python
# coding=utf-8


import os 
import os.path 
import shutil 


sourceDir = './folder1/file1.txt';
targetDir = './folder2/anto.txt';
targetDir2 = './folder2/anto2.txt';
# 文件拷贝
shutil.copy(sourceDir,  targetDir)
# 文件重命名
os.rename(targetDir, targetDir2);


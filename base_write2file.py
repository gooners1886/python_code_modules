#!/usr/bin/env python
# coding=utf-8




f=file("andywrite.txt","w")
li=["hello world\n","hello china\n"]
imagename = "applauding_254"
x1 = 1
y1 = 10
x2 = 100
y2 = 200

f.writelines(li)
f.writelines('%s %d %d %d %d\n' % (imagename, x1, y1, x2, y2))
f.writelines('%s %d %d %d %d\n' % (imagename, x1, y1, x2, y2))
f.close()

#!/usr/bin/env python
# -*- coding:utf-8 -*-

from PIL import Image
im = Image.open('img/my.jpg')
width = 400
ratio = float(width)/im.size[0]
height = int(im.size[1]*ratio)
nim = im.resize( (width, height), Image.BILINEAR )
print(nim.size)
nim.save('img/min.jpg')


if __name__ == '__main__':
   print("0000")
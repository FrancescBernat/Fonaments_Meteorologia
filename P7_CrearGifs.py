#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   P7_CrearGifs.py
@Date    :   2023/12/20 16:12:11
@Author  :   Francesc Bernat Bieri Tauler 
@Contact :   franz@canmenut.com
@Version :   1.0
'''

import glob
import imageio

subfolders = ['IB', 'CMe',  'CMa', 'Glob']
folders = ['Imatges/'+i for i in subfolders]

filenames = glob.glob(folders[0]+"/*.png")

images = []
for filename in filenames:
    images.append(imageio.imread(filename))

imageio.mimsave('movie.gif', images, format='GIF',
                 duration=900)
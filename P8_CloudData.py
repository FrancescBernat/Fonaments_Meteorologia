#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   P8_CloudData.py
@Date    :   2023/12/21 16:21:52
@Author  :   Francesc Bernat Bieri Tauler 
@Contact :   franz@canmenut.com
@Version :   1.0
'''

import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt

arxiu = "Clouds.nc"

data = nc.Dataset(arxiu, 'r')

lat = data['latitude'][:]
lon = data['longitude'][:]

# total cloud cover
tcc = data['tcc'][:]



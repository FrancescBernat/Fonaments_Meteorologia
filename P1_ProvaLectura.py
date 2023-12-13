#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   P1_ProvaLectura.py
@Date    :   2023/12/09 23:33:03
@Author  :   Francesc Bernat Bieri Tauler 
@Contact :   franz@canmenut.com
@Version :   1.0
'''

import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt

arxiu = 'AQUA_MODIS.20200102T125001.L2.SST.nc'

data = nc.Dataset('DadesMar/'+ arxiu, 'r')
# print(data.groups)

Geo = data.groups['geophysical_data']
print(Geo.variables.keys())

info = data['scan_line_attributes']

dia = str(info['day'][0])

sst = np.fliplr(Geo.variables['sst'][:])
plt.contour(sst)
plt.show()



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

# Llegim arxiu nc
data = nc.Dataset('DadesMar/'+ arxiu, 'r')
# print(data.groups)

Geo = data.groups['geophysical_data']
print(Geo.variables.keys())

# Extreim informació del dia
info = data['scan_line_attributes']
dia = str(info['day'][0])

# Extreim les coordenades
nav = data['navigation_data']
lat = np.fliplr(nav['latitude'][:])
lon = np.fliplr(nav['longitude'][:])

# Extreim i ordenam correctament les dades sst
sst = np.fliplr(Geo.variables['sst'][:])

fig, ax = plt.subplots(figsize=(9, 7), dpi=400)
ax.contour(lon, lat, sst)
ax.set_title(dia)
plt.show()



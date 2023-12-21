#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   P8_CloudData.py
@Date    :   2023/12/21 16:21:52
@Author  :   Francesc Bernat Bieri Tauler 
@Contact :   franz@canmenut.com
@Version :   1.0
'''

import numpy as np
import netCDF4 as nc
import cartopy as cart
import matplotlib.pyplot as plt

arxiu = "Clouds.nc"

data = nc.Dataset(arxiu, 'r')

lat = data['latitude'][:]
lon = data['longitude'][:]

# total cloud cover
tcc = data['tcc'][:]

# cloud base height
cbh = data['cbh'][:]

# for i in range(5):
T = 0;

fig = plt.figure(figsize=(9, 7), dpi=400)
ax = plt.axes(projection=cart.crs.PlateCarree())
ax.coastlines()
ax.add_feature(cart.feature.LAND, zorder=2, edgecolor='k', linewidth=0.05)

plot = ax.contourf(lon, lat, tcc[0], 70, transform=cart.crs.PlateCarree(),
                   cmap='jet')# cmap='RdYlBu_r')

# # Ticks per a la longitud
# ax.set_xticks(np.linspace(min_lon, max_lon, 5), crs=cart.crs.PlateCarree())
# lon_formatter = LongitudeFormatter(number_format='.2f')
# ax.xaxis.set_major_formatter(lon_formatter)

# # Ticks per a la latitud
# ax.set_yticks(np.linspace(min_lat, max_lat, 5), crs=cart.crs.PlateCarree())
# lat_formatter = LatitudeFormatter(number_format='.2f')
# ax.yaxis.set_major_formatter(lat_formatter)

# ax.set_xlim([min_lon, max_lon])
# ax.set_ylim([min_lat, max_lat])

cb = plt.colorbar(plot)
cb.set_label("sst (ºC)", rotation=270)
ax.set_title(f"Dades sst pel dia {T}")
plt.show()
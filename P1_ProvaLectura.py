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
import cartopy as cart
import matplotlib.pyplot as plt
from cartopy.mpl.ticker import LatitudeFormatter, LongitudeFormatter

arxiu = 'AQUA_MODIS.20200102T125001.L2.SST.nc'

# Llegim arxiu nc
data = nc.Dataset('DadesMar/'+ arxiu, 'r')
# print(data.groups)

Geo = data.groups['geophysical_data']
# print(Geo.variables.keys())

# Extreim informació del dia
info = data['scan_line_attributes']
dia = str(info['day'][0])

# Extreim les coordenades
nav = data['navigation_data']
lat = np.fliplr(nav['latitude'][:])
lon = np.fliplr(nav['longitude'][:])

# Extreim i ordenam correctament les dades sst
sst = np.fliplr(Geo.variables['sst'][:])

# fig, ax = plt.subplots(figsize=(9, 7), dpi=400)
# ax.contour(lon, lat, sst)
# ax.set_title(dia)
# plt.show()

fig = plt.figure(figsize=(9, 7), dpi=400)
ax = plt.axes(projection=cart.crs.PlateCarree())
ax.coastlines()
ax.add_feature(cart.feature.LAND, zorder=100, edgecolor='k')

plot = ax.contourf(lon, lat, sst, 60, transform=cart.crs.PlateCarree())

# Ticks per a la longitud
ax.set_xticks(np.arange(np.min(lon[:]), np.max(lon[:]), 6), crs=cart.crs.PlateCarree())
lon_formatter = LongitudeFormatter(number_format='.2f')
ax.xaxis.set_major_formatter(lon_formatter)

# Ticks per a la latitud
ax.set_yticks(np.arange(np.min(lat[:]), np.max(lat[:]), 5), crs=cart.crs.PlateCarree())
lat_formatter = LatitudeFormatter(number_format='.2f')
ax.yaxis.set_major_formatter(lat_formatter)

cb = plt.colorbar(plot)
# cb.set_title("sst (ºC)")
cb.set_label("sst (ºC)", rotation=270)
ax.set_title(f"Dades sst pel dia {dia}")
plt.show()
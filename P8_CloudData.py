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
import datetime as dt
import cartopy as cart
import cmocean as cm
import matplotlib.pyplot as plt

from cartopy.mpl.ticker import LatitudeFormatter, LongitudeFormatter


arxiu = "Clouds.nc"

data = nc.Dataset(arxiu, 'r')

time = data['time'][:]

T = [dt.datetime(1900,1,1,0,0,0)+dt.timedelta(hours=int(t)) 
     for t in time]

lat = data['latitude'][:]
lon = data['longitude'][:]

# total cloud cover
tcc = data['tcc'][:]

# cloud base height
cbh = data['cbh'][:]

# low cloud cover
lcc = data['lcc'][:]


for i in range(len(T)):

    fig = plt.figure(figsize=(9, 7), dpi=400)
    ax = plt.axes(projection=cart.crs.PlateCarree())
    ax.coastlines()
    ax.add_feature(cart.feature.LAND, zorder=2, edgecolor='k', linewidth=0.05)

    plot = ax.contourf(lon, lat, tcc[i], 70, transform=cart.crs.PlateCarree(),
                    cmap=cm.cm.rain)# cmap='RdYlBu_r')

    # Ticks per a la longitud
    ax.set_xticks(lon[::3], crs=cart.crs.PlateCarree())
    lon_formatter = LongitudeFormatter(number_format='.2f')
    ax.xaxis.set_major_formatter(lon_formatter)

    # Ticks per a la latitud
    ax.set_yticks(lat[::3], crs=cart.crs.PlateCarree())
    lat_formatter = LatitudeFormatter(number_format='.2f')
    ax.yaxis.set_major_formatter(lat_formatter)

    cb = plt.colorbar(plot)
    cb.set_label("Total Cloud Cover")
    ax.set_title(f"Total Cloud Cover pel dia {T[i]}")
    plt.show()
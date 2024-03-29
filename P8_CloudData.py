#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   P8_CloudData.py
@Date    :   2023/12/21 16:21:52
@Author  :   Francesc Bernat Bieri Tauler 
@Version :   1.0

Representam la cantidad de niguls de día 6 de gener, per 
veure si coincideix amb l'anomalia de SST detectada.

Dades extretes de ERA5
'''

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

    fig = plt.figure(figsize=(9, 7), dpi=600)
    ax = plt.axes(projection=cart.crs.PlateCarree())
    ax.coastlines()
    ax.add_feature(cart.feature.LAND, zorder=2, edgecolor='k', linewidth=0.05)

    plot = ax.contourf(lon, lat, tcc[i], 70, transform=cart.crs.PlateCarree(),
                    cmap=cm.cm.rain)
    
    # Ticks per a la longitud
    ax.set_xticks(lon[::3], crs=cart.crs.PlateCarree())
    lon_formatter = LongitudeFormatter(number_format='.2f')
    ax.xaxis.set_major_formatter(lon_formatter)

    # Ticks per a la latitud
    ax.set_yticks(lat[::3], crs=cart.crs.PlateCarree())
    lat_formatter = LatitudeFormatter(number_format='.2f')
    ax.yaxis.set_major_formatter(lat_formatter)

    cb = plt.colorbar(plot)
    cb.set_label("Percentatge de niguls")
    ax.set_title(f'Niguls a les {T[i].strftime("%H:%M:%S")}')
    plt.show()
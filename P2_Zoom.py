#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   P2_Zoom.py
@Date    :   2023/12/14 17:30:13
@Author  :   Francesc Bernat Bieri Tauler 
@Contact :   franz@canmenut.com
@Version :   1.0
'''

import numpy as np
import xarray as xr
import netCDF4 as nc
import cartopy as cart
import matplotlib as mp
import matplotlib.pyplot as plt
from cartopy.mpl.ticker import LatitudeFormatter, LongitudeFormatter

# Per a cambiar les lletres a l'estil que és te a latex
mp.rcParams['mathtext.fontset'] = 'stix'
mp.rcParams['font.family'] = 'STIXGeneral'
mp.rcParams.update({'font.size': 14})

arxiu = 'AQUA_MODIS.20200102T125001.L2.SST.nc'

# Llegim arxiu nc
data = nc.Dataset('DadesMar/'+ arxiu, 'r')

# Extreim el dia de lectura
time = data.getncattr('time_coverage_start')
T = time.replace('T', ' ').split('.')[0]

# Extreim el sst
Geo = data.groups['geophysical_data']
sst = np.fliplr(Geo.variables['sst'][:])

# Extreim les coordenades
nav = data['navigation_data']
lat = np.fliplr(nav['latitude'][:])
lon = np.fliplr(nav['longitude'][:])
ind2 = np.argwhere((lat>=37) & (lat<=42) & (lon>=0) & (lon<=6))

ind = (lat>=37) & (lat<=42) & (lon>=0) & (lon<=6)

indlat = np.where((lat>37) & (lat<42))[0]
indlon = np.where((lon>0) & (lon<6))[0]

# Problema, les latituds i les longituds cambien
indlat1 = np.where(lat[:,0].data>=37)[0][0]
indlat2 = np.where(lat[:,0].data<=42)[0][-1]

# Problema, les latituds i les longituds cambien
indlon1 = np.where(lon[1,:].data>1)[0][0]
indlon2 = np.where(lon[1,:].data<6)[0][-1]

# sst = sst[indlat[0]:indlat[-1], indlon[0]:indlon[-1]]
# lat = lat[indlat[0]:indlat[-1], indlon[0]:indlon[-1]]

# lon = lon[indlat[0]:indlat[-1], indlon[0]:indlon[-1]]
# lat = lat[indlat]
# lon = lon[indlon]
# sst = sst[indlat][indlon]

# sst = sst[indlat1:indlat2, indlon1:indlon2]
# lon = lon[indlat1:indlat2, indlon1:indlon2]
# lat = lat[indlat1:indlat2, indlon1:indlon2]

# sst = sst[ind2]
# lat = lat[ind2]
# lon = lon[ind2]

min_lon = 1
min_lat = 37
max_lon = 6
max_lat = 42

da = xr.DataArray([lon, lat, sst], dims=['lon', 'lat', 'sst'])
da = xr.DataArray(sst, dims=['x', 'y'], 
                  coords = dict(lon=(["x", "y"], lon), 
                            lat=(["x", "y"], lat)))

mask_lon = (da.lon >= min_lon) & (da.lon <= max_lon)
mask_lat = (da.lat >= min_lat) & (da.lat <= max_lat)
# a = da.isel(lat=slice(37,42), lon=slice(0,6))

# cropped_ds = da.sel(lat=slice(min_lat,max_lat), lon=slice(min_lon,max_lon))

cro_da = da.where(mask_lon & mask_lat, drop=True)

##########################################################################################

fig = plt.figure(figsize=(9, 7), dpi=400)
ax = plt.axes(projection=cart.crs.PlateCarree())
ax.coastlines()
ax.add_feature(cart.feature.LAND, zorder=2, edgecolor='k', linewidth=0.05)

plot = ax.contourf(cro_da.lon, cro_da.lat, cro_da, 70, transform=cart.crs.PlateCarree())

# Ticks per a la longitud
ax.set_xticks(np.arange(np.min(cro_da.lon[:]), np.max(cro_da.lon[:]), 6), crs=cart.crs.PlateCarree())
lon_formatter = LongitudeFormatter(number_format='.2f')
ax.xaxis.set_major_formatter(lon_formatter)

# Ticks per a la latitud
ax.set_yticks(np.arange(np.min(cro_da.lat[:]), np.max(cro_da.lat[:]), 5), crs=cart.crs.PlateCarree())
lat_formatter = LatitudeFormatter(number_format='.2f')
ax.yaxis.set_major_formatter(lat_formatter)

cb = plt.colorbar(plot)
cb.set_label("sst (ºC)", rotation=270)
ax.set_title(f"Dades sst pel dia {T}")
plt.show()

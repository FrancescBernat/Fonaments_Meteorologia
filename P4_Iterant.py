#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   P4_Iterant.py
@Date    :   2023/12/16 13:03:27
@Author  :   Francesc Bernat Bieri Tauler 
@Contact :   franz@canmenut.com
@Version :   1.0
'''

import glob 
import pandas as pd
import xarray as xr
import funcions as fun
from importlib import reload

reload(fun)

nom_arxius = 'DadesMar/*_MODIS.*.SST.nc'

arxius = glob.glob(nom_arxius)

# Definesc ara les latituds i les longituds de cada zona.
lat_Glo = [37, 42]
lon_Glo = [1, 6]

lat_CMe = [39.7, 40]
lon_CMe = [3.2, 3.9]

lat_CMa = [38.6, 39.5]
lon_CMa = [1.5, 3]

lats = [lat_Glo, lat_CMe, lat_CMa]
lons = [lon_Glo, lon_CMe, lon_CMa]
labels = ['Illes Balears', 'Canal de Menorca', 
          'Canal de Mallorca']


T, sst, lat, lon = fun.DadesMODIS(arxius[0])

data = xr.DataArray(
                    sst, dims=['x', 'y'], 
                    coords = dict(lon=(["x", "y"], lon), 
                                lat=(["x", "y"], lat))
                    )

for la, lo, lab in zip(lats, lons, labels):
    red_data = fun.ZonaZoom(data, lo, la)
    fun.Repr(red_data, lo, la, lab, T)
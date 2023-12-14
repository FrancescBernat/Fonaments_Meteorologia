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
import netCDF4 as nc
import datetime as dt
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


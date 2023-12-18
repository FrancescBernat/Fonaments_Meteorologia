#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   P5_Grafiques1d.py
@Date    :   2023/12/18 15:53:45
@Author  :   Francesc Bernat Bieri Tauler 
@Contact :   franz@canmenut.com
@Version :   1.0
'''

import numpy as np
import pandas as pd
import matplotlib as mp
import matplotlib.pyplot as plt

mp.rcParams['mathtext.fontset'] = 'stix'
mp.rcParams['font.family'] = 'STIXGeneral'
mp.rcParams.update({'font.size': 17})

df = pd.read_pickle("./dataframe.pkl")

# Miram les files (r --> rows) on tenim nan
r, _ = np.where(df.isna())
r = np.unique(r)

# diesNan = df['dia'][r]

df.drop(r)
# plt.style.use('_mpl-gallery')

x = df['dia']
Mit_IB = df['Mitj IB']
Desv_IB = df['Desv IB']

Mit_CMe = df['Mitj CMe']
Desv_CMe = df['Desv CMe']

Mit_CMa = df['Mitj CMa']
Desv_CMa = df['Desv CMa']

# plot
fig, ax = plt.subplots(figsize=(10, 8), dpi=400)

ax.fill_between(x, Mit_IB-Desv_IB, Mit_IB+Desv_IB, 
                alpha=.5, linewidth=0)
ax.plot(x, Mit_IB, linewidth=2)

# ax.fill_between(x, Mit_CMe-Desv_CMe, Mit_CMe+Desv_CMe, 
#                 alpha=.5, linewidth=0)
# ax.plot(x, Mit_CMe, linewidth=2)

# ax.fill_between(x, Mit_CMa-Desv_CMa, Mit_CMa+Desv_CMa, 
#                 alpha=.5, linewidth=0)
# ax.plot(x, Mit_CMa, linewidth=2)


ax.set(xticks=x[::5], ylabel='sst (ºC)')
fig.autofmt_xdate()
plt.show()
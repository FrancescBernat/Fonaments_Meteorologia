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
import funcions as fun
import matplotlib as mp
import matplotlib.pyplot as plt
from importlib import reload

reload(fun)

# mp.rcParams['mathtext.fontset'] = 'stix'
# mp.rcParams['font.family'] = 'STIXGeneral'
# mp.rcParams.update({'font.size': 17})

df = pd.read_pickle("./dataframe.pkl")

# Miram les files (r --> rows) on tenim nan
r, _ = np.where(df.isna())
r = np.unique(r)

# Miram els indexos on els Nan superen el 50 %.
ind_Bad = []

for var in ['CMe', 'CMa', 'IB']:

    # Supos que quan hi ha menys nans 
    # es quan només es te en compte les illes
    minNan = df['Nan '+var].min()

    aux = np.squeeze(np.where(
        (df['Nan '+var]-minNan)/df['Tam '+ var] > 0.4
        ))
    ind_Bad += aux.tolist()

# Combinam el cas anterior amb  els llocs on son tots nans
ind = np.unique(ind_Bad + r.tolist())

# plt.style.use('_mpl-gallery')
# plt.style.use('dark_background')
# plt.style.use('seaborn-v0_8-deep')

colors = ['#4C72B0', '#55A868', '#C44E52', '#8172B2', '#CCB974', '#64B5CD']

x = df['dia']
Mit_IB, Mit_CMe, Mit_CMa = [df['Mitj ' + var] for var in ['IB', 'CMe', 'CMa']]
Desv_IB, Desv_CMe, Desv_CMa = [df['Desv ' + var] for var in ['IB', 'CMe', 'CMa']]

# Mit_IB = df['Mitj IB']
# Desv_IB = df['Desv IB']

# Mit_CMe = df['Mitj CMe']
# Desv_CMe = df['Desv CMe']

# Mit_CMa = df['Mitj CMa']
# Desv_CMa = df['Desv CMa']


def ErrorPlot(x, y, yerr, color):
    fig, ax = plt.subplots(figsize=(10, 8), dpi=600)

    ax.errorbar(x, y, yerr, fmt='o', linewidth=2, capsize=6,
                color=color)

    # ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
    #     ylim=(0, 8), yticks=np.arange(1, 8))
    ax.set(xticks=x[::5])
    fig.autofmt_xdate()
    plt.show()

# for i in colors:
    # ErrorPlot(x, Mit_IB, Desv_IB, i)

# Graficam les dades sense filtrar
for M, D, tit, col in zip([Mit_IB, Mit_CMe, Mit_CMa],
                [Desv_IB, Desv_CMe, Desv_CMa], 
                ['Illes Balears', 'Canal de Menorca',
                 'Canal de Mallorca'], range(3)):
    
    fun.fillPlot(x, M, D, tit, colors[col])

fig, ax = plt.subplots(figsize=(10, 8), dpi=400)
ax.plot(x, Mit_IB, label="Illes Balears", color=colors[0])
ax.plot(x, Mit_CMe, label="Canal de Menorca", color=colors[1])
ax.plot(x, Mit_CMa, label="Canal de Mallorca", color=colors[2])

ax.set(xticks=x[::5])
ax.set_ylabel('sst (ºC)', fontsize=30)
ax.legend()
fig.autofmt_xdate()
plt.show()
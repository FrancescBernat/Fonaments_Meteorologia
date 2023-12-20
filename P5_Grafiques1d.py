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

def fillPlot(Mitj, DesvEst):
    
    fig, ax = plt.subplots(figsize=(10, 8), dpi=400)

    ax.fill_between(x, Mitj-DesvEst, Mitj+DesvEst, 
                    alpha=.5, linewidth=0)
    ax.plot(x, Mitj, linewidth=2)

    # ax.fill_between(x, Mit_CMe-Desv_CMe, Mit_CMe+Desv_CMe, 
    #                 alpha=.5, linewidth=0)
    # ax.plot(x, Mit_CMe, linewidth=2)

    # ax.fill_between(x, Mit_CMa-Desv_CMa, Mit_CMa+Desv_CMa, 
    #                 alpha=.5, linewidth=0)
    # ax.plot(x, Mit_CMa, linewidth=2)


    ax.set(xticks=x[::5])
    ax.set_ylabel('sst (ºC)', fontsize=30)
    fig.autofmt_xdate()
    plt.show()

def ErrorPlot(x, y, yerr):
    fig, ax = plt.subplots()

    ax.errorbar(x, y, yerr, fmt='o', linewidth=2, capsize=6)

    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
        ylim=(0, 8), yticks=np.arange(1, 8))

    plt.show()

    
for M, D in zip([Mit_IB, Mit_CMe, Mit_CMa],
                [Desv_IB, Desv_CMe, Desv_CMa]):
    fillPlot(M, D)

fig, ax = plt.subplots(figsize=(10, 8), dpi=400)
ax.plot(x, Mit_IB, label="Illes Balears")
ax.plot(x, Mit_CMe, label="Canal de Menorca")
ax.plot(x, Mit_CMa, label="Canal de Mallorca")

ax.set(xticks=x[::5])
ax.set_ylabel('sst (ºC)', fontsize=30)
ax.legend()
fig.autofmt_xdate()
plt.show()
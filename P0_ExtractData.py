#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   P0_ExtractData.py
@Date    :   2023/12/12 16:04:59
@Author  :   Francesc Bernat Bieri Tauler 
@Contact :   franz@canmenut.com
@Version :   1.1

Arxiu per a descarregar totes les dades de Modis sense
haver-ho de fer manualment. 

Segurament hi hagui alguna manera més eficient.
'''

import time
import pyautogui
import webbrowser

file = "Download.txt"

with open(file, 'r') as f:
    Lines = f.readlines()

for l in Lines:
    print(l)
    webbrowser.open(l)

    # Deixam descansar un temps per a que es descarregui sense problemes
    time.sleep(20)

    # Tancam el navegador
    pyautogui.hotkey('ctrl', 'w')
    print("tab closed \n")
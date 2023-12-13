#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   P0_ExtractData.py
@Date    :   2023/12/12 16:04:59
@Author  :   Francesc Bernat Bieri Tauler 
@Contact :   franz@canmenut.com
@Version :   1.1
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
    time.sleep(20)
    pyautogui.hotkey('ctrl', 'w')
    print("tab closed \n")

    



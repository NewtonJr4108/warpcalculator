# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 22:39:41 2022

@author: Coding
"""

import time

print("Warp Drive Awaiting Electromagnetic Engagement")
def warpgauge():
    while True:
        try:
            warp = input("State warp core energy output in petajoules\n")
        
            m = int(warp)*1000000000000000/89875517900000000*300
            print("Injecting tritium/deuterium plasma into reactor. ")
            print(str(m)+" KG of Fuel per Second in Use")
            time.sleep(3)
            warp1=65*1000000000000000
            petawarp = (int(warp)*1000000000000000)
            c=petawarp/warp1
            warpfactor = c ** (1./3.)
            print("Accelerating to Warp "+str(warpfactor)+"("+str(c)+"c)")
            print("Travelling at "+str((c)/325)+" Lightyears Per Day")
        except ValueError:
            print("That's not a valid energy gauge, ding dong!")
            break
warpgauge()

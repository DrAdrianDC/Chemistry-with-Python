#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 06:01:15 2024

@author: adriandominguezcastro
"""

# Library installation
# pip install periodictable

# Periodic Table Element Info using Python

import periodictable

element_name = input("Enter the element symbol: ").capitalize()
element_data = getattr(periodictable, element_name, None)

if element_data:
    print(f"Element: {element_data.name}")
    print(f"Symbol: {element_data.symbol}")
    print(f"Atomic Number: {element_data.number}")
    print(f"Atomic Weight: {element_data.mass}")
    print(f"Density: {element_data.density}")
else:
    print(f"Element '{element_name}' not found ")
    
    
    
    
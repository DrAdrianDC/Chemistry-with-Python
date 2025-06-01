#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 31 12:25:53 2025

@author: adriandominguezcastro
"""

import math

def calculate_ph(h_conc):
    return -math.log10(h_conc)

def calculate_poh(oh_conc):
    return -math.log10(oh_conc)

def h_conc_from_ph(ph):
    return 10 ** -ph

def oh_conc_from_poh(poh):
    return 10 ** -poh

def ph_from_poh(poh):
    return 14 - poh

def poh_from_ph(ph):
    return 14 - ph

def classify_solution(ph):
    if ph < 7:
        return "Acidic"
    elif ph > 7:
        return "Basic"
    else:
        return "Neutral"

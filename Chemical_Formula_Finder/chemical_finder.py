#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 07:48:56 2024

@author: adriandominguezcastro
"""

# Library installation
# pip install pubchempy

# Enter chemical Name to find formula

import pubchempy as pcp

# Take name as input
chemical_name = input ("Enter chemical name: ")

try:
    # Search PubChem for the compound by its name
    compound = pcp.get_compounds(chemical_name, 'name')[0]
    
    # Display information about the compound
    print(f"IUPAC Name: {compound.iupac_name}")
    print(f"Common Name: {compound.synonyms[0]}")
    print(f"Molecular Weight: {compound.molecular_weight}")
    print(f"Formula: {compound.molecular_formula}")
    
    
    # You cab access more properties as needed
except IndexError:
     print(f"No information found for {chemical_name}.")
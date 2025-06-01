#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 31 10:45:51 2025

@author: adriandominguezcastro
"""

import streamlit as st
from utils import *

st.set_page_config(page_title="pH and pOH Calculator", layout="centered")

st.title("pH and pOH Calculator")
st.markdown("Enter one known value to calculate the rest.")

input_type = st.selectbox("Select input type:", ["pH", "pOH", "[H⁺] (mol/L)", "[OH⁻] (mol/L)"])

user_input = st.text_input(f"Enter value for {input_type}:")

if user_input:
    try:
        value = float(user_input)
        st.divider()

        if input_type == "pH":
            ph = value
            poh = poh_from_ph(ph)
            h = h_conc_from_ph(ph)
            oh = oh_conc_from_poh(poh)
        elif input_type == "pOH":
            poh = value
            ph = ph_from_poh(poh)
            oh = oh_conc_from_poh(poh)
            h = h_conc_from_ph(ph)
        elif input_type == "[H⁺] (mol/L)":
            h = value
            ph = calculate_ph(h)
            poh = poh_from_ph(ph)
            oh = oh_conc_from_poh(poh)
        elif input_type == "[OH⁻] (mol/L)":
            oh = value
            poh = calculate_poh(oh)
            ph = ph_from_poh(poh)
            h = h_conc_from_ph(ph)

        nature = classify_solution(ph)

        st.success(f"**Solution is: {nature.upper()}**")
        st.write(f"**pH:** {ph:.4f}")
        st.write(f"**pOH:** {poh:.4f}")
        st.write(f"**[H⁺]:** {h:.2e} mol/L")
        st.write(f"**[OH⁻]:** {oh:.2e} mol/L")

    except ValueError:
        st.error("Please enter a valid numeric value.")

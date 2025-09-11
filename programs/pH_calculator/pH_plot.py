#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 31 14:25:53 2025

@author: adriandominguezcastro
"""

import matplotlib.pyplot as plt
import numpy as np

def plot_ph_scale(ph_value):
    fig, ax = plt.subplots(figsize=(10, 1.5))

    # Define pH color spectrum (rough approximation)
    ph_colors = [
        "#FF0000", "#FF3300", "#FF6600", "#FF9900", "#FFCC00", "#FFFF00",  # Acidic
        "#CCFF33", "#99FF66", "#66FF99", "#33FFCC", "#00FFFF", "#00CCFF", "#0099FF", "#0066FF"  # Basic
    ]

    for i in range(14):
        ax.barh(0, width=1, left=i, height=1, color=ph_colors[i], edgecolor='black')

    # Add current pH marker
    ax.axvline(ph_value, color='black', linestyle='--', label=f'pH = {ph_value:.2f}')

    ax.set_xlim(0, 14)
    ax.set_yticks([])
    ax.set_xticks(np.arange(0, 15, 1))
    ax.set_xlabel('pH Scale')
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2), ncol=1)
    ax.set_title('pH Scale Visualization')

    return fig

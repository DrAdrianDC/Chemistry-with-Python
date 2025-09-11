#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 11:05:01 2024

@author: adriandominguezcastro
"""

# Radioactive decay

import math
import matplotlib.pyplot as plt  # Importing matplotlib for plotting

# Constant decay function
def decay_constant(half_time):
    """
    Calculates the decay constant based on the half-life of the isotope.
    
    Parameters:
    half_time (float): The half-life of the isotope in seconds.

    Returns:
    float: The decay constant.
    """
    return 0.693/half_time

# Radioactive decay law
def radioactive_decay_law(mass_0, decay_constant, time):
    """
    Applies the radioactive decay law to calculate remaining mass after a given time.

    Parameters:
    mass_0 (float): The initial mass of the substance in grams.
    decay_constant (float): The decay constant of the substance.
    time (float): Time elapsed in seconds.

    Returns:
    float: The remaining mass after the time period.
    """
    return mass_0 * math.exp(- (decay_constant * time))


# Input validation function
def get_positive_float(prompt):
    """
    Repeatedly prompts the user for a positive float input.

    Parameters:
    prompt (str): The prompt to display to the user.

    Returns:
    float: A positive float value.
    """
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive value.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Get user inputs 
       # half_time
half_time = get_positive_float("Introduce the half_time value of your radioactive isotope in seconds: ")

       # initial mass
mass_0 = get_positive_float("Introduce the original mass in grams: ")
            
       # time            
time = get_positive_float("Introduce the time value in seconds: ")

# Calculate the decay constant and remaining mass
decay_const = decay_constant(half_time)
remaining_mass = radioactive_decay_law(mass_0, decay_const, time)

print(f'The remaining mass of your radioactive isotope after {time} seconds is {remaining_mass} grams')


# Plotting the results

# Now, let's plot the radioactive decay over time
# Define a time range from 0 to the input time (e.g., 1000 seconds)
time_values = [i for i in range(int(time) + 1)]

# Calculate the remaining mass for each time value
mass_values = [radioactive_decay_law(mass_0, decay_const, t) for t in time_values]

# Plot the decay curve
plt.figure(figsize=(10, 6))
plt.plot(time_values, mass_values, label=f'Half-life = {half_time} sec', color='blue', linewidth=2)

# Adding labels and title
plt.title('Radioactive Decay Over Time', fontsize=14)
plt.xlabel('Time (seconds)', fontsize=12)
plt.ylabel('Remaining Mass (grams)', fontsize=12)
plt.grid(True)
plt.legend()

# Save the plot
plt.savefig('my_plot.png', dpi=300, bbox_inches='tight')


# Show the plot
plt.show()



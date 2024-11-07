# Molecular Dynamics Simulation using Monte Carlo Methods

This repository contains a simulation of molecular dynamics using Monte Carlo methods. The simulation explores the configurational space of particles in a cubic box, calculating the total energy of the system using the Lennard-Jones potential and applying periodic boundary conditions.

## Description

Monte Carlo methods are used to simulate the movement of particles in a system and study their interactions. In this case, we are using the Lennard-Jones potential to model the interactions between particles. The system undergoes a series of random moves, and the simulation determines whether each move is accepted or rejected based on the change in energy and temperature.
The simulation tracks the total energy of the system over time and visualizes the final positions of the particles in 3D.

## Features

* Lennard-Jones Potential: The energy between two particles is modeled using the Lennard-Jones potential, which is a function of the distance between particles.

* Monte Carlo Simulation: The system is evolved through a series of random moves, with the acceptance or rejection of each move determined by the energy change and temperature.
  
* Energy Convergence: The simulation tracks the total energy of the system over time, showing how the system evolves towards equilibrium.
  
* 3D Particle Visualization: The final positions of the particles are visualized in 3D, showing their distribution in the simulation box.
  
## Requirements
This code requires the following Python libraries:
* numpy
* matplotlib
* 
You can install the required libraries using pip:

pip install numpy matplotlib

# Molecular Dynamics Simulation using Monte Carlo Methods

This repository contains a simulation of molecular dynamics using Monte Carlo methods. The simulation explores the configurational space of particles in a cubic box, calculating the total energy of the system using the Lennard-Jones potential and applying periodic boundary conditions.

## Description

Monte Carlo methods are used to simulate the movement of particles in a system and study their interactions. In this case, we are using the Lennard-Jones potential to model the interactions between particles. ( The Lennard-Jones potential is often used to model simple atomic or molecular systems where short-range repulsive forces and long-range attractive forces need to be considered. It is particularly useful in simulating noble gases, liquids, and other systems with relatively simple interatomic interactions.)

The system undergoes a series of random moves, and the simulation determines whether each move is accepted or rejected based on the change in energy and temperature. The simulation tracks the total energy of the system over time and visualizes the final positions of the particles in 3D.

##### (The Total Energy, starting high due to random particle placement and gradually decreasing as the system finds a configuration with lower energy)

## Features

* **Lennard-Jones Potential:** The energy between two particles is modeled using the Lennard-Jones potential, which is a function of the distance between particles.

* **Monte Carlo Simulation:** The system is evolved through a series of random moves, with the acceptance or rejection of each move determined by the energy change and temperature.
  
* **Energy Convergence:** The simulation tracks the total energy of the system over time, showing how the system evolves towards equilibrium.
  
* **3D Particle Visualization:** The final positions of the particles are visualized in 3D, showing their distribution in the simulation box.
  
## Requirements
This code requires the following Python libraries:
* numpy
* matplotlib

You can install the required libraries using pip:

   ```bash
   pip install numpy matplotlib
   ```

## Code Overview

### 1. Parameters
The simulation is initialized with the following parameters:
* **num_particles:** Number of particles in the system (default is 50).
* **box_size:** Size of the cubic simulation box (default is 10.0).
* **temperature:** Temperature of the system (default is 1.0).
* **max_steps:** Number of Monte Carlo steps (default is 1000).
* **move_dist:** Maximum move distance for each step (default is 0.1).
* **epsilon:** Depth of the Lennard-Jones potential well (default is 1.0).
* **sigma:** Distance at which the Lennard-Jones potential is zero (default is 1.0).

  
### 2. Functions

* **lennard_jones_potential(r):** Calculates the Lennard-Jones potential between two particles based on their distance r.
* **calculate_total_energy(positions):** Computes the total energy of the system by summing the Lennard-Jones potential for all particle pairs.
* **monte_carlo_simulation(positions, max_steps, temperature):** Performs the Monte Carlo simulation by randomly moving particles and accepting or rejecting the moves based on the energy change.
* **plot_particles(positions):** Visualizes the final positions of the particles in 3D using matplotlib.


### 3. Outputs

* **Energy Convergence Plot:** The total energy of the system is plotted over time, showing how the system evolves toward equilibrium.
* **Particle Position Visualization:** A 3D scatter plot shows the final positions of the particles in the simulation box.


### Usage

To run the simulation, simply execute the script. 

  ```bash
   python 
   ```

The results will be saved as:
* energy_convergence.png: A plot showing the energy convergence over the Monte Carlo steps.
* final_particle_positions.png: A 3D plot of the final positions of the particles.

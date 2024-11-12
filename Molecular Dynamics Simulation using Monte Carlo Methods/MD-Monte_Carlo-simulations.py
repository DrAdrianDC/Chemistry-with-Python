


# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Parameters for the simulation
num_particles = 50       # Number of particles in the simulation
box_size = 10.0          # Size of the cubic simulation box
temperature = 1.0        # Temperature (arbitrary units)
max_steps = 1000         # Number of Monte Carlo steps
move_dist = 0.1          # Maximum move distance for each step
epsilon = 1.0            # Depth of the Lennard-Jones potential well
sigma = 1.0              # Distance at which the Lennard-Jones potential is zero

# Initialize particle positions randomly within the box
positions = np.random.uniform(0, box_size, (num_particles, 3))

# Lennard-Jones potential function for a pair of particles
def lennard_jones_potential(r):
    return 4 * epsilon * ((sigma / r)**12 - (sigma / r)**6)

# Calculate total energy of the system based on Lennard-Jones potential
def calculate_total_energy(positions):
    energy = 0.0
    for i in range(num_particles):
        for j in range(i + 1, num_particles):
            r_ij = np.linalg.norm(positions[i] - positions[j])  # Distance between particles
            if r_ij < box_size / 2:  # Consider periodic boundary conditions
                energy += lennard_jones_potential(r_ij)
    return energy

# Monte Carlo move simulation
def monte_carlo_simulation(positions, max_steps, temperature):
    energies = []
    all_positions = []
    current_energy = calculate_total_energy(positions)
    
    for step in range(max_steps):
        # Randomly choose a particle to move
        particle_idx = np.random.randint(0, num_particles)
        original_position = positions[particle_idx].copy()
        
        # Propose a random move within the move distance
        proposed_move = original_position + np.random.uniform(-move_dist, move_dist, 3)
        
        # Apply periodic boundary conditions
        proposed_move = proposed_move % box_size
        
        # Calculate new energy if the move is accepted
        positions[particle_idx] = proposed_move
        new_energy = calculate_total_energy(positions)
        
        # Calculate energy change and decide to accept or reject the move
        delta_energy = new_energy - current_energy
        if delta_energy < 0 or np.random.rand() < np.exp(-delta_energy / temperature):
            # Accept the move
            current_energy = new_energy
        else:
            # Reject the move
            positions[particle_idx] = original_position
        
        # Store the current energy and positions
        energies.append(current_energy)
        all_positions.append((positions.copy(), particle_idx))  # Store particle index for visualization
    
    return all_positions, energies

# Run the simulation
all_positions, energies = monte_carlo_simulation(positions, max_steps, temperature)

# Plot energy over each step
plt.figure(1)
plt.plot(energies)
plt.xlabel("Monte Carlo Step")
plt.ylabel("Total Energy")
plt.title("Energy Convergence in 3D Monte Carlo Molecular Dynamics")
plt.tight_layout()
plt.savefig("energy_convergence.png")

# Visualization of final particle positions
def plot_particles(positions):
    fig = plt.figure(2)
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(positions[:, 0], positions[:, 1], positions[:, 2], c='b', marker='o')
    ax.set_xlim(0, box_size)
    ax.set_ylim(0, box_size)
    ax.set_zlim(0, box_size)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.title("Final Particle Positions in 3D")
    plt.tight_layout()
    plt.savefig("final_particle_positions.png")

# Pass the last position set from the simulation to the plotting function
plot_particles(all_positions[-1][0])

# Visualization of particle movement with animation
fig = plt.figure(3)
ax = fig.add_subplot(111, projection='3d')

is_paused = False  # Control for pausing animation

def toggle_pause(event):
    global is_paused
    if event.key == ' ':  # Spacebar to pause/resume
        is_paused = not is_paused

fig.canvas.mpl_connect('key_press_event', toggle_pause)

def update(step):
    """Update function for animation, respects the pause state."""
    if is_paused:
        return  # Skip update if paused

    ax.clear()
    current_positions, moving_idx = all_positions[step]
    # Plot all particles in blue, except the one moving in red
    ax.scatter(current_positions[:, 0], current_positions[:, 1], current_positions[:, 2], c='b', marker='o')
    ax.scatter(current_positions[moving_idx, 0], current_positions[moving_idx, 1], current_positions[moving_idx, 2], c='r', marker='o')

    ax.set_xlim(0, box_size)
    ax.set_ylim(0, box_size)
    ax.set_zlim(0, box_size)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(f"Step {step}")

# Initialize animation with the update function
ani = FuncAnimation(fig, update, frames=max_steps, interval=50, blit=False)

plt.show()

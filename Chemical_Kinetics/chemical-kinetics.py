# Chemical Kinetics

# Import libraries
import numpy as np
import scipy.integrate

# Define the reaction rate function (d[A]/dt = -k[A])
def reaction_rate(t, y, k):
    """
    Calculates the rate of change of concentrations.

    Args:
        y: A list or array containing the concentrations of all species.
        t: The time.
        k: The rate constant.

    Returns:
        A list or array containing the rate of change of each concentration.
    """
    dydt = [-k * y[0]]  # For a single first-order reaction A -> B
    return dydt

# Define initial conditions
initial_conditions = [1.0]  # Initial concentration of A (e.g., [A] = 1.0)

# Define time points to solve for
time_points = np.linspace(0, 10, 100)  # Time from 0 to 10, with 100 points

# Define the rate constant
rate_constant = 0.5

# Solve the ODE using scipy.integrate.odeint
solution = scipy.integrate.solve_ivp(reaction_rate, [time_points[0], time_points[-1]], initial_conditions, args=(rate_constant,), t_eval=time_points)

# Extract the concentrations at each time point
concentrations = solution.y.T

# You can now plot the results or analyze the data
# For example, plot the concentration of A over time
import matplotlib.pyplot as plt
plt.plot(time_points, concentrations[:, 0], label="A")
plt.xlabel("Time")
plt.ylabel("Concentration")
plt.legend()
plt.show()



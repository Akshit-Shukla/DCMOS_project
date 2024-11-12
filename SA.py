import numpy as np
import random
import math
from PyLTSpice import SimCommander
from simulation_util import modify_and_simulate_netlist

# Function to update transistor parameters with random changes within bounds
def update_params(transistor_params, param_bounds):
    new_params = {}

    for param, details in transistor_params.items():
        # Ensure details contain "value" and "type"
        if not isinstance(details, dict) or "type" not in details or "value" not in details:
            continue  # Skip parameter if format is incorrect

        # Get transistor type and current value
        transistor_type = details["type"]
        current_value = details["value"]

        # Random change within a small range
        change = random.uniform(-1e-9, 1e-9)
        new_value = current_value + change

        # Apply bounds based on transistor type and parameter (W or L)
        if "W" in param:
            min_val, max_val = param_bounds[transistor_type]["W"]
        elif "L" in param:
            min_val, max_val = param_bounds[transistor_type]["L"]

        # Ensure new value is within bounds
        bounded_value = np.clip(new_value, min_val, max_val)
        
        # Update new_params dictionary
        new_params[param] = {"value": bounded_value, "type": transistor_type}
    
    return new_params

# Simulated Annealing Algorithm
def simulated_annealing(sim, initial_params, param_bounds, initial_temp, cooling_rate, max_iters):
    current_params = initial_params.copy()
    current_cost = math.inf
    best_params, best_cost = current_params, current_cost
    temperature = initial_temp

    for i in range(max_iters):
        # Generate new parameters by applying a small random change
        new_params = current_params.copy()
        for param in new_params:
            change = 10e-9 * random.uniform(-5, 5)  # Random change in a small range
            new_value = np.clip(new_params[param] + change, *param_bounds[param])  # Enforce bounds
            new_params[param] = new_value

        # Define netlist path for the simulation
        netlist_path = "D:\\DCMOS_PROJECT\\adder_new\\full_adder.sp"

        # Modify netlist with new parameters and run the simulation
        static_current = modify_and_simulate_netlist(netlist_path, new_params, i)

        # Calculate cost for new parameters (minimizing static current)
        new_cost = -1 * static_current
        
        # Calculate the acceptance probability using the given formula
        if new_cost < current_cost:
            acceptance_probability = 1  # Always accept if new cost is lower
        else:
            delta_cost = current_cost - new_cost
            acceptance_probability = 1 / (1 + math.exp(delta_cost / temperature))

        # Accept new parameters based on acceptance probability
        if random.uniform(0, 1) < acceptance_probability:
            current_params, current_cost = new_params, new_cost
            # Update best parameters if new cost is lower
            if new_cost < best_cost:
                best_params, best_cost = new_params, new_cost

        # Cool down the temperature
        temperature *= cooling_rate
        print(f"Iteration {i+1}: Best Cost={best_cost:.5e}, Temperature={temperature:.5e}")

    return best_params, best_cost

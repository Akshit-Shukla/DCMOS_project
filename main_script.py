import os
from simulation_util import modify_and_simulate_netlist
from SA import simulated_annealing
import random
import math
from PyLTSpice import SimCommander

def run_simulations_in_loop():
    # Path to the LTspice netlist file
    

    # Initial parameters for the transistors
  
    """param_bounds = {
    "nmos": {"W": (120e-9, 250e-9), "L": (45e-9, 60e-9)},
    "pmos": {"W": (200e-9, 500e-9), "L": (50e-9, 80e-9)}
    }"""

    
    #initial_params = {'Wn': 100e-9, 'Ln': 45e-9, 'Wp': 180e-9, 'Lp': 45e-9}
    """param_bounds = {
    "W1": 1000, "L1": 50,
    "W2": 1000, "L2": 50,
    "W3": 1000, "L3": 50,
    "W4": 200, "L4": 50,
    "W5": 1000, "L5": 50,
    "W6": 220, "L6": 60,
    "W7": 130, "L7": 50,
    "W8": 170, "L8": 55
    }"""



    param_bounds = {
    "W1": (90e-9, 1000e-9),  # min and max for W1
    "L1": (50e-9, 45-9),    # min and max for L1
    "W2": (90e-9, 1000e-9),  # min and max for W2
    "L2": (50e-9, 45e-9),
    "W3": (90e-9, 1000e-9),
    "L3": (50e-9, 45e-9),
    "W4": (90e-9, 1000e-9),
    "L4": (50e-9, 45e-9),
    "W5": (90e-9, 1000e-9), 
    "L5": (50e-9, 45e-9),
    "W6": (90e-9, 1000e-9),
    "L6": (50e-9, 45e-9),
    "W7": (90e-9, 1000e-9),  # min and max for W1
    "L7": (50e-9, 45-9),    # min and max for L1
    "W8": (90e-9, 1000e-9),  # min and max for W2
    "L8": (50e-9, 45e-9),
    "W9": (90e-9, 1000e-9),
    "L9": (50e-9, 45e-9),
    "W10": (90e-9, 1000e-9),
    "L10": (50e-9, 45e-9),
    "W11": (90e-9, 1000e-9), 
    "L11": (50e-9, 45e-9),
    "W12": (90e-9, 1000e-9), 
    "L12": (50e-9, 45e-9),
    
    "W13": (90e-9, 1000e-9),
    "L13": (50e-9, 45e-9),
    "W14": (90e-9, 1000e-9),  # min and max for W1
    "L14": (50e-9, 45-9),    # min and max for L1
    "W15": (90e-9, 1000e-9),  # min and max for W2
    "L15": (50e-9, 45e-9),
    "W16": (90e-9, 1000e-9),
    "L16": (50e-9, 45e-9),
    "W17": (90e-9, 1000e-9),
    "L17": (50e-9, 45e-9),
    "W18": (90e-9, 1000e-9), 
    "L18": (50e-9, 45e-9),
    "W19": (90e-9, 1000e-9),
    "L19": (90e-9, 1000e-9),
    "W20": (50e-9, 45e-9),
    "L20": (50e-9, 45e-9),
    "W21": (90e-9, 1000e-9),  # min and max for W1
    "L21": (50e-9, 45-9),    # min and max for L1
    "W22": (90e-9, 1000e-9),  # min and max for W2
    "L22": (50e-9, 45e-9),
    "W23": (90e-9, 1000e-9),
    "L23": (50e-9, 45e-9),
    "W24": (90e-9, 1000e-9),
    "L24": (50e-9, 45e-9),
    "W25": (90e-9, 1000e-9), 
    "L25": (50e-9, 45e-9),
    "W26": (90e-9, 1000e-9),
    "L26": (50e-9, 45e-9),
    "W27": (90e-9, 1000e-9),  # min and max for W1
    "L27": (50e-9, 45-9),    # min and max for L1
    "W28": (90e-9, 1000e-9),  # min and max for W2
    "L28": (50e-9, 45e-9),
       # min and max for L2
    # Add bounds for other parameters here...
    }
    
    


    initial_params = {
    "W1": 720e-9, "L1": 45e-9,
    "W2": 720e-9, "L2": 45e-9,
    "W3": 720e-9, "L3": 45e-9,
    "W4": 720e-9, "L4": 45e-9,
    "W5": 720e-9, "L5": 45e-9,
    "W6": 720e-9, "L6": 45e-9,
    "W7": 720e-9, "L7": 45e-9,
    "W8": 720e-9, "L8": 45e-9,
    "W9": 720e-9, "L9": 45e-9,
    "W10": 360e-9, "L10": 45e-9,
    "W11": 360e-9, "L11": 45e-9,
    "W12": 360e-9, "L12": 45e-9,
    "W13": 360e-9, "L13": 45e-9,
    "W14": 360e-9, "L14": 45e-9,
    "W15": 360e-9, "L15": 45e-9,
    "W16": 360e-9, "L16": 45e-9,
    "W17": 360e-9, "L17": 45e-9,
    "W18": 540e-9, "L18": 45e-9,
    "W19": 540e-9, "L19": 45e-9,
    "W20": 540e-9, "L20": 45e-9,
    "W21": 1080e-9, "L21": 45e-9,
    "W22": 1080e-9, "L22": 45e-9,
    "W23": 1080e-9, "L23": 45e-9,
    "W24": 720e-9, "L24": 45e-9,
    "W25": 720e-9, "L25": 45e-9,
    "W26": 360e-9, "L26": 45e-9,
    "W27": 360e-9, "L27": 45e-9,
    "W28": 360e-9, "L28": 45e-9,

    }

   


    initial_temp = 10000.0
    cooling_rate = 0.99  # Cooling rate as per the paper
    max_iters = 1000
    netlist_file = 'D:\\DCMOS_PROJECT\\adder_new\\full_adder.sp'
    sim = SimCommander(netlist_file)
       

    best_params, best_cost = simulated_annealing(sim, initial_params, param_bounds, initial_temp, cooling_rate, max_iters)

    print(best_params)

if __name__ == "__main__":
        run_simulations_in_loop()

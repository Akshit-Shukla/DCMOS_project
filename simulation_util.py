import re
import os
import shutil
from PyLTSpice import SimCommander


def modify_and_simulate_netlist(netlist_path, params, run_id):
    """
    Modify the LTspice netlist with the specified parameters, run the simulation,
    and save the output to a uniquely named log file.
    """
    static_current = 0
    try:
        # Attempt to read the netlist file with multiple encodings
        try:
            with open(netlist_path, 'r', encoding='utf-8') as file:
                netlist_content = file.read()
        except UnicodeDecodeError:
            with open(netlist_path, 'r', encoding='utf-16') as file:
                netlist_content = file.read()

        # Replace placeholders in the netlist with the provided values
        for key, value in params.items():
            netlist_content = netlist_content.replace(f"{{{key}}}", str(value))

        # Ensure the modified netlist is saved in ASCII encoding
        modified_netlist_path = netlist_path.replace(".sp", f"_modified_{run_id}.sp")
        with open(modified_netlist_path, 'w', encoding='ascii') as file:
            file.write(netlist_content)

        print(f"Netlist modified for run {run_id}. Saved as {modified_netlist_path}")

        # Run the LTspice simulation
        sim = SimCommander(modified_netlist_path)
        sim.run()
        sim.wait_completion()

        # Construct the log file path
        original_log_file = os.path.splitext(modified_netlist_path)[0] + "_1.log"
        unique_log_file = f"simulation_run_{run_id}.log"

        # Check if the log file exists, then save a copy with a unique name
        if os.path.exists(original_log_file):
            shutil.copy(original_log_file, unique_log_file)
            print(f"Log file for run {run_id} saved as {unique_log_file}")
        else:
            print(f"Expected log file {original_log_file} not found.")

        static_current = extract_static_current_from_log_file(unique_log_file)

    except Exception as e:
        print(f"Error in modify_and_simulate_netlist for run {run_id}: {e}")

    return static_current


def extract_static_current_from_log_file(log_file_name):
    """
    Extract the static current from a specific LTspice log file.
    """
    static_current = 0
    try:
        with open(log_file_name, 'r') as log_file:
            log_content = log_file.read()

        # Updated regex to match the format "static_current_000: (i(v4))=-4.35839e-05"
        static_current_match = re.search(r"static_current_000: \(i\(v4\)\)=([+-]?\d*\.?\d+(?:[eE][+-]?\d+)?)", log_content)

        if static_current_match:
            # Extract and convert the matched value to float
            static_current = float(static_current_match.group(1))
            print(f"Static current from {log_file_name}: {static_current} A")
        else:
            print("Static current not found in the log file.")

    except Exception as e:
        print(f"Error reading or parsing the log file: {e}")

    return static_current

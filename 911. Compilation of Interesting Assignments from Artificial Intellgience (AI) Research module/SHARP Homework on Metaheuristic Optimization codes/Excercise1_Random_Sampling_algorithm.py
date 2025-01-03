# Excercise 1: Propose and implement a Random Sampling algorithm to solve the 
# p-median location problem

# Theory of the Random Sampling algorithm:
# Just keep randomly select p facilities and only update the optimal p facilities if a new set
# of p facilities foudn has a smaller objective value.


# ////////////////////////////////////////////////////////////////////////////


# Implementation of the Random Sampling algorithm

# There are 4 important variables that each Solution Algorithm must return, 
# 1. 'best_solution_list' - the set of facility locations (represented as indices) selected by 
#                           the solution/optimization algorithm that minimizes the total 
#                           distance/Objective Value from each demand point to its nearest facility.
# 2. 'best_obj_value' - the best 'Objective Value' found by the solution/optimization algorithm 
# 3. 'cputime_i_list' - a list of time where the 'Objective Value's are found by the solution/optimization 
#                       algorithm 
# 4. 'objvalue_logging_list' - a Pandas Dataframe that logs the found 'Objective Value's during 
#                              the iterations of the solution/optimization algorithm and the time 
#                              when these 'Objective Value's are found as results
import random
import numpy as np
import copy
import time
import matplotlib.pyplot as plt
from IPython.display import clear_output

# def connectpoints(x, y, p1, p2):
#     """Draw a line between two points."""
#     x1, x2 = x[p1], x[p2]
#     y1, y2 = y[p1], y[p2]
#     plt.plot([x1, x2], [y1, y2], 'k-')

# def plot_solution(coordlct_x, coordlct_y, openfac, linkindex_p1, linkindex_p2):
#     """Plot the facility locations, demand points, and connections."""
#     plt.figure(figsize=(10, 6))
    
#     # Plot demand points
#     plt.scatter(coordlct_x, coordlct_y, color='black', label='Demand Points')
    
#     # Plot open facilities (convert openfac to numpy array if it's a list)
#     openfac_array = np.array(openfac)
#     plt.scatter(coordlct_x[openfac_array], coordlct_y[openfac_array], color='red', label='Open Facilities', s=100)
    
#     # Connect demand points to their nearest facilities
#     for i_index in range(len(linkindex_p2)):
#         connectpoints(coordlct_x, coordlct_y, linkindex_p1[i_index], linkindex_p2[i_index])
    
#     plt.title('Random Sampling Optimisation Algorithm Solution for the P-Median Problem')
#     plt.xlabel('X Coordinate')
#     plt.ylabel('Y Coordinate')
#     plt.legend()
#     plt.grid()
#     plt.show()

# # Random Sampling Algorithm for p-median
# def random_sampling_optimisation_algorithm(coordlct_x, coordlct_y, distancelct, n, openfac, ObjValue, max_time=20):
#     """
#     Random Sampling Algorithm for the p-median problem.
#     In this version, a completely new set of facilities is randomly selected at each iteration.
    
#     Parameters:
#     - coordlct_x, coordlct_y: Coordinates of the candidate locations.
#     - distancelct: Distance matrix between the candidate locations.
#     - n: Total number of candidate locations.
#     - openfac_size: Number of facilities to open (p).
#     - ObjValue: Initial total distance for the solution.
#     - max_time: Maximum runtime for the algorithm.

#     Returns:
#     - OptSolution: The best set of facilities found.
#     - min(Objvalue_list): The smallest objective value found.
#     - cputime_i_list: List of CPU times.
#     - Objvalue_list: List of objective values over iterations.
#     """
    
#     random.seed(3)
#     iteration = 0
#     ObjValueOpt = ObjValue
#     Objvalue_list = [ObjValue]
#     OptSolution = copy.deepcopy(openfac)  # Start with the initial solution
#     program_starts = time.time()
#     cputime_i_list = [0]  # Initialize with zero time
    
#     # Convert coordinates to numpy arrays for indexing
#     coordlct_x = np.array(coordlct_x)
#     coordlct_y = np.array(coordlct_y)

#     # For storing the last best mappings for plotting
#     best_linkindex_p1 = []
#     best_linkindex_p2 = []

#     while cputime_i_list[-1] < max_time:
        
#         iteration += 1
        
#         # Step 1: Create a new solution by selecting a completely new random set of 'p' facilities
#         new_solution = random.sample(range(n), len(openfac))
        
#         # Step 2: Compute the total distance for this new solution
#         total_distance = 0
#         linkindex_p1 = []  # Demand points
#         linkindex_p2 = []  # Nearest facilities

#         for i in range(n):  # For each demand point
#             min_distance = float('inf')
#             closest_facility = None
#             for fac in new_solution:  # Find nearest facility
#                 if distancelct[i, fac] < min_distance:
#                     min_distance = distancelct[i, fac]
#                     closest_facility = fac
#             total_distance += min_distance
#             linkindex_p1.append(i)  # Demand point i
#             linkindex_p2.append(closest_facility)  # Closest facility to i
        
#         # Step 3: Update the optimal solution if the new solution is better
#         if total_distance < ObjValueOpt:
#             ObjValueOpt = copy.deepcopy(total_distance)
#             OptSolution = copy.deepcopy(new_solution)
#             best_linkindex_p1 = copy.deepcopy(linkindex_p1)
#             best_linkindex_p2 = copy.deepcopy(linkindex_p2)  # Save the best mapping
        
#         # Append objective value and CPU time to lists
#         Objvalue_list.append(ObjValueOpt)
#         now = time.time()
#         cputime_i_list.append(now - program_starts)


#         # #Code for Updating Plot

#         # plt.plot(coordlct_x, coordlct_y, 'o', color='black')

#         # # Plot current selected facilities in red
#         # current_solution_array = np.array(new_solution)
#         # plt.scatter(coordlct_x[current_solution_array], coordlct_y[current_solution_array], color='red', label='Open Facilities', s=100)

#         # for i_index in range(len(linkindex_p2)): 
#         #     connectpoints(coordlct_x,coordlct_y,linkindex_p1[i_index],linkindex_p2[i_index])
            
#         # clear_output(wait=True)
#         # plt.draw()
#         # plt.pause(0.1)
#         # plt.clf()


#         # Print the current best solution for tracking
#         print(f"Iteration: {iteration} | Best Objective Value: {ObjValueOpt}")


#     # Plot the best solution found
#     plot_solution(coordlct_x, coordlct_y, OptSolution, best_linkindex_p1, best_linkindex_p2)

#     # Return the best solution found
#     return OptSolution, min(Objvalue_list), cputime_i_list, Objvalue_list


import random
import numpy as np
import copy
import time
import matplotlib.pyplot as plt
from IPython.display import clear_output

def connectpoints(x, y, p1, p2):
    """Draw a line between two points: p1 (demand) to p2 (facility)."""
    x1, x2 = x[p1], x[p2]
    y1, y2 = y[p1], y[p2]
    plt.plot([x1, x2], [y1, y2], 'k-')  # 'k-' for black solid line

def plot_solution(coordlct_x, coordlct_y, openfac, linkindex_p1, linkindex_p2):
    """Plot the facility locations, demand points, and connections."""
    plt.figure(figsize=(10, 6))
    
    # Plot demand points (ensure they are distinct from facilities)
    demand_points = np.setdiff1d(np.arange(len(coordlct_x)), openfac)  # All points that are not open facilities
    plt.scatter(coordlct_x[demand_points], coordlct_y[demand_points], color='black', label='Demand Points', zorder=1)
    
    # Connect demand points to their nearest facilities (no facility-to-facility connections)
    for i_index in range(len(linkindex_p2)):
        if linkindex_p1[i_index] in demand_points and linkindex_p2[i_index] in openfac:
            # Only connect demand points to open facilities
            connectpoints(coordlct_x, coordlct_y, linkindex_p1[i_index], linkindex_p2[i_index])
    
    # Plot open facilities AFTER the lines, so they appear on top
    plt.scatter(coordlct_x[openfac], coordlct_y[openfac], color='red', label='Open Facilities', zorder=2)

    plt.title('Random Sampling Optimisation Algorithm Solution for the P-Median Problem')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.legend()
    plt.grid()
    plt.show()

# Random Sampling Algorithm for p-median
def random_sampling_optimisation_algorithm(coordlct_x, coordlct_y, distancelct, n, openfac, ObjValue, max_time=20):
    """
    Random Sampling Algorithm for the p-median problem.
    In this version, a completely new set of facilities is randomly selected at each iteration.
    
    Parameters:
    - coordlct_x, coordlct_y: Coordinates of the candidate locations.
    - distancelct: Distance matrix between the candidate locations.
    - n: Total number of candidate locations.
    - openfac_size: Number of facilities to open (p).
    - ObjValue: Initial total distance for the solution.
    - max_time: Maximum runtime for the algorithm.

    Returns:
    - OptSolution: The best set of facilities found.
    - min(Objvalue_list): The smallest objective value found.
    - cputime_i_list: List of CPU times.
    - Objvalue_list: List of objective values over iterations.
    """
    
    random.seed(3)
    iteration = 0
    ObjValueOpt = ObjValue
    Objvalue_list = [ObjValue]
    OptSolution = copy.deepcopy(openfac)  # Start with the initial solution
    program_starts = time.time()
    cputime_i_list = [0]  # Initialize with zero time
    
    # Convert coordinates to numpy arrays for indexing
    coordlct_x = np.array(coordlct_x)
    coordlct_y = np.array(coordlct_y)

    # For storing the last best mappings for plotting
    best_linkindex_p1 = []
    best_linkindex_p2 = []

    while cputime_i_list[-1] < max_time:
        
        iteration += 1
        
        # Step 1: Create a new solution by selecting a completely new random set of 'p' facilities
        new_solution = random.sample(range(n), len(openfac))
        
        # Step 2: Compute the total distance for this new solution
        total_distance = 0
        linkindex_p1 = []  # Demand points
        linkindex_p2 = []  # Nearest facilities

        for i in range(n):  # For each demand point
            min_distance = float('inf')
            closest_facility = None
            for fac in new_solution:  # Find nearest facility
                if distancelct[i, fac] < min_distance:
                    min_distance = distancelct[i, fac]
                    closest_facility = fac
            total_distance += min_distance
            linkindex_p1.append(i)  # Demand point i
            linkindex_p2.append(closest_facility)  # Closest facility to i
        
        # Step 3: Update the optimal solution if the new solution is better
        if total_distance < ObjValueOpt:
            ObjValueOpt = copy.deepcopy(total_distance)
            OptSolution = copy.deepcopy(new_solution)
            best_linkindex_p1 = copy.deepcopy(linkindex_p1)
            best_linkindex_p2 = copy.deepcopy(linkindex_p2)  # Save the best mapping
        
        # Append objective value and CPU time to lists
        Objvalue_list.append(ObjValueOpt)
        now = time.time()
        cputime_i_list.append(now - program_starts)

        # Print the current best solution for tracking
        print(f"Iteration: {iteration} | Best Objective Value: {ObjValueOpt}")


    # Plot the best solution found
    plot_solution(coordlct_x, coordlct_y, OptSolution, best_linkindex_p1, best_linkindex_p2)

    # Return the best solution found
    return OptSolution, min(Objvalue_list), cputime_i_list, Objvalue_list

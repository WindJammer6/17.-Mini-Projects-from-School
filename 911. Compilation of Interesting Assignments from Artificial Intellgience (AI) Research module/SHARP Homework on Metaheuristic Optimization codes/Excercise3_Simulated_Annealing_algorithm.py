# Excercise 3: Propose and implement a Simulated Annealing algorithm to solve the 
# p-median location problem


# Theory of the Simulated Annealing algorithm:
# --see the report for this homework--


# ////////////////////////////////////////////////////////////////////////////


# Implementation of the Simulated Annealing algorithm

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
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
import copy
import time
from IPython.display import clear_output


def connectpoints(x,y,p1,p2):
    x1, x2 = x[p1], x[p2]
    y1, y2 = y[p1], y[p2]
    plt.plot([x1,x2],[y1,y2],'k-')


# Swap Operator for p-median: swap one facility in openfac with one outside it
def swap_random(openfac, n, totalfac):
    closed_facilities = list(set(range(totalfac)) - set(openfac))
    to_open = random.choice(closed_facilities)
    to_close = random.choice(openfac)
    new_openfac = openfac.copy()
    new_openfac.remove(to_close)
    new_openfac.append(to_open)
    return new_openfac


# Recalculate total distance for the current facility selection
def calculate_total_distance(openfac, distancelct, n):
    total_distance = 0
    assignments = []
    
    for i in range(n):
        min_distance = float('inf')
        nearest_facility = -1
        
        for fac in openfac:
            if distancelct[i, fac] < min_distance:
                min_distance = distancelct[i, fac]
                nearest_facility = fac
        
        assignments.append(nearest_facility)
        total_distance += min_distance

    return total_distance, assignments


def plot_solution(coordlct_x, coordlct_y, openfac, linkindex_p1, linkindex_p2):
    """Plot the facility locations, demand points, and connections."""
    plt.figure(figsize=(10, 6))
    
    # Plot demand points
    plt.scatter(coordlct_x, coordlct_y, color='black', label='Demand Points', zorder=1)
    
    # Convert openfac to a numpy array of integers if it's not already
    coordlct_x = np.array(coordlct_x)
    coordlct_y = np.array(coordlct_y)
    
    # Plot open facilities (red) on top
    plt.scatter(coordlct_x[openfac], coordlct_y[openfac], color='red', label='Open Facilities', s=100, zorder=3)
    
    # Connect only demand points to their nearest facilities (avoid connecting facilities to each other)
    for i_index in range(len(linkindex_p2)):
        demand_point = linkindex_p1[i_index]
        assigned_facility = linkindex_p2[i_index]
        
        # Ensure we are only connecting demand points to facilities, not facilities to facilities
        if demand_point not in openfac and assigned_facility in openfac:
            connectpoints(coordlct_x, coordlct_y, demand_point, assigned_facility)
    
    plt.title('Simulated Annealing Optimisation Algorithm Solution for the P-Median Problem')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.legend()
    plt.grid()
    plt.show()


# Simulated Annealing Algorithm for p-median
def simulated_annealing_optimisation_algorithm(coordlct_x, coordlct_y, distancelct, n, openfac, total_distance, max_time=150, initial_temp=1000000, cooling_rate=0.9999, no_swap=1):
    random.seed(3)
    program_starts = time.time()
    
    # Initialize with current solution
    current_openfac = copy.deepcopy(openfac)
    current_obj_value = total_distance
    best_openfac = current_openfac
    best_obj_value = current_obj_value
    
    objvalue_list = [current_obj_value]
    cputime_i_list = [0]

    linkindex_p1 = np.arange(n)  # Demand points (just a list of 0 to n-1)
    
    temp = initial_temp
    iteration = 0
    it_T = 0
    
    while cputime_i_list[-1] < max_time:
        iteration += 1
        new_openfac = copy.deepcopy(current_openfac)
        
        # Apply neighborhood operator
        swap_it = 0
        while swap_it < no_swap:
            new_openfac = swap_random(new_openfac, n, len(coordlct_x))
            swap_it += 1
        
        # Calculate the objective value for the new solution
        new_obj_value, new_assignments = calculate_total_distance(new_openfac, distancelct, n)
        
        # Compute the acceptance criterion
        diff = new_obj_value - current_obj_value
        
        # Cooling schedule
        if it_T > 20:
            temp = initial_temp / float(iteration + 1)
            it_T = 0
        it_T += 1
        
        # Metropolis acceptance criterion
        metropolis = math.exp(-diff / temp) if temp > 0 else 0
        
        # Accept new solution if better, or with some probability if worse
        if diff < 0 or random.random() < metropolis:
            current_openfac = new_openfac
            current_obj_value = new_obj_value
            
            if current_obj_value < best_obj_value:
                best_openfac = copy.deepcopy(current_openfac)
                best_obj_value = current_obj_value
                best_assignments = new_assignments
            
        objvalue_list.append(current_obj_value)
        now = time.time()
        cputime_i_list.append(now - program_starts)
        

        # # Code for Updating Plot
        # plt.plot(coordlct_x, coordlct_y, 'o', color='black')

        # # Plot current selected facilities in red
        # current_solution_array = np.array(new_openfac)
        # coordlct_x = np.array(coordlct_x)
        # coordlct_y = np.array(coordlct_y)
        # plt.scatter(coordlct_x[current_solution_array], coordlct_y[current_solution_array], color='red', label='Open Facilities', s=100)

        # # Link assignments to the current solution for plotting
        # linkindex_p2 = np.array(new_assignments)  # Corresponding assigned facilities
        
        # for i_index in range(len(linkindex_p2)): 
        #     connectpoints(coordlct_x, coordlct_y, linkindex_p1[i_index], linkindex_p2[i_index])
        
        # clear_output(wait=True)
        # plt.draw()
        # plt.pause(0.1)
        # plt.clf()

        # print(f"Current best selected facilities: {best_openfac}")
        print(f"Iteration {iteration}: Best Objective Value: {best_obj_value}")

    # Prepare the link indices for plotting
    linkindex_p1 = np.arange(n)  # Demand points (just a list of 0 to n-1)
    linkindex_p2 = np.array(best_assignments)  # Corresponding assigned facilities

    # Plot the final solution
    plot_solution(coordlct_x, coordlct_y, best_openfac, linkindex_p1, linkindex_p2)

    return best_openfac, best_obj_value, cputime_i_list, objvalue_list


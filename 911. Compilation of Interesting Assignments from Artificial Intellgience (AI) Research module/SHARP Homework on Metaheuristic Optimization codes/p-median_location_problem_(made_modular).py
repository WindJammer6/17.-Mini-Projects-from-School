# The p-median location problem:
# Consider the p-median location problem: Given a set of n locations representing demand points and 
# a set of m potential facility locations, the p-median problem aims to determine the optimal selection
# of p facilities from the set of potential locations. The objective is to minimize the total distance 
# associated with serving all demand points while ensuring that each demand point is assigned to its 
# nearest facility among the selected p.

# (The p-median location problem is similar to the TSP problem (which was used to go through notes) 
# but not exactly the same but the optimisation algorithms work for both problems)


# //////////////////////////////////////////////////////////////

import random
import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np

from Excercise1_Random_Sampling_algorithm import random_sampling_optimisation_algorithm
from Excercise2_Local_Search_algorithm import hill_climbing_local_search_optimisation_algorithm
from Excercise3_Simulated_Annealing_algorithm import simulated_annealing_optimisation_algorithm


################################
# Generate Candidate Locations #
################################

################## Instance 1 ##########################
# Select random seed
random.seed(1)

# Number of candidate locations (n = total locations)
n = 100

# Number of facilities to open (p = openfac)
openfac = 15

# Coordinate Range
rangelct = 100000

# Generate random locations (candidate facilities)
coordlct_x = random.choices(range(0, rangelct), k=n)
coordlct_y = random.choices(range(0, rangelct), k=n)

# Plot the candidate locations
plt.title('Generated Candidate Facility Locations')
plt.plot(coordlct_x, coordlct_y, 'o', color='black')
plt.show()


################## Instance 2 ##########################
# # Select random seed
# random.seed(1)

# # Number of candidate locations
# n=1000

# #Number of locations to open
# openfac=30

# #Coordinate Range
# rangelct=100000

# #Generate random locations
# coordlct_x = random.choices(range(0, rangelct), k=n)
# coordlct_y = random.choices(range(0, rangelct), k=n)

# # Plot the candidate locations
# plt.title('Generated Candidate Facility Locations')
# plt.plot(coordlct_x, coordlct_y, 'o', color='black')
# plt.show()



#########################
# Compute Distance Matrix
#########################

# Create a distance matrix between candidate locations
distancelct = np.empty([n, n])
for i_index in range(n):
    for j_index in range(n):
        distancelct[i_index, j_index] = (math.sqrt(((coordlct_x[i_index] - coordlct_x[j_index]) ** 2) +
                                                   ((coordlct_y[i_index] - coordlct_y[j_index]) ** 2)))

# Set diagonal to a large number to prevent zero distance to itself
distancelct[np.diag_indices_from(distancelct)] = 99999


################################################
# Generate Initial Solution for p-median Problem
################################################

# Select random 'p' facilities to open
random.seed(1)
openfac = random.sample(list(range(n)), openfac)
print(f"Initial, random facility locations: {openfac}")

# Assign each demand point (all locations) to its nearest open facility
assignments = []
total_distance = 0

for i in range(n):
    min_distance = float('inf')
    nearest_facility = -1
    
    # Find the nearest facility for each demand point
    for fac in openfac:
        if distancelct[i, fac] < min_distance:
            min_distance = distancelct[i, fac]
            nearest_facility = fac
    
    # Assign demand point to nearest facility and calculate total distance
    assignments.append(nearest_facility)
    total_distance += min_distance

print(f"Total distance for the initial solution: {total_distance}")

# Plot the initial solution
plt.title(f'Initial p-Median Solution with {openfac} Facilities')
plt.plot(coordlct_x, coordlct_y, 'o', color='black')  # Plot all locations
for i, facility in enumerate(openfac):
    plt.plot(coordlct_x[facility], coordlct_y[facility], 'ro')  # Plot facilities in red
plt.show()


##############################################
# Run Solution Algorithms for p-median Problem
##############################################

# Use Random Sampling Optimisation Solution algorithm for p-median problem
best_openfacist, best_obj_value, cputime_i_list, objvalue_logging_list = random_sampling_optimisation_algorithm(
    coordlct_x, coordlct_y, distancelct, n, openfac, total_distance, max_time=30)

# # Example using Hill Climbing Local Search Optimisation algorithm
best_openfacist1, best_obj_value1, cputime_i_list1, objvalue_logging_list1 = hill_climbing_local_search_optimisation_algorithm(
    coordlct_x, coordlct_y, distancelct, n, openfac, total_distance, max_time=30)

# # Example using Simulated Annealing Optimisation algorithm
best_openfacist2, best_obj_value2, cputime_i_list2, objvalue_logging_list2 = simulated_annealing_optimisation_algorithm(
    coordlct_x, coordlct_y, distancelct, n, openfac, total_distance, max_time=30)



################### To plot graph for individual Solution Algorithms #######################
# # Output the smallest found objective value
# print(f"Smallest Objective Value using the Solution Algorithm: {best_obj_value}")
# print(f"Best selected facilities found using the Solution Algorithm: {best_openfacist}")

# # Plot the optimization results
# plt.title('Objective Value Results for p-Median problem Solution Algorithm')
# plt.xlabel('Time of CPU run in seconds')
# plt.ylabel('Objective Value')
# plt.plot(cputime_i_list[:len(objvalue_logging_list)], objvalue_logging_list, 'k-')

# plt.show()

# # Log the objective values and CPU times into a Pandas DataFrame
# solutiondf = pd.DataFrame({
#     'CPU Time': cputime_i_list[:len(objvalue_logging_list)],
#     'Objective Value': objvalue_logging_list
# })

# print(f"Logging Objective Values and CPU times:\n{solutiondf}")




################### To plot all Solution Algorithms in the same graph #######################
# Output the smallest found objective value for the Random Sampling Optimisation Algorithm
print(f"Smallest Objective Value using the Random Sampling Optimisaition Algorithms: {best_obj_value}")
print(f"Best selected facilities found using the Random Sampling Optimisation Algorithm: {best_openfacist}")

# Plot the optimization results
plt.title('Objective Value Results for p-Median problem Random Sampling Solution Algorithm')
plt.xlabel('Time of CPU run in seconds')
plt.ylabel('Objective Value')
plt.plot(cputime_i_list[:len(objvalue_logging_list)], objvalue_logging_list, 'k-')

plt.show()


# Output the smallest found objective value for the Hill Climbing Local Search Optimisation Algorithm
print(f"Smallest Objective Value using the Hill Climbing Local Search Optimisaition Algorithms: {best_obj_value1}")
print(f"Best selected facilities found using the Hill Climmbing Optimisation Algorithm: {best_openfacist1}")

# Plot the optimization results
plt.title('Objective Value Results for p-Median problem Hill Climbing Local Search Solution Algorithm')
plt.xlabel('Time of CPU run in seconds')
plt.ylabel('Objective Value')
plt.plot(cputime_i_list1[:len(objvalue_logging_list1)], objvalue_logging_list1, 'k-')

plt.show()


# Output the smallest found objective value for the Simulated Annealing Optimisation Algorithm
print(f"Smallest Objective Value using all the Simulated Annealing Optimisaition Algorithms: {best_obj_value2}")
print(f"Best selected facilities found using the Simulated Annealing Optimisation Algorithm: {best_openfacist2}")

# Plot the optimization results
plt.title('Objective Value Results for p-Median problem Simulated Annealing Solution Algorithm')
plt.xlabel('Time of CPU run in seconds')
plt.ylabel('Objective Value')
plt.plot(cputime_i_list2[:len(objvalue_logging_list2)], objvalue_logging_list2, 'k-')

plt.show()



# Plot the optimization results
plt.title('Objective Value Results for the p-Median problem Solution Algorithms')
plt.xlabel('Time of CPU run in seconds')
plt.ylabel('Objective Value')
plt.plot(cputime_i_list[:len(objvalue_logging_list)], objvalue_logging_list, 'k-', color='red', label='Random Sampling')
plt.plot(cputime_i_list1[:len(objvalue_logging_list1)], objvalue_logging_list1, 'k-', color='green', label='Hill Climbing Local Search')
plt.plot(cputime_i_list2[:len(objvalue_logging_list2)], objvalue_logging_list2, 'k-', color='blue', label='Simulated Annealing')
plt.legend()

plt.show()
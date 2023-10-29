#Watch the youtube tutorial on 'Using scipy integrate solve ivp' link: https://www.youtube.com/watch?v=INBu1Pyj0Is Physics with Neo

# Case 3 [Very large r, No chaos]:
# σ = 10, r = 350, b = 8/3, using [x(0), y(0), z(0)] = [0,1,0], show the y(t) as a function of time as below
# with periodic pattern that no more chaos.

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


#The Lozenz Equation:
    # 𝑥̇ = 𝜎(𝑦 − 𝑥)
    # 𝑦̇ = rx − 𝑦 − 𝑥z
    # 𝑧̇ = 𝑥y − 𝑏z

#The input 'arr' is an array containing the respective required parameters to create the Lorenz Equation of 
#the order: '[sigma, r, b, x, y, z]'
def lorenzequation(t, arr, sigma, r, b):

    #Unpacking the 'arr' array into the respective required parameters to create the Lorenz Equation
    x, y, z = arr

    dotx = sigma * (y - x)
    doty = r * x - y - x * z
    dotz = x * y - b * z

    return dotx, doty, dotz     #solve ivp is smart enough to tell this is an array so dont need the '[]' just return like that will do


if __name__ == "__main__":

    sigma_value = 10
    r_value = 350
    b_value = 8/3
    
    initial_conditions = [0,1,0]
    
    #Write about how the scipy.integrate.solve_ivp function works, its purpose and the parameters that it takes in
    #   scipy.integrate.solve_ivp(math_function, t_span, y0, method='RK45', t_eval=None, dense_output=False, 
    #                             events=None, vectorized=False, args=None, **options)

    #np.linspace vs np.arange (np.linspace is better here):
    #numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)[source]
        #Return evenly spaced numbers over a specified interval
    #numpy.arange([start, ]stop, [step, ]dtype=None, *, like=None)
        #Return evenly spaced values within a given interval

    #the 2 (0,7) needs to be same, and they represent the size span (x axis biggest number from 0 to 50 in xaxis) of the graph you want to print out i think? Numbers 0 to 7??
    solution = solve_ivp(lorenzequation, (0,7), initial_conditions, args=[sigma_value, r_value, b_value], t_eval=np.linspace(0, 7, 1500000))
    
    #Extracting the x, y, and z values
    x,y,z = solution.y
    print("x parameter values: ", x)
    print("y parameter values: ", y)
    print("z parameter values: ", z)

    #Extracting the time, t values
    t = solution.t
    print("t parameter values: ", t)

    plt.xlabel('t axis')
    plt.ylabel('y axis')

    #First parameter will be on x axis, second parameter on y axis
    plt.plot(t,y)
    plt.show()

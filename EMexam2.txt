# Problem 1 from exam 2
# By Logan Wright

"""
A square in the x-y plane has width and height of 40. Two opposing ends have V = x^2 and
the other two sides have V = 0. A conductor of V = 100 has width and height of 20 and is
also centered at the origin, centered in the larger 40x40 plate. Find V(x, y) and plot it
on a heatmap.
"""

import matplotlib.pyplot as plt
import numpy as np

# This function simply resets the boundaries only, no adjustments to important values
def resetBoundaries(V):
    # I pass through the rows, calling the direction down the rows -x, and setting
    # the value equal to x^2 on the boundary
    for index1, x in zip(range(0, 40, 1), range(-20, 20, 1)):
        V[index1][0] = x * x
        V[index1][-1] = x * x
    
    # I likewise move across all of the y values, aside from the first and last,
    # and set them to zero
    for index2, y in zip(range(1, 39, 1), range(-20, 20, 1)):
        V[0][index2] = 0
        V[-1][index2] = 0
    
    # And finally, I set V = 100 in the inner 20x20 square of charged conductor
    for index3 in range(10, 30, 1):
        for index4 in range(10, 30, 1):
            V[index3][index4] = 100.0
    
    return V

def averageRegion(V, loops = 10_000):
    # We need to make a copy of V in order to have a stationary array for reference.
    # The array V will be modified after 1 iteration in this for loop
    V_stationary = np.copy(V)
    
    # Average over the number of loops specified
    for _ in range(loops):
        # Iterate through the rows and columns being sure to avoid the first and
        # last row indeces and the first and last column indeces
        for index1, x in zip(range(1, 39, 1), range(-19, 19, 1)):
            for index2, y in zip(range(1, 39, 1), range(-19, 19, 1)):
                # Successively average the region by adding the 4 adjacent values
                # and the dividing the sum by 4
                V[index1, index2] = 1 / 4 * (V_stationary[index1 - 1, index2] + V_stationary[index1 + 1, index2] \
                                             + V_stationary[index1, index2 -1] + V_stationary[index1, index2 + 1])
        
        # After a loop, reset the boundaries for V and then update V_stationary to become the new V
        # Also, since V is an array, it is passed to this function by reference
        # and thus will be updated without needing to return the values. So I simply call the function and pass to it V
        resetBoundaries(V)
        V_stationary = np.copy(V)
    
    # Reset the boundaries once more on exit
    resetBoundaries(V)
    
    return V

# Create the initial voltage V as a 40x40 array
V = np.zeros((40, 40), dtype = float)
# Additionally, create the 2d meshgrid for matplotlib to map position the voltage values
# onto the plot
X, Y = np.meshgrid(np.array(range(-20, 20, 1), float), np.array(range(-20, 20, 1)))

# Perform the operations iteratively
averageRegion(V, 50)

# Finally, plot the figure onto a 3D heatplot
fig, ax = plt.subplots(subplot_kw = {"projection": "3d"})
surf = ax.plot_surface(X = X, Y = Y, Z = V, cmap = 'hot')

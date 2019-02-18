# -*- coding: utf-8 -*-
"""Search mechanisms.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1o9md3y9W9txhvhp3mZTzIEtnF92KzmSE

# Brute-Force Search
"""

import numpy as np
from scipy import optimize
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter


#Here we define function f. f is the function that we like to find its global minimum. Here f is the
#famous Rastrigin Function that has many local minima.
  
def f(z):
    x,y=z
    h = (x**2 - 10 * np.cos(2 * 3.14 * x)) +(y**2 - 10 * np.cos(2 * 3.14 * y)) + 20
    return (h)
  
 
# Let's take a look at how this function looks like. 

fig = plt.figure()
ax = fig.gca(projection='3d')

X = np.arange(-5, 5, 0.002)
Y = np.arange(-5, 5, 0.002)
X, Y = np.meshgrid(X, Y)
Z = f((X,Y))

surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=True) 
  
  
  
# We use Python's Scipy module and its built-in optimizer method, brute. Actually
# implementing brute force search is not that hard; define a grid, evaluate the 
#function over the grid points, and choose the point that has the minimum value.
# Of course the grid points should be close enough to make sure that we don't 
# miss a global minimum point between them. The rule of thumb is that the resolution of
# grid should be higher than the curvature of function surface, otherwise we 
# are going to miss those fine curves that fall between our grid points.
  
rranges = (slice(-4, 4,0.01), slice(-4, 4,0.01))

resbrute = optimize.brute(f, rranges,full_output=True,
                          finish=optimize.fmin)
print("The global minimum point is located at",resbrute[0])  

print("The function value at this global point is",resbrute[1])  

# For full description of how to use SciPy's brute force optimization and the arguments it takes, please see its official
#documentation at: https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.optimize.brute.html

"""# Homework
Try this technique on another function! Edit function f, and put a new function there and see whether it finds the global minimum point or not. Don't be afraid of going 3-D. But notice that if you define a 3-D function, you have to add another dimension to rranges as well.
"""

import numpy as np
from scipy import optimize
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter


#Here we define function f. f is the function that we like to find its global minimum. Here f is the
#famous Rastrigin Function that has many local minima.
  
def f(z):
    
    h =0.26*(z[0]**2+z[1]**2)-0.48*z[0]*z[1]
    return (h)
  
 
# Let's take a look at how this function looks like. 

fig = plt.figure()
ax = fig.gca(projection='3d')

X = np.arange(-5, 5, 0.002)
Y = np.arange(-5, 5, 0.002)
X, Y = np.meshgrid(X, Y)
Z = f((X,Y))

surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=True) 
  
  
  
# We use Python's Scipy module and its built-in optimizer method, brute. Actually
# implementing brute force search is not that hard; define a grid, evaluate the 
#function over the grid points, and choose the point that has the minimum value.
# Of course the grid points should be close enough to make sure that we don't 
# miss a global minimum point between them. The rule of thumb is that the resolution of
# grid should be higher than the curvature of function surface, otherwise we 
# are going to miss those fine curves that fall between our grid points.
  
rranges = (slice(-4, 4,0.01), slice(-4, 4,0.01))

resbrute = optimize.brute(f, rranges,full_output=True,
                          finish=optimize.fmin)
print("The global minimum point is located at",resbrute[0])  

print("The function value at this global point is",resbrute[1])  

# For full description of how to use SciPy's brute force optimization and the arguments it takes, please see its official
#documentation at: https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.optimize.brute.html

"""#Random Search"""

import numpy as np
from numpy import random
from scipy import optimize
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from random import randint
                    
numIter=200000;

def f(z):
    
    h = (z[0]**2 - 10 * np.cos(2 * 3.14 * z[0])) +(z[1]**2 - 10 * np.cos(2 * 3.14 * z[1])) + 20
    return (h)
  
 
# Let's take a look at how this function looks like. 

fig = plt.figure()
ax = fig.gca(projection='3d')

X = np.arange(-5, 5, 0.002)
Y = np.arange(-5, 5, 0.002)
X, Y = np.meshgrid(X, Y)
Z = f((X,Y))

best = (X[0][0], Y[0][0], Z[0][0])
for i in range(1, numIter):
  randX = randint(0,4999)
  randY = randint(0,4999)
  if (Z[randX][randY] <= best[2]):
    best = (randX, randY, Z[randX][randY])
  
print(best[2])

surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=True)

"""# Simulated Annealing"""

#codes for SA is coming from Brigham Young University's ME 575's Optimization course, taught by Professor: John D. Hedengren. Codes are partially edited by me. - Behnam Kia
# Import some other libraries that we'll need
# matplotlib and numpy packages must also be installed
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import random
import math

# define objective function
def f(x):
    x1 = x[0]
    x2 = x[1]
    obj = 0.2 + x1**2 + x2**2 - 0.1*math.cos(6.0*3.1415*x1) - 0.1*math.cos(6.0*3.1415*x2)
    return obj

# Start location
x_start = [0.8, -0.5]

# Design variables at mesh points
i1 = np.arange(-1.0, 1.0, 0.01)
i2 = np.arange(-1.0, 1.0, 0.01)
x1m, x2m = np.meshgrid(i1, i2)
fm = np.zeros(x1m.shape)
for i in range(x1m.shape[0]):
    for j in range(x1m.shape[1]):
        fm[i][j] = 0.2 + x1m[i][j]**2 + x2m[i][j]**2 \
             - 0.1*math.cos(6.0*3.1415*x1m[i][j]) \
             - 0.1*math.cos(6.0*3.1415*x2m[i][j])

# Create a contour plot
plt.figure()
# Specify contour lines
#lines = range(2,52,2)
# Plot contours
CS = plt.contour(x1m, x2m, fm)#,lines)
# Label contours
plt.clabel(CS, inline=1, fontsize=10)
# Add some text to the plot
plt.title('Non-Convex Function')
plt.xlabel('x1')
plt.ylabel('x2')

##################################################
# Simulated Annealing
##################################################
# Number of cycles
n = 50
# Number of trials per cycle
m = 50
# Number of accepted solutions
na = 0.0
# Probability of accepting worse solution at the start
p1 = 0.7
# Probability of accepting worse solution at the end
p50 = 0.001
# Initial temperature
t1 = -1.0/math.log(p1)
# Final temperature
t50 = -1.0/math.log(p50)
# Fractional reduction every cycle
frac = (t50/t1)**(1.0/(n-1.0))
# Initialize x
x = np.zeros((n+1,2))
x[0] = x_start
xi = np.zeros(2)
xi = x_start
na = na + 1.0
# Current best results so far
xc = np.zeros(2)
xc = x[0]
fc = f(xi)
fs = np.zeros(n+1)
fs[0] = fc
# Current temperature
t = t1
# DeltaE Average
DeltaE_avg = 0.0
for i in range(n):
    for j in range(m):
        # Generate new trial points
        xi[0] = xc[0] + random.random() - 0.5
        xi[1] = xc[1] + random.random() - 0.5
        # Clip to upper and lower bounds
        xi[0] = max(min(xi[0],1.0),-1.0)
        xi[1] = max(min(xi[1],1.0),-1.0)
        DeltaE = abs(f(xi)-fc)
        if (f(xi)>fc):
            # Initialize DeltaE_avg if a worse solution was found
            #   on the first iteration
            if (i==0 and j==0): DeltaE_avg = DeltaE
            # objective function is worse
            # generate probability of acceptance
            p = math.exp(-DeltaE/(DeltaE_avg * t))
            # determine whether to accept worse point
            if (random.random()<p):
                # accept the worse solution
                accept = True
            else:
                # don't accept the worse solution
                accept = False
        else:
            # objective function is lower, automatically accept
            accept = True
        if (accept==True):
            # update currently accepted solution
            xc[0] = xi[0]
            xc[1] = xi[1]
            fc = f(xc)
            # increment number of accepted solutions
            na = na + 1.0
            # update DeltaE_avg
            DeltaE_avg = (DeltaE_avg * (na-1.0) +  DeltaE) / na
    # Record the best x values at the end of every cycle
    x[i+1][0] = xc[0]
    x[i+1][1] = xc[1]
    fs[i+1] = fc
    # Lower the temperature for next cycle
    t = frac * t

# print solution
print('Best solution: ' + str(xc))
print('Best objective: ' + str(fc))

plt.plot(x[:,0],x[:,1],'y-o')
plt.savefig('contour.png')

fig = plt.figure()
ax1 = fig.add_subplot(211)
ax1.plot(fs,'r.-')
ax1.legend(['Objective'])
ax2 = fig.add_subplot(212)
ax2.plot(x[:,0],'b.-')
ax2.plot(x[:,1],'g--')
ax2.legend(['x1','x2'])

# Save the figure as a PNG
plt.savefig('iterations.png')

plt.show()
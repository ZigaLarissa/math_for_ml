#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sympy as sp


# the derivative function
def dy_dx(expression, variable='x'):
    x = sp.symbols(variable)
    f = sp.sympify(expression)
    derivative = sp.diff(f, x)
    return derivative


# # Task 2: Test the derivative function written with a quadratic equation of your choice
# *NB: Must have atleast 2 minimas and atleast 2 maximas*
# let's define x

x = sp.symbols('x')
def f(x):
    return x


# let's define f(x) = x^2 + 5x + 6
    
def g(x):
    g_x = x**2 + 5*x + 6
    return g_x


# find the derivative of g(x)
der = dy_dx(g(x))
print("The original function is: ", g(f(x)))
print("The derivative is: ", der)


#Create a visualization of the quadratic equation

x = np.linspace(-15, 10, 100)
y = g(x)

plt.xlabel('x')
plt.ylabel('y')
plt.title('The Quadratic Equation')
plt.plot(x, y)


# Create separate array of Minimas and maximas

def get_max_min(equation):
    x = sp.symbols('x')
    derivative = dy_dx(equation, 'x')
    critical_pts = sp.solve(derivative, x)
    x_critical_pts = []
    y_critical_pts = []
    
    for point in critical_pts:
        values = equation.subs(x, point)
        x_critical_pts.append(point)
        y_critical_pts.append(values)
        
    return x_critical_pts, y_critical_pts

y = 'x**3 - 9*x**2 + 15*x + 4'
equation = sp.sympify(y)
arr_minimas, arr_maximas = get_max_min(equation)

print(f'the array of minimas is {arr_minimas} and the array of maximas is {arr_maximas}')


# the global Minima and the Global maxima _ Plot this so that I can see

x = np.linspace(-25, 15, 100)
y = g(x)

plt.plot(x, y, label='equation')
plt.scatter(arr_minimas, [g(point) for point in arr_minimas], color='red', marker='o', label='Minima')
plt.scatter(arr_maximas, [g(point) for point in arr_maximas], color='green', marker='o', label='Maxima')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('The Quadratic Equation with Minima and Maxima illustrated')
plt.show()
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import random
import decimal

def func(X, Y):
    #return (.26 * (X**2 + Y**2) - (.48*X*Y))
    return -np.sqrt((X-1)**2+(Y+2)**2) + np.sin(X+(Y**2))

def math_function(x_range, y_range):
    X = np.arange(x_range[0], x_range[1], x_range[2])
    Y = np.arange(y_range[0], y_range[1], y_range[2])
    X, Y = np.meshgrid(X, Y)
    Z = func(X, Y)
    return X,Y,Z


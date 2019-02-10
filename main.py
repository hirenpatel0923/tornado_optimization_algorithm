from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import random
import decimal
from tornado_functions import *
from tornado import Tornado


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

rng = (-8,8)
x_range = (rng[0],rng[1],.25)
y_range = (rng[0],rng[1],.25)
X, Y, Z = math_function(x_range, y_range)

ax.plot_wireframe(X, Y, Z, rstride=1, cstride=1)


tornado_lst = []
lst_x = []
lst_y = []
lst_z = []
for i in range(10):
    t = Tornado(rng, func)
    lst_x.append(t.x)
    lst_y.append(t.y)
    lst_z.append(t.current_cost)
    if i < 5:
        t.theta_rate = 20
        t.r_rate = 5
    tornado_lst.append(t)


def tornado_radius_movement(index, tornado, ax):
    r = tornado.r
    theta = tornado.theta
    for i in range(tornado.r_rate):
        if tornado.r_dir_forward:
            r = tornado.r + tornado.r_diff
        else:
            r = tornado.r - tornado.r_diff

        x_new, y_new = tornado.calculate_xy(r, theta)
        z_new = func(x_new, y_new) 
        tornado.calculate_current_cost()

        if z_new > tornado.current_cost:
            tornado.r_dir_forward = True
            tornado.r_diff *= 1.2
            tornado.x, tornado.y, tornado.current_cost, tornado.r = x_new, y_new, z_new, r
            lst_x[index] = tornado.x
            lst_y[index] = tornado.y
            lst_z[index] = tornado.current_cost
        else:
            tornado.r_dir_forward = False
            tornado.r_diff /= 1.2

        #tornado.x, tornado.y, tornado.current_cost, tornado.r = x_new, y_new, z_new, r
        plot = ax.scatter(lst_x, lst_y, lst_z, color='red')
        plt.pause(.1)
        plot.remove()

def tornado_theta_movement(index, tornado, ax):
    r = tornado.r
    theta = tornado.theta
    for i in range(tornado.theta_rate):
        if tornado.t_dir_forward:
            theta += tornado.theta_diff
        else:
            theta -= tornado.theta_diff

        x_new, y_new = tornado.calculate_xy(r, theta)
        z_new = func(x_new, y_new) 
        tornado.calculate_current_cost()

        if z_new > tornado.current_cost:
            diff = z_new - tornado.current_cost
            if diff > tornado.z_diff_prev:
                tornado.theta_diff /= 1.2
            else:
                tornado.theta_diff *= 1.2
            tornado.z_diff_prev = diff
            tornado.t_dir_forward = True
            tornado.x, tornado.y, tornado.current_cost, tornado.theta = x_new, y_new, z_new, theta
            lst_x[index] = tornado.x
            lst_y[index] = tornado.y
            lst_z[index] = tornado.current_cost
        else:
            tornado.t_dir_forward = False
        
        #tornado.x, tornado.y, tornado.current_cost, tornado.theta = x_new, y_new, z_new, theta
        plot = ax.scatter(lst_x, lst_y, lst_z, color='red')
        plt.pause(.1)
        plot.remove()

#main function code
for i in range(100):
    for index, t in enumerate(tornado_lst):
        tornado_radius_movement(index, t, ax)
        tornado_theta_movement(index, t, ax)


for t in tornado_lst:
    ax.scatter(t.x, t.y, t.current_cost, color='red')


plt.show()
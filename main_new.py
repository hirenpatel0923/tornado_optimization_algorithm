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

ax.plot_wireframe(X, Y, Z, rstride=1, cstride=1, color='grey')

total_tornados = 20
r_rate = 16
t_rate = 4

colors = cm.rainbow(np.linspace(0,.5,int(total_tornados/2)))
colors_violent = cm.rainbow(np.linspace(.5,1,int(total_tornados/2)))

iteration_count = 201
tornado_lst = []
tornado_lst_violent = []
lst_x = []
lst_y = []
lst_z = []

lst_x_violent = []
lst_y_violent = []
lst_z_violent = []
for i in range(total_tornados):
    if i < total_tornados/2:
        t = Tornado(rng, func, t_rate, r_rate)
        t.is_violent = True

        lst_x_violent.append(t.x)
        lst_y_violent.append(t.y)
        lst_z_violent.append(t.current_cost)
        tornado_lst_violent.append(t)
    else:
        t = Tornado(rng, func, r_rate, t_rate)

        lst_x.append(t.x)
        lst_y.append(t.y)
        lst_z.append(t.current_cost)
        tornado_lst.append(t)


def tornado_radius_movement(index, tornado, ax):
    r = tornado.r
    theta = tornado.theta
    if tornado.r_counter < tornado.r_rate:
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
            tornado.position_change = True
            tornado.position_change_counter = 0

            if tornado.is_violent:
                lst_x_violent[index] = tornado.x
                lst_y_violent[index] = tornado.y
                lst_z_violent[index] = tornado.current_cost
            else:
                lst_x[index] = tornado.x
                lst_y[index] = tornado.y
                lst_z[index] = tornado.current_cost
        else:
            tornado.r_dir_forward = False
            tornado.r_diff /= 1.2
            tornado.position_change = False
            tornado.position_change_counter += 1

        #tornado.x, tornado.y, tornado.current_cost, tornado.r = x_new, y_new, z_new, r
        # plot = ax.scatter(lst_x, lst_y, lst_z, s=100, color=colors)
        # plot_violent = ax.scatter(lst_x_violent, lst_y_violent, lst_z_violent, s=100, color=colors_violent)
        
        plot = ax.scatter(lst_x, lst_y, lst_z, s=100, color='blue')
        plot_violent = ax.scatter(lst_x_violent, lst_y_violent, lst_z_violent, s=100, color='red')

        
        plt.pause(.00001)
        plot.remove()
        plot_violent.remove()

        tornado.r_counter += 1  
    else:
        tornado_theta_movement(index, tornado, ax)

def tornado_theta_movement(index, tornado, ax):
    r = tornado.r
    theta = tornado.theta
    if tornado.t_counter < tornado.theta_rate:
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
            tornado.position_change = True
            tornado.position_change_counter = 0
            
            if tornado.is_violent:
                lst_x_violent[index] = tornado.x
                lst_y_violent[index] = tornado.y
                lst_z_violent[index] = tornado.current_cost
            else:
                lst_x[index] = tornado.x
                lst_y[index] = tornado.y
                lst_z[index] = tornado.current_cost
        else:
            tornado.t_dir_forward = False
            tornado.position_change = False
            tornado.position_change_counter += 1
        
        #tornado.x, tornado.y, tornado.current_cost, tornado.theta = x_new, y_new, z_new, theta
        # plot = ax.scatter(lst_x, lst_y, lst_z, s=100, color=colors)
        # plot_violent = ax.scatter(lst_x_violent, lst_y_violent, lst_z_violent, s=100, color=colors_violent)
        
        plot = ax.scatter(lst_x, lst_y, lst_z, s=100, color='blue')
        plot_violent = ax.scatter(lst_x_violent, lst_y_violent, lst_z_violent, s=100, color='red')

        
        plt.pause(.00001)
        plot.remove()
        plot_violent.remove()

        tornado.t_counter += 1

    else:
        tornado.t_counter = 0
        tornado.r_counter = 0

local_maxima_lst = [-999 for i in range(int(total_tornados/2))]
local_maxima_lst_coord = [0 for i in range(int(total_tornados/2))]
local_maxima_lst_violent = [-999 for i in range(int(total_tornados/2))]
local_maxima_lst_violent_coord = [0 for i in range(int(total_tornados/2))]

#main function code
for i in range(iteration_count):
    for index, t in enumerate(tornado_lst):
        if t.position_change_counter > (r_rate + t_rate):
            #print("tornado ", index, " reached local maxiama.")
            x = random.uniform(rng[0],rng[1])
            y = random.uniform(rng[0],rng[1])
            #if func(x,y) > t.current_cost:
                #print("tornado ", index, " found new position.")
            t.position_change = True
            t.position_change_counter = 0
            t.x = x
            t.y = y
            t.calculate_current_cost()

        tornado_radius_movement(index, t, ax)

        if local_maxima_lst[index] < t.current_cost:
            local_maxima_lst[index] = t.current_cost
            local_maxima_lst_coord[index] = [t.x, t.y]
            # print("strong tornado: ", index)
            # print("maxima : ",t.current_cost)
            # print("=======================================")

    for index, t in enumerate(tornado_lst_violent):
        if t.position_change_counter > (r_rate + t_rate):
            #print("tornado ", index, " reached local maxiama.")
            x = random.uniform(rng[0],rng[1])
            y = random.uniform(rng[0],rng[1])
            #if func(x,y) > t.current_cost:
                #print("tornado ", index, " found new position.")
            t.position_change = True
            t.position_change_counter = 0
            t.x = x
            t.y = y
            t.calculate_current_cost()

        tornado_radius_movement(index, t, ax)
        
        if local_maxima_lst_violent[index] < t.current_cost:
            local_maxima_lst_violent[index] = t.current_cost
            local_maxima_lst_violent_coord[index] = [t.x, t.y]
            # print("violent tornado: ", index)
            # print("maxima : ",t.current_cost)
            # print("=======================================")



    if i%100==0:
        print("iteration : ",(i/100))


ax.scatter(lst_x, lst_y, lst_z, s=100, color='green')
ax.scatter(lst_x_violent, lst_y_violent, lst_z_violent, s=100, color='brown')
plt.show()



print("===============================================")
#print("Local maxima List : ",local_maxima_lst)
max_index = local_maxima_lst.index(max(local_maxima_lst))
print("local maxima strong: ", max(local_maxima_lst))
print("position : ", local_maxima_lst_coord[max_index])


print("===============================================")
#print("Local maxima List Violent: ",local_maxima_lst_violent)
max_index = local_maxima_lst_violent.index(max(local_maxima_lst_violent))
print("local maxima violent: ", max(local_maxima_lst_violent))
print("position : ", local_maxima_lst_violent_coord[max_index])


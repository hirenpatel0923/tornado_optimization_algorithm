import numpy as np
import random
from tornado_functions import func

class Tornado():
    def __init__(self, range, func, r_rate, t_rate):
        self.x = random.uniform(range[0],range[1])
        self.y = random.uniform(range[0],range[1])
        self.r = random.uniform(range[0],range[1])
        self.r_diff = random.uniform(0,1)
        self.r_dir_forward = True
        self.r_rate = r_rate
        self.theta = random.randint(0, 360)
        self.theta_diff = random.uniform(0,5)
        self.t_dir_forward = True
        self.theta_rate = t_rate
        self.current_cost = 0
        self.z_diff_prev = 0
        self.growth_rate = 0
        self.r_counter = 0
        self.t_counter = 0
        self.position_change = False
        self.position_change_counter = 0
        self.is_violent = False
        self.calculate_current_cost()

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_r(self, r):
        self.r = r
    
    def set_theta(self, theta):
        self.theta = theta

    def get_r(self):
        return self.r

    def get_theta(self):
        return self.theta

    def calculate_current_cost(self):
        self.current_cost = func(self.x, self.y)

    def calculate_xy(self, r, theta):
        x = r * np.cos(np.pi * theta / 360)
        y = r * np.sin(np.pi * theta / 360)
        return x, y

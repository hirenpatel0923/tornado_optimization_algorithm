from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import random
import decimal

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Grab some test data.
X = np.arange(-8, 8, 0.25)
Y = np.arange(-8, 8, 0.25)
X, Y = np.meshgrid(X, Y)
Z = -np.sqrt((X-1)**2+(Y+2)**2) + np.sin(X+(Y**2))

# Plot a basic wireframe.
ax.plot_wireframe(X, Y, Z, rstride=1, cstride=1)

init_tornados = 6
total_iterations = 1000
R=[]
thetas=[]
x=[]
y=[]
z=[]
#taking a random starting radius and angle for each initial tornado
for i in range(init_tornados):
    R.append(decimal.Decimal(random.randrange(-800, 800))/100)
    thetas.append(random.randrange(-180, 180))
    x.append(float(R[i])*np.cos(np.pi*thetas[i]/180))
    y.append(float(R[i])*np.sin(np.pi*thetas[i]/180))
    z.append(-np.sqrt((x[i]-1)**2+(y[i]+2)**2) + np.sin(x[i]+(y[i]**2)))

'''for i in range(total_iterations):
    for j in range(init_tornados):
'''

abc=ax.scatter(x,y,z,color='red')
x=[1.052,2,3]
y=[1,2.2394,3]
z=[1,2,3.983745]
plt.pause(4)
abc.remove()
ax.scatter(x,y,z,color='red')
plt.show()

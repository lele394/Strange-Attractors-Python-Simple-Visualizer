"""

available mode : Lorenz : Edward Lorenz's famous butterfly attractor
                 default : put your own 3D attractor here


nb : parameter rho, beta, and sigma of Lorenz attractor can be modified in NextStep function
"""





startingPosition = [1, 10, 1] #starting point position
iterations = 10000 #number of points to compute
mode = "Lorenz" #mode




import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm


axe = plt.figure().add_subplot(projection='3d')






def NextStep(pos, mode="default"):
    if mode == "default":
        x = 0
        y = 0
        z = 0
        return x, y, z
    
    elif mode == "Lorenz":
        rho = 28
        sigma = 10
        beta = 8/3

        px = pos[0]
        py = pos[1]
        pz = pos[2]
        
        x = sigma * (py - px)
        y = px * (rho - pz) - py
        z = px*py - beta * pz

        return x, y, z





X = [startingPosition[0]]
Y = [startingPosition[1]]
Z = [startingPosition[2]]

sx, sy, sz = startingPosition[0], startingPosition[1], startingPosition[2]



for i in range(iterations):


    dt = 0.005

    ax, ay, az = NextStep([sx, sy, sz], mode)
    
    sx+=ax * dt
    sy+=ay * dt
    sz+=az * dt
    
    X.append(sx)
    Y.append(sy)
    Z.append(sz)


axe.plot(X, Y, Z, marker="", linewidth=0.7)

plt.show()

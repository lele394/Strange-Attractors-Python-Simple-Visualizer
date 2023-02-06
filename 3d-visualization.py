"""

available mode : Lorenz : Edward Lorenz's famous butterfly attractor
                 Bouali : http://chaos-3d.e-monsite.com/medias/files/nody2.pdf


nb : parameter rho, beta, and sigma of Lorenz attractor can be modified in NextStep function
"""





startingPosition = [1, 10, 1] #starting point position
iterations = 10000 #number of points to compute
mode = "Bouali" #mode




import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm


axe = plt.figure().add_subplot(projection='3d')






def NextStep(pos, mode="default"):
    
    
    
    
    
    
    if mode == "Bouali":
        a = 4
        alpha = 0.3
        b = 1
        c = 1.5
        beta = 0.05
        s = 1

        px = pos[0]
        py = pos[1]
        pz = pos[2]
        
        x = px*(a-py) + alpha * pz
        y = -py*(b-px*px)
        z = -px*(c-s*pz) - beta*pz
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

    if(i%100000 == 0): print(i, "   ", i/iterations*100, "%")

    dt = 0.05

    ax, ay, az = NextStep([sx, sy, sz], mode)
    
    sx+=ax * dt
    sy+=ay * dt
    sz+=az * dt
    
    X.append(sx)
    Y.append(sy)
    Z.append(sz)

print("rendering")
axe.plot(X, Y, Z, marker="", linewidth=0.7)

plt.show()

"""
feel free to message me to add new attractors

available mode : default : put your own 3D attractor here
                 Clifford 
                 Juan
                 Henon


"""





startingPosition = [0.1, 0.1] #starting point position
iterations = 1000000 #number of points to compute
mode = "Henon" #mode

_MARKERWIDTH = 0.02 #if lower than one, will be transparent, can be used to trace "occupation maps"




import matplotlib.pyplot as plt
from math import cos, sin


axe = plt.figure().add_subplot()






def NextStep(pos, mode="default"):
    
    px = pos[0]
    py = pos[1]



    if mode == "default":
        x = 0
        y = 0
        return x, y

    elif mode == "Clifford":
        alpha = 1.7
        beta = 1.8
        gamma = 0.9
        delta = 0.4

        x = sin(alpha * py) + gamma * cos(alpha * px)
        y = sin(beta * px) + delta * cos(beta * py)

        return x, y

    elif mode == "Juan":
        c0 = -0.7623860293700191
        c1 = -0.6638578730949067
        c2 = 1.8167801002094635
        c3 = -2.7677186549504844

        x = cos(c0 * px)**2 - sin(c1 * py)**2
        y = 2*cos(c2 * px) * sin(c3 * py)

        return x, y
        

    elif mode == "Henon":
        a = 1.4
        b = 0.3

        x = 1 + py - a * px**2
        y = b * px

        return x, y
    






X = [startingPosition[0]]
Y = [startingPosition[1]]


sx, sy = startingPosition[0], startingPosition[1]



for i in range(iterations):


    if(i%100000 == 0): print(i, "   ", i/iterations*100, "%")

    sx, sy = NextStep([sx, sy], mode)
    

    
    X.append(sx)
    Y.append(sy)

print("rendering")
axe.plot(X, Y, marker=".", linewidth=0, markersize=_MARKERWIDTH)

plt.show()

"""
feel free to message me to add new attractors

available mode : default : put your own 3D attractor here
                 Clifford 



"""





startingPosition = [1, 1] #starting point position
iterations = 10000000 #number of points to compute
mode = "Clifford" #mode

_MARKERWIDTH = 0.02 #if lower than one, will be transparent, can be used to trace "occupation maps"




import matplotlib.pyplot as plt
from math import cos, sin


axe = plt.figure().add_subplot()






def NextStep(pos, mode="default"):
    if mode == "default":
        x = 0
        y = 0
        return x, y

    elif mode == "Clifford":
        alpha = 1.7
        beta = 1.8
        gamma = 0.9
        delta = 0.4

        px = pos[0]
        py = pos[1]

        x = sin(alpha * py) + gamma * cos(alpha * px)
        y = sin(beta * px) + delta * cos(beta * py)

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

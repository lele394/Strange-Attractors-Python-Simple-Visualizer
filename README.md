# Strange-Attractors-Python-Simple-Visualizer


A simple python based visualizer for attractors using Matplotlib's pyplot library.

## 3D Attractors

list of current 3D attractors and their equations

#### Lorenz 

x = sigma * (py - px) * dt <br>
y = px * (rho - pz) - py * dt <br>
z = px*py - beta * pz * dt <br>

#### Bouali

x = px*(a-py) + alpha * pz
y = -py*(b-px*px)
z = -px*(c-s*pz) - beta*pz

<br><br><br>

## 2D Attractors

#### Clifford
x = sin(alpha * py) + gamma * cos(alpha * px)
y = sin(beta * px) + delta * cos(beta * py)


#### Juan
x = cos(c0 * px)**2 - sin(c1 * py)**2
y = 2*cos(c2 * px) * sin(c3 * py)

list of current 3D attractors and their equations

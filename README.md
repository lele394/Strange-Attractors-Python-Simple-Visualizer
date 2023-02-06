# Strange-Attractors-Python-Simple-Visualizer


A simple python based visualizer for attractors using Matplotlib's pyplot library.

*might make something out of [that](http://paulbourke.net/fractals/sprott/) one day, looks dope ngl*

Heavily inspired from [Paul Bourke's website](http://paulbourke.net/fractals/)

## 3D Attractors

list of current 3D attractors and their equations

#### Lorenz 

x = sigma * (py - px) * dt <br>
y = px * (rho - pz) - py * dt <br>
z = px * py - beta * pz * dt <br>

#### Bouali

x = px * (a-py) + alpha * pz * dt <br>
y = -py * (b-px * px) * dt <br>
z = -px * (c-s * pz) - beta * pz * dt <br>

#### Arneodo
x = py * dt <br>
y = pz * dt <br>
z = a * px -  b * py - pz - c * px * px * px * dt <br>

#### Den Tsucs
x = a * (py - px) + d * px * pz * dt <br>
y = f * py - px * pz * dt <br>
z = c * pz + px * py - e * px * px * dt <br>
<br><br><br>

## 2D Attractors
list of current 2D attractors and their equations
#### Clifford
x = sin(alpha * py) + gamma * cos(alpha * px) <br>
y = sin(beta * px) + delta * cos(beta * py) <br>


#### Juan
x = cos(c0 * px)**2 - sin(c1 * py)**2 <br>
y = 2*cos(c2 * px) * sin(c3 * py) <br>

#### Henon
x = 1 + py - a * px**2 <br>
y = b * px <br>




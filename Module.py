import statistics
from math import sin, pi

import mymodule
mymodule.eMobilis("eMobilis Mobile Technology")

dataset=[4,5,8,2,7,1,6,8,10]
x=statistics.mean(dataset)
y=statistics.median(dataset)
z=statistics.mode(dataset)
w=statistics.geometric_mean(dataset)
q=sin(pi/2)

print("Mean is",x)
print("Median is",y)
print("Mode is",z)
print("Geometric_mean is",w)
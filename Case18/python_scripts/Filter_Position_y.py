import os
import math
Number_of_sides=20
theta=2*math.pi/Number_of_sides
radius=0.4385
CenterX=0.6
CenterY=0.6
x = []
y = []
for i in range (0,Number_of_sides):
   x.append(radius*math.sin((i*theta)-theta)+CenterX)
   y.append(radius*math.cos((i*theta)-theta)+CenterY)

print (y)

#for j in range (0,Number_of_sides):
    #surfaceTransformPoints -translate "(x[j] y[j] 0)" filter.stl filter1.stl
#    os.system("cp filter.stl filter+str(j)+.stl")
    
#os.system("for j in 1 2 3 4 5; do cp filter.stl filter$j.stl; done")

#os.system("for j in {1..5}; do cp filter.stl filter$j.stl; done")

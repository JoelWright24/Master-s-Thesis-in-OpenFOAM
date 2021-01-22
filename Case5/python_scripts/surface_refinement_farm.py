import math

   
for i in range (0,100):
    print("	filter_%d\n	{\n	    level (3 3);\n	    cellZone cz_solid_%d;\n	    faceZone fz_solid_%d;\n	    cellZoneInside inside;\n	}" % (i, i, i))


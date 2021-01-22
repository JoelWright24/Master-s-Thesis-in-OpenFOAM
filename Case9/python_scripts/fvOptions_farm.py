import math


for i in range (0,100):
    print("source%d \n{ \n    type	explicitPorositySource;\n    explicitPorositySourceCoeffs\n    {\n	type            DarcyForchheimer;\n	selectionMode   cellZone;\n	cellZone        cz_solid_%d;\n	DarcyForchheimerCoeffs\n	{\n	    d   d [0 -2 0 0 0 0 0] (3e12 0 3e12);\n	    f   f [0 -1 0 0 0 0 0] (4e5 0 4e5);\n            coordinateSystem\n	    {\n                type    cartesian;\n                origin  (0 0 0);\n                coordinateRotation\n                {\n                    type    axesRotation;\n                    e1  (1 0 0);\n                    e2  (0 1 0);\n                }\n            }\n        }\n    }\n}\n" % (i, i))



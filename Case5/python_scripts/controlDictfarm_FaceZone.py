import math

for i in range (0,100):
    print("   massFlowAtFilter_%i\n   {\n        type            surfaceFieldValue;\n        functionObjectLibs (\"libfieldFunctionObjects.so\");\n        enabled         true;\n	surfaceFormat	vtk;\n        writeControl    timeStep;\n        writeInterval   1250;\n        log             true;\n        writeFields     true;\n        regionType      faceZone;\n        name            fz_solid_%d;\n        operation       sum;\n        fields\n        (\n            phi\n        );\n   }" % (i, i))
    



import math

for i in range (0,100):
    print("   volFieldValue_%i\n   {\n        type            volFieldValue;\n        libs (\"libfieldFunctionObjects.so\");\n        enabled         true;\n        fields\n        (\n            U\n        );\n        operation       volIntegrate;\n	surfaceFormat	vtk;\n        writeControl    timeStep;\n        writeInterval   1250;\n        log             true;\n        writeFields     true;\n        regionType      cellZone;\n        name            cz_solid_%d;\n   }" % (i, i))
    


	
    

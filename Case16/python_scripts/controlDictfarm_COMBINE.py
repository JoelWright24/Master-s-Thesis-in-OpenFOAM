import math

for i in range (0,100):
    print("   volFieldValue_%i\n   {\n        type            volFieldValue;\n        libs (\"libfieldFunctionObjects.so\");\n        enabled         true;\n        fields\n        (\n            U\n        );\n        operation       volIntegrate;\n	surfaceFormat	null;\n        writeControl    timeStep;\n        writeInterval   12500;\n        log             true;\n        writeFields     true;\n        regionType      cellZone;\n        name            cz_solid_%d;\n   }" % (i, i))
    print("   massFlowAtFilter_%i\n   {\n        type            surfaceFieldValue;\n        functionObjectLibs (\"libfieldFunctionObjects.so\");\n        enabled         true;\n	surfaceFormat	null;\n        writeControl    timeStep;\n        writeInterval   12500;\n        log             true;\n        writeFields     true;\n        regionType      faceZone;\n        name            fz_solid_%d;\n        operation       sum;\n        fields\n        (\n            phi\n        );\n   }" % (i, i))
    


	
    

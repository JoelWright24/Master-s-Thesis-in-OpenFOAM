import math

   
for i in range (0,100):
    print("filter_%d.stl\n{\n    extractionMethod    extractFromSurface;\n    extractFromSurfaceCoeffs\n    {\n    includedAngle   120;\n    }\n    baffles (porosityFaces);\n    writeObj        yes;\n}" % (i))



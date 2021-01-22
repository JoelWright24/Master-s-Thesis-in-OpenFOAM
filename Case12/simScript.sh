#!/bin/bash


# STEP1: rename the stl files with .stl

# mv constant/triSurface/filter.STL constant/triSurface/filter.stl
# mv constant/triSurface/chamber.STL constant/triSurface/chamber.stl

# STEP2: translate the stl files

# surfaceTransformPoints -scale "(0.001 0.001 0.001)" constant/triSurface/filter.stl constant/triSurface/filter.stl
# surfaceTransformPoints -scale "(0.001 0.001 0.001)" constant/triSurface/chamber.stl constant/triSurface/chamber.stl

# STEP 3: print the filter files from the pythonFiles 

# x=($(python3 ./python_scripts/Filter_Position_x.py | tr -d '[],'))
# z=($(python3 ./python_scripts/Filter_Position_y.py | tr -d '[],'))
# layer=(0.02 0.315 0.61 0.905 1.2)
# raise=0.02
# counter=0
# for i in "${!layer[@]}"
# do
# for j in "${!x[@]}"
# do
# surfaceTransformPoints -translate "( ${x[$j]} ${layer[$i]} ${z[$j]} )" constant/triSurface/filter.stl constant/triSurface/filter_$counter.stl
# counter=$((counter+1))
# done
# done 

# STEP 4: classic run scripts stuff
blockMesh
surfaceFeatureExtract
snappyHexMesh -overwrite
topoSet
createPatch -overwrite
setSet -batch system/setSetDict
rm 0/cellLevel
rm 0/pointLevel
splitMeshRegions -cellZonesOnly -overwrite
decomposePar
mpirun -np 4 bouSimpleFoam -parallel >& solver.log &

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#%%
import numpy as np
import trimesh
import os
import glob

# Create a folder for all surface/mesh files, and create a nested folder inside this one called "output"
os.chdir(".....") # assign that folder here
filelist = glob.glob("*.obj") # or whatever file extension your meshes have

# Create lists for results (volumes, CoM, and names)
result_list_v = []
result_list_c = []
result_list_n = []

# Main loop
for file in filelist:
    # Get body name from file name
    name = str(file.split('.')[0])

    # Add name to list of names
    result_list_n.append(name)

    # Load the mesh file    
    mesh = trimesh.load(file)
    chull = mesh.convex_hull
    vol = chull.volume

    # Append mesh convex hull volume and center of mass info to lists
    result_list_v.append(vol)
    result_list_c.append(chull.center_mass)

# Convert lists to arrays
v_array = np.vstack(result_list_v)
c_array = np.vstack(result_list_c)

# Combine into one big array
mass_results = np.column_stack((result_list_n, v_array, c_array, filelist))

# Whole-specimen dimension estimates
specimen_volume = sum(result_list_v)
segment_v_by_percentage = result_list_v/specimen_volume

X = result_list_c
Y = [segment_v_by_percentage[0], segment_v_by_percentage[1]]

specimen_com = segment_v_by_percentage.dot(c_array)
# old script: specimen_com = sum([X[0]*Y[0], X[1]*Y[1]])
specimen_values = np.insert(specimen_com, 0, specimen_volume)
print(specimen_values)

# Save the big array as a table
np.savetxt('output/Segment_properties.txt', mass_results, delimiter=' ',fmt="%s")
np.savetxt('output/Specimen_properties.txt', specimen_values, delimiter=' ',fmt="%s")
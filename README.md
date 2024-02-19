# MCH_MassCoM
Brief Description: This script estimates mass and center of mass (CoM) for digitized specimens organized into multiple 3D mesh files



This Python script takes body segments that have already been separated onto individual surface mesh filse, wraps each in its own convex hull, and computes the mass and center of mass for each segment as well as for the whole body.

Requirements:
-Python (implemented here with Spyder)
-Mesh processing library: "trimesh" (see https://github.com/mikedh/trimesh)

Step 1: Place all surface mesh files into the same folder (.obj and .ply both work as file types), and create a folder inside this one called "output".
Step 2: Adjust the file directory path name in this script to the top-level folder (mesh files and "output" should be located inside).
Step 3: Run the script.

The output for whole-specimen dimensions is stored in the "output" folder with the name "Specimen_properties.txt", and the dimensions for each individual segment are stored in "Segment_properties.txt".

The script was adapted from a pipeline originally created by Dr. Rob Brocklehurst.

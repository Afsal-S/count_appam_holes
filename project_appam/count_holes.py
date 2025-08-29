# Import necessary libraries for project_appam
import cv2
import numpy as np
import os

# Folder containing appam images for project_appam
image_folder = 'appam_pictures'

# File to save results for project_appam
results_file = 'results/hole_count.csv'

# Write header to results file if it doesn't exist
if not os.path.exists(results_file):
    with open(results_file, 'w') as f:
        f.write('Image_Name,Estimated_Holes\n')

# Process each image in the project_appam folder
for filename in os.listdir(image_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image_path = os.path.join(image_folder, filename)

        # Read image in grayscale
        img = cv2.imread(image_path, 0)

        # Apply threshold to highlight holes
        _, threshold_img = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)

        # Find contours (holes) in the image
        contours, _ = cv2.findContours(threshold_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Count the number of holes
        hole_count = len(contours)

        print(f'Found {hole_count} holes in {filename}!')

        # Save results to CSV
        with open(results_file, 'a') as f:
            f.write(f'{filename},{hole_count}\n')

print("\nAll done! Check your results in the 'project_appam_results/hole_counts.csv' file!")
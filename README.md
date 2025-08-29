count-appam-holes/

│── appam_pictures/            # Folder containing input Appam images
│── results/                   # Folder to store output CSV file
│── count_holes.py             # Main script to process images
│── results/hole_count.csv     # Generated file with hole counts
│── README.md                  # Project description

How It Works
1. The script loads each Appam image from the `appam_pictures` folder.
2. Converts it to grayscale and applies thresholding.
3. Detects contours (holes/bubbles) using **OpenCV**.
4. Counts the holes and stores the results in `results/hole_count.csv`.

Why This Project?

This is a short project done for fun to combine:

Food culture 

Computer Vision 

Python Programming 

It can be extended to:

Analyze fermentation quality

Compare Appam textures

Build a food pattern recognition dataset

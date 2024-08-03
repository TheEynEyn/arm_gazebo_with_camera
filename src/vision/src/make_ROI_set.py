#!/usr/bin/env python
import cv2
import os

# Define the image path using os library
image_path = os.path.join('/home', 'hussein','ControlArm','src', 'vision','src', 'image.png')

# Load the image
image = cv2.imread(image_path)

# Check if the image is loaded successfully
if image is None:
    print(f"Error: Could not load the image from the path {image_path}.")
    exit()

# Create a directory to save the cropped images
save_dir = os.path.join('/home', 'hussein','ControlArm','src', 'vision','src', 'cropped_images')
os.makedirs(save_dir, exist_ok=True)

# Initialize the counter for the cropped images
counter = 1

while True:
    # Select ROI
    roi = cv2.selectROI("Select ROI", image, fromCenter=False, showCrosshair=True)
    cv2.destroyWindow("Select ROI")

    # Check if ROI has been selected (width and height are not zero)
    if roi[2] == 0 or roi[3] == 0:
        print("No ROI selected. Exiting loop.")
        break

    # Extract the template from the selected ROI
    x, y, w, h = roi
    cropped_image = image[y:y+h, x:x+w]

    # Save the cropped image with a unique name
    cropped_image_path = os.path.join(save_dir, f'cropped_image_{counter}.png')
    cv2.imwrite(cropped_image_path, cropped_image)
    print(f"Saved {cropped_image_path}")

    # Increment the counter
    counter += 1

    # Optionally, display the cropped image
    cv2.imshow("Cropped Image", cropped_image)
    cv2.waitKey(500)  # Display for 500ms
    cv2.destroyAllWindows()

print("ROI selection and saving complete.")

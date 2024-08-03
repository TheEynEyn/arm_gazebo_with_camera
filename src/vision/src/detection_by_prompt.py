#!/usr/bin/env python
import cv2
import os
import threading

class_name = None
change_class = False
exit_program = False

def get_user_input():
    global class_name, change_class, exit_program
    while True:
        if class_name is None:
            class_name = input("Enter the class name to detect (e.g., ball, rubik): ").strip().lower()
        else:
            user_input = input(f"Current class is '{class_name}'. Do you want to change it? (y/n/exit): ").strip().lower()
            if user_input == 'y':
                class_name = input("Enter the new class name to detect (e.g., ball, rubik): ").strip().lower()
                change_class = True
            elif user_input == 'exit':
                exit_program = True
                break

def determine_center_segment(image_shape, center):
    w, h = image_shape
    segment_width = w / 4
    
    x, y = center
    
    if 0 <= x < segment_width:
        return 1
    elif segment_width <= x < 2 * segment_width:
        return 2
    elif 2 * segment_width <= x < 3 * segment_width:
        return 3
    elif 3 * segment_width <= x < 4 * segment_width:
        return 4

def template_matching(image, cropped_image_dir, class_name, threshold=0.8):
    h_img, w_img, channels = image.shape

    image_files = [f for f in os.listdir(cropped_image_dir) if os.path.isfile(os.path.join(cropped_image_dir, f))]
    class_images = [f for f in image_files if class_name in f.lower()]

    detected_centers = []

    for template_file in class_images:
        template_path = os.path.join(cropped_image_dir, template_file)
        template = cv2.imread(template_path)
        if template is None:
            print(f"Error: Could not load the template image from the path {template_path}.")
            continue

        result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        if max_val >= threshold:
            top_left = max_loc
            h, w = template.shape[:2]
            bottom_right = (top_left[0] + w, top_left[1] + h)
            center = (top_left[0] + w // 2, top_left[1] + h // 2)

            cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
            cv2.putText(image, class_name, (top_left[0], top_left[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            cv2.circle(image, center, 7, (0, 0, 255), -1)

            detected_centers.append(center)
            #print(f"Detected center for {template_file}: {center}")

    return detected_centers, w_img, h_img

if __name__ == "__main__":
    image_path = os.path.join('/home', 'hussein','ControlArm','src', 'vision','src', 'image.png')
    cropped_image_dir = os.path.join('/home', 'hussein','ControlArm','src', 'vision','src', 'cropped_images')
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not load the image from the path {image_path}.")
    else:
        input_thread = threading.Thread(target=get_user_input)
        input_thread.daemon = True
        input_thread.start()
        
        last_class_name = None
        display_image = image.copy()  # Initialize display_image

        while True:
            if exit_program:
                break

            if change_class or (last_class_name != class_name and class_name != ""):
                if class_name:  # Check if class_name is not empty
                    display_image = image.copy()
                    centers, w, h = template_matching(display_image, cropped_image_dir, class_name)
                    last_class_name = class_name
                    change_class = False

                    if centers:
                        for center in centers:
                            center_segment_number = determine_center_segment((w, h), center)
                            #print(f"Center segment number: {center_segment_number}")
                    else:
                        print("No centers detected.")
            
            cv2.imshow("Image", display_image)
            key = cv2.waitKey(1) & 0xFF  # Wait for a key press (1 ms delay)
            if key == ord('q'):  # Press 'q' to exit the loop
                break

        cv2.destroyAllWindows()

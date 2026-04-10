import sys
import cv2
import numpy as np
import time

# Load images
images = []
for i in range(8):
    img = cv2.imread(f'captured_image{i}.jpg')
    if img is None:
        print(f"Error: captured_image{i}.jpg could not be loaded. Check the file path.")
    else:
        images.append(img)

# Proceed only if all images are loaded correctly
if len(images) == 8:
    # Ensure all images have the same number of channels
    for i in range(1, len(images)):
        if images[i].shape[2] != images[0].shape[2]:
            if images[i].shape[2] > images[0].shape[2]:
                images[i] = images[i][:, :, :3]  # Keep only the first 3 channels
            else:
                images[0] = images[0][:, :, :3]  # Keep only the first 3 channels

    # Create a blank image with the size to fit all images horizontally
    height = max(img.shape[0] for img in images)
    width = sum(img.shape[1] for img in images)
    output_img = np.zeros((height, width, 3), dtype='uint8')

    # Place each image in the output image
    current_x = 0
    for img in images:
        output_img[:img.shape[0], current_x:current_x + img.shape[1], :] = img
        current_x += img.shape[1]

    cv2.imshow('Combined Image', output_img)
    cv2.imwrite('longimage.jpg',output_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Not all images could be loaded. Please check the file paths.")
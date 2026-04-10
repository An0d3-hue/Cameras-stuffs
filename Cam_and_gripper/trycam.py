import sys
import cv2
import numpy as np
import time

# Load images
img1 = cv2.imread('captured_image{}.jpg'.format(0))
img2 = cv2.imread('captured_image{}.jpg'.format(1))

# Check if images are loaded correctly
if img1 is None:
    print("Error: img1 could not be loaded. Check the file path.")
if img2 is None:
    print("Error: img2 could not be loaded. Check the file path.")

# Proceed only if both images are loaded correctly
if img1 is not None and img2 is not None:
    print(f"Shape of img1: {img1.shape}")
    print(f"Shape of img2: {img2.shape}")

    # Ensure both images have the same number of channels
    if img1.shape[2] != img2.shape[2]:
        if img1.shape[2] > img2.shape[2]:
            img1 = img1[:, :, :3]  # Keep only the first 3 channels
        else:
            img2 = img2[:, :, :3]  # Keep only the first 3 channels

    # Now you can proceed with your operations
    output_img = np.zeros((max(img1.shape[0], img2.shape[0]), img1.shape[1] + img2.shape[1], 3), dtype='uint8')
    output_img[:img1.shape[0], :img1.shape[1], :] = img1
    output_img[:img2.shape[0], img1.shape[1]:img1.shape[1] + img2.shape[1], :] = img2

    cv2.imshow('Combined Image', output_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
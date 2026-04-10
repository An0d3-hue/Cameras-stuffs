import sys
import cv2
import numpy as np
import time

# opencv read images from camera
# and display
# open camera
# Load our images

img1 = cv2.imread('captured_image{}.jpg'.format(0))
img2 = cv2.imread('captured_image{}.jpg'.format(1))

# Check if images are loaded correctly
if img1 is None:
    print("Error: img1 could not be loaded. Check the file path.")
if img2 is None:
    print("Error: img2 could not be loaded. Check the file path.")

if img1 is not None and img2 is not None:
    print(f"Shape of img1: {img1.shape}")
    print(f"Shape of img2: {img2.shape}")

    # Ensure both images have the same number of channels
    if img1.shape[2] != img2.shape[2]:
        if img1.shape[2] > img2.shape[2]:
            img1 = img1[:, :, :3]  # Keep only the first 3 channels
        else:
            img2 = img2[:, :, :3]  # Keep only the first 3 channels

img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

cv2.imshow('img1_gray',img1_gray)
cv2.imshow('img2_gray',img2_gray)

# Create our ORB detector and detect keypoints and descriptors
orb = cv2.ORB_create(nfeatures=2000)

# Find the key points and descriptors with ORB
keypoints1, descriptors1 = orb.detectAndCompute(img1, None)
keypoints2, descriptors2 = orb.detectAndCompute(img2, None)
# draw keypoints
output_image1 = cv2.drawKeypoints(img1, keypoints1, None, color=(255, 0, 255), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('Keypoints1', output_image1)
output_image2 = cv2.drawKeypoints(img2, keypoints2, None, color=(255, 0, 255), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('Keypoints2', output_image2)

# Create a BFMatcher object.
# It will find all of the matching keypoints on two images
bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
matches = bf.match(descriptors1, descriptors2)
print(f"Total matches found: {len(matches)}")

# Filter matches
all_matches = []
for match in matches:
    print(match.distance)  # Print distance of each match
    if match.distance < 300:  # Replace with your desired threshold
        all_matches.append(match)

# Check filtered matches
print(f"Filtered matches: {len(all_matches)}")

matches_sorted = sorted(all_matches, key=lambda x: x.distance)

print(keypoints1[0].pt)
print(keypoints1[0].size)
print("Descriptor of the first keypoint: ")
print(descriptors1[0])

# Check if matches_sorted is not empty and contains match objects
if matches_sorted and hasattr(matches_sorted[0], 'distance'):
    print(matches_sorted[0].distance)
else:
    print("No valid matches found or matches_sorted contains tuples")

def draw_matches(img1, keypoints1, img2, keypoints2, matches):
    r, c = img1.shape[:2]
    r1, c1 = img2.shape[:2]

    # Create a blank image with the size of the first image + second image
    output_img = np.zeros((max([r, r1]), c + c1, 3), dtype='uint8')
    output_img[:r, :c, :] = np.dstack([img1, img1, img1])
    output_img[:r1, c:c + c1, :] = np.dstack([img2, img2, img2])

    # Go over all of the matching points and extract them
    for match in matches:
        img1_idx = match.queryIdx
        img2_idx = match.trainIdx
        (x1, y1) = keypoints1[img1_idx].pt
        (x2, y2) = keypoints2[img2_idx].pt

        # Draw circles on the keypoints
        cv2.circle(output_img, (int(x1), int(y1)), 4, (0, 255, 255), 1)
        cv2.circle(output_img, (int(x2) + c, int(y2)), 4, (0, 255, 255), 1)

        # Connect the same keypoints
        cv2.line(output_img, (int(x1), int(y1)), (int(x2) + c, int(y2)), (0, 255, 255), 1)

    return output_img

# Example usage of draw_matches function
output_img = draw_matches(img1, keypoints1, img2, keypoints2, matches_sorted)
cv2.imshow('Matches', output_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

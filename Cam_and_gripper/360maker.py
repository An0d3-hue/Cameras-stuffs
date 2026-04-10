import cv2
import numpy as np
from exif import Image

video_path = 'output.mp4'
video = cv2.VideoCapture(video_path)
success, image = video.read()
count = 0

while success:
    cv2.imwrite(f"frame{count}.jpg", image)
    success, image = video.read()
    count += 1

# Load images
images = [cv2.imread(f"frame{i}.jpg") for i in range(count)]

# Create a stitcher object
stitcher = cv2.Stitcher_create()
status, pano = stitcher.stitch(images)

if status == cv2.Stitcher_OK:
    cv2.imwrite('panorama.jpg', pano)
else:
    print("Error during stitching")

with open('panorama.jpg', 'rb') as image_file:
    my_image = Image(image_file)

my_image.make = "Python"
my_image.model = "360 Photosphere"

with open('panorama_360.jpg', 'wb') as new_image_file:
    new_image_file.write(my_image.get_file())

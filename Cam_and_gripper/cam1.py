# program to capture single image from webcam in python
# importing OpenCV library
import cv2
import argparse
# initialize the camera
# If you have multiple camera connected with
# current device, assign a value in cam_port
# variable according to that
cam_port = 1
cam = cv2.VideoCapture(cam_port)

# reading the input using the camera
result, image = cam.read()
# If image will detect without any error,
# show result
if result:

    # showing result, it takes frame name and image
    # output
    #cv2.rectangle(image, (108, 100), (535, 390), [0, 255, 0], 1)
    cv2.imshow("img1", image)
    # saving image in local storage
    cv2.imwrite("img1.jpg", image)

    img = cv2.imread('img1.jpg')
    print(img.shape)  # Print image shape

    # Cropping an image
    cropped_image = img[100:390, 108:535]

    # Display cropped image
    cv2.imshow("cropped", cropped_image)

    # Save the cropped image
    cv2.imwrite("Cropped Image.jpg", cropped_image)
    # If keyboard interrupt occurs, destroy image window
    while True:
        if cv2.waitKey(1) & 0xFF == ord('a'):
            break

    cv2.destroyAllWindows()

# If captured image is corrupted, moving to else part
else:
    print("No image detected. Please! try again")
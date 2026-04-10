import cv2

value = 0
# Open the default camera
cap = cv2.VideoCapture(1)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('Frame', frame)

    # Wait for 'c' key to capture the image or 'q' to quit
    key = cv2.waitKey(1) & 0xFF
    if key == ord('c'):
        # Save the captured image
        cv2.imwrite('captured_image{}.jpg'.format(value), frame)

        img = cv2.imread('captured_image{}.jpg'.format(value))
        print(img.shape)  # Print image shape

        # Cropping an image
        cropped_image = img[100:390, 108:535]

        # Display cropped image
        #cv2.imshow("cropped", cropped_image)

        # Save the cropped image
        cv2.imwrite('captured_image{}.jpg'.format(value), cropped_image)

        # change to next photo and confirm save
        value = value + 1
        print("Image captured and saved!")
    elif key == ord('q'):
        break

# Release the capture and destroy all windows
cap.release()
cv2.destroyAllWindows()
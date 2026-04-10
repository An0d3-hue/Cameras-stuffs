import cv2

# Open the default cameras
cam1 = cv2.VideoCapture(0)
cam2 = cv2.VideoCapture(1)

# Get the default frame width and height for both cameras
frame_width1 = int(cam1.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height1 = int(cam1.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_width2 = int(cam2.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height2 = int(cam2.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create VideoWriter objects for both cameras
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out1 = cv2.VideoWriter('output1.mp4', fourcc, 20.0, (frame_width1, frame_height1))
out2 = cv2.VideoWriter('output2.mp4', fourcc, 20.0, (frame_width2, frame_height2))

while True:
    ret1, frame1 = cam1.read()
    ret2, frame2 = cam2.read()

    if ret1 and ret2:
        # Write the frames to the output files
        out1.write(frame1)
        out2.write(frame2)

        # Display the captured frames
        cv2.imshow('Camera 1', frame1)
        cv2.imshow('Camera 2', frame2)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) == ord('q'):
        break

# Release the capture and writer objects
cam1.release()
cam2.release()
out1.release()
out2.release()
cv2.destroyAllWindows()
#########################################################
# Script created by T.Slenter for testing purpose only. #
# Cartoon generator with images or webcam.              #
#########################################################

#The cv2 module can be installed with: pip3 install opencv-python

#Import modules
import cv2

#Use a image to transform
def picture_to_cartoon(image, save_image):
    image = cv2.imread(image)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    #color = cv2.bilateralFilter(image, 9, 250, 250)
    color = cv2.bilateralFilter(image, 7, 250, 250)

    cartoon = cv2.bitwise_and(image, color, mask=edges)

    # For debugging
    # cv2.imshow("Images", image)
    # cv2.imshow("edges", edges)
    cv2.imshow("Cartoon", cartoon)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    answer = input("Do you want to save this image? y/n: ")
    if answer == 'y':
        cv2.imwrite(save_image, cartoon)

#Use the webcam to create a live filter
def live_cartoon(capture_device):
    print("Press 'q' to quit!")
    cv2.namedWindow("Webcam", cv2.WINDOW_NORMAL)

    cap = cv2.VideoCapture(capture_device)

    while True:
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.medianBlur(gray, 5)
        edges = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

        #color = cv2.bilateralFilter(frame, 9, 250, 250)
        color = cv2.bilateralFilter(frame, 7, 250, 250)

        cartoon = cv2.bitwise_and(frame, color, mask=edges)

        cv2.imshow("Webcam", cartoon)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close the window
    cap.release()
    cv2.destroyAllWindows()

#Snapshot using the webcam
def snap_cartoon(capture_device, save_image):
    cv2.namedWindow("Snap", cv2.WINDOW_NORMAL)

    cap = cv2.VideoCapture(capture_device)
    sec = 0

    # Some webcams need to have a second to capture. So we skip the first 2 frames.
    while sec != 2:
        ret, frame = cap.read()
        sec += 1

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    #color = cv2.bilateralFilter(frame, 9, 250, 250)
    color = cv2.bilateralFilter(frame, 7, 250, 250)

    cartoon = cv2.bitwise_and(frame, color, mask=edges)
    cv2.imshow("Snap", cartoon)

    # Release the webcam and close the window
    cap.release()
    cv2.waitKey(0)

    answer = input("Do you want to save this image? y/n: ")
    if answer == 'y':
        cv2.imwrite(save_image, cartoon)

#Example run function:

#Use function(image_filename, filename_for saving)
#picture_to_cartoon("100_1904.jpg", "converted2.jpg")

#Use function(capture device) / usually 0 or 1
#live_cartoon(1)

#Use function(capture device, image_name_to save) / capture device is usually 0 or 1
#snap_cartoon(0, "my_new_snap2.jpg")
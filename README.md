# opencv-cartoon-generator
An OpenCV cartoon generator using images or a webcam

# How to run:
Within the script you can find 3 functions. Uncomment the one which you like to try, and run the script: capture_functions.py

# Example run function:
#Use function(image_filename, filename_for saving)

picture_to_cartoon("100_1904.jpg", "converted2.jpg")

#Use function(capture device) / usually 0 or 1

live_cartoon(1)

#Use function(capture device, image_name_to save) / capture device is usually 0 or 1

snap_cartoon(0, "my_new_snap2.jpg")

## 1. opencv-cartoon-generator
An OpenCV cartoon generator using images or a webcam

## 2. How to run
Within the script you can find 3 functions. Uncomment the one which you like to try, and run the script: capture_functions.py

## 3. Example run function
#Use function(image_filename, filename_for saving)

picture_to_cartoon("100_1904.jpg", "converted2.jpg")

#Use function(capture device) / usually 0 or 1

live_cartoon(1)

#Use function(capture device, image_name_to save) / capture device is usually 0 or 1

snap_cartoon(0, "my_new_snap2.jpg")

## 4. Example output
![alt text](https://github.com/tslenter/opencv-cartoon-generator/blob/main/example.jpg?raw=true)

## 5. License

"opencv-cartoon-generator" is a free application that can be used to make livestream or image cartoon like.

Copyright (C) 2023 Tom Slenter

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

For more information contact the author:

Name author: Tom Slenter

E-mail: info@remotesyslog.com

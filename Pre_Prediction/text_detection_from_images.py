# Import required packages
import cv2
import pytesseract
import os
import pandas as pd

# Mention the installed location of Tesseract-OCR in your system
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

im_path = './Image Files/'
im_files = os.listdir(im_path)


# creating a dataframe
df = pd.DataFrame()

# Read image from which text needs to be extracted
img = cv2.imread(im_path+im_files[0])

# Preprocessing the image starts

# Convert the image to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Performing OTSU threshold
ret, thresh1 = cv2.threshold(
    gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

# Specify structure shape and kernel size.
# Kernel size increases or decreases the area
# of the rectangle to be detected.
# A smaller value like (10, 10) will detect
# each word instead of a sentence.
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (6, 6))

# Applying dilation on the threshold image
dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)

# Finding contours
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_NONE)

# Creating a copy of image
im2 = img.copy()

# A text file is created and flushed
file = open("recognized.txt", "w+")
file.write("")
file.close()

xmin = []
xmax = []
ymin = []
ymax = []
Text = []

# Looping through the identified contours
# Then rectangular part is cropped and passed on
# to pytesseract for extracting text from it
# Extracted text is then written into the text file


print("Xmin     Xmax     Ymin     yMax     Text")
i = 0
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    xm = x + w
    ym = y + h

    xmin.append(x)
    xmax.append(xm)
    ymin.append(y)
    ymax.append(ym)

    # Drawing a rectangle on copied image
    rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Cropping the text block for giving input to OCR
    cropped = im2[y:y + h, x:x + w]

    # Open the file in append mode
    # file = open("recognized.txt", "a")

    # Apply OCR on the cropped image
    text = pytesseract.image_to_string(cropped)
    text = text.strip()
    Text.append(text)
    # print(xmin[i], "    ", xmax[i], "    ", ymin[i],
    #       "    ", ymax[i], "    ", text, "     ")

    # Appending the text into file
    # file.write(text)
    # file.write("\n")
    i += 1
    # Close the file
    # file.close


df['xmin'] = xmin
df['xmax'] = xmax
df['ymin'] = ymin
df['ymax'] = ymax
df['Object'] = Text


print(df)

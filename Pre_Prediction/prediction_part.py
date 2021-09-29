from pdf2image import convert_from_path
import os

f_path = "./Test Invoices/"
files = os.listdir(f_path)
# print(files)
im_path = "./Image Files/"


def fileProcessing(f):
    file_name = f
    if(file_name.endswith('.pdf')):
        print("PDF File Found")
        pages = convert_from_path(file_name)

        for i in range(len(pages)):
            pages[i].save(im_path+(file_name.split('/')[-1]).split('.')
                          [0]+' page' + str(i) + '.jpg', 'JPEG')
    else:
        print("Image File Found")


fileProcessing(f_path+files[0])

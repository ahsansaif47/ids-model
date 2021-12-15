import os
from pdf2image import convert_from_path
from PIL import Image
import keras_ocr
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd
import numpy as np
from Mat_Package import Grapher
import networkx as nx

test_invoices = "./Test Invoices Folder/PDF Invoices/"
im_path = "./Invoice Images/"
pipeline = keras_ocr.pipeline.Pipeline()
im_files_list = os.listdir(im_path)

files = os.listdir(test_invoices)


def pdf_toImage(file_name):
    # print("File processed is: ", file_name)
    if(file_name.endswith('.pdf')):
        # print("PDF File Found..")
        pages = convert_from_path(file_name)

        for i in range(len(pages)):
            pages[i].save(im_path+(file_name.split('/')[-1]).split('.')
                          [0]+' page' + str(i) + '.png', 'PNG')
            # converting to grey-scale
            img = Image.open(im_path + file_name.split('/')
                             [-1].split('.')[0]+' page' + str(i) + '.png').convert('LA')
            img.save(im_path + file_name.split('/')
                     [-1].split('.')[0]+' page' + str(i) + '.png')
            img = img.resize((1700, 1800), Image.ANTIALIAS)
            img.save(im_path + file_name.split('/')
                     [-1].split('.')[0]+' page' + str(i) + '.png')
    else:
        print("Image File Found..")


def batchData_Tuple(ImagePath):
    f_names = []
    custom_images = []
    for filename in os.listdir(ImagePath):
        f_names.append(filename)
        custom_images.append(os.path.join(ImagePath, filename))

    images = [keras_ocr.tools.read(path) for path in custom_images]
    t_images = len(images)
    print("Total Images are: ", t_images)
    image_batches = []
    batch_start = 0
    batch_end = 1
    if(t_images > 1):
        while(batch_start < t_images):
            batch = []
            batch = images[batch_start:batch_end]
            batch_start = batch_end
            batch_end = batch_start + 1
            image_batches.append(batch)
        batch = images[batch_start:]
    else:
        image_batches.append(images[0])
    print(image_batches)
    return f_names, image_batches


def tuples_toCSV(b_prediction):
    Object = []
    xmin = []
    xmax = []
    ymin = []
    ymax = []
    dataframes = []

    for i in range(len(b_prediction)):
        df = pd.DataFrame()
        SmallList_OBJECT = []
        SmallList_XMIN = []
        SmallList_XMAX = []
        SmallList_YMIN = []
        SmallList_YMAX = []
        FILE = b_prediction[i]
        for j in range(len(FILE)):
            SmallList_OBJECT.append(b_prediction[i][j][0])
            SmallList_XMIN.append(b_prediction[i][j][1][1][0])
            SmallList_YMIN.append(b_prediction[i][j][1][1][1])
            SmallList_XMAX.append(b_prediction[i][j][1][2][0])
            SmallList_YMAX.append(b_prediction[i][j][1][2][1])

        Object.append(SmallList_OBJECT)
        xmin.append(SmallList_XMIN)
        xmax.append(SmallList_XMAX)
        ymin.append(SmallList_YMIN)
        ymax.append(SmallList_YMAX)

        df['xmin'] = SmallList_XMIN
        df['xmax'] = SmallList_XMAX
        df['ymin'] = SmallList_YMIN
        df['ymax'] = SmallList_YMAX
        df['Object'] = SmallList_OBJECT
        dataframes.append(df)

    return dataframes


def batch_toDataframe(batches_array):
    dataframes = []
    for i in range(len(batches_array)):
        im_batch = batches_array[i]
        prediction = pipeline.recognize(im_batch)
        df_batch = tuples_toCSV(prediction)
        dataframes.append(df_batch)

    return dataframes


def df_AdjMatrix(df_array):
    matrices = []
    # for i in range(len(df_array)):
    G = Grapher.makeGraph(df_array[0])
    M = nx.to_numpy_array(G, dtype=np.int32)
    matrices.append(M)

    return matrices


pdf_toImage(test_invoices+files[0])

img = mpimg.imread(im_path + im_files_list[0])
# imgplot = plt.imshow(img)
# plt.show()

file_names = batchData_Tuple(im_path)[0]
image_batches = batchData_Tuple(im_path)[1]

print("File names are: ", file_names)
t_batches = len(image_batches)
print("Total batches are: ", t_batches)

df_batches = batch_toDataframe(image_batches)
print(df_batches[0][1])

matrices = df_AdjMatrix(df_batches)
print("Total matrices are: ", len(matrices))

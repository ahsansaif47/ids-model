import pandas as pd
import os

csv_folder = "./Test Invoices Folder/CSVs/"
csvs = os.listdir(csv_folder)

for i in csvs:
    df = pd.read_csv(csv_folder + i)
    xmin = df['xmin']
    ymin = df['ymin']
    xmax = df['xmax']
    ymax = df['xmax']

    for j in range(len(xmin)):
        xmin[j] = round(xmin[j])
        ymin[j] = round(ymin[j])
        xmax[j] = round(xmax[j])
        ymax[j] = round(ymax[j])

    df['xmin'] = xmin
    df['ymin'] = ymin
    df['xmax'] = xmax
    df['ymax'] = ymax

    df.to_csv(csv_folder + i, index=False)

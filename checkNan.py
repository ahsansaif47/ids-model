import pandas as pd
import os

dataset = "./Dataset (Labelled Images)/"

label_files = dataset + "label/"

files = os.listdir(label_files)

for i in range(len(files)):
    df = pd.read_csv(label_files+files[0])
    print(df['Object'].isnull().sum())

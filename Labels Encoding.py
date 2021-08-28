import pandas as pd
from sklearn.preprocessing import LabelEncoder
import os

f_path = "./Dataset (Labelled Images)/label"
files = os.listdir(f_path)
LE = LabelEncoder()

for i in files:
    df = pd.read_csv(f_path+"/"+i)
    df['Encodings'] = LE.fit_transform(df.labels.values)
    df.to_csv(f_path+"/"+i)


def getLabels():
    labels = []
    for i in files:
        df = pd.read_csv(f_path+"/"+i)
        array = df['Encodings']
        maxVal = max(array)
        labels.append(maxVal)

    nLabels = max(labels)
    nArray = []
    for i in range(nLabels):
        nArray.append(i)

    print(nArray)
    # return nLabels


getLabels()
# testing commit

print("Labels Encoding Done")

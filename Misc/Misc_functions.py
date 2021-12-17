import pandas as pd


def returnText(df):
    Text = []
    seenList = []
    text = df['Object'].to_list()

    for i in range(len(text)):
        if(text[i] not in seenList):
            Text.append(text[i])
        seenList.append(text[i])

    return Text


def returnL_T(direc, files):
    train_text = []
    labels = []
    for f in range(len(files)):
        seenList = []
        df = pd.read_csv(direc + files[f], encoding='unicode_escape')
        text = df['Object'].to_list()
        T_labels = df['labels'].to_list()

        for i in range(len(text)):
            if(text[i] not in seenList):
                labels.append(T_labels[i])
                train_text.append(text[i])
            seenList.append(text[i])

    return labels, train_text

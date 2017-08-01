import pandas as pd 
from sklearn.cross_validation import train_test_split

def train_test():
    df = pd.read_csv("data_preprocessed.csv",header=None)

    label_cols = df.columns[0:2]
    Y = df[label_cols]

    feature_cols = df.columns[2:len(df.columns)]
    X = df[feature_cols]

    X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state=1)
    train_df = pd.concat([y_train,X_train],axis=1)
    test_df = pd.concat([y_test,X_test], axis=1)

    return train_df, test_df

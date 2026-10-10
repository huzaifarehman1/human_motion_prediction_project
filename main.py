

lable_train = "/home/huzaifa/Code/AI_ML/DL/human_motion_prediction_project/UCI HAR Dataset/UCI HAR Dataset/train/y_train.csv"
lable_test = "/home/huzaifa/Code/AI_ML/DL/human_motion_prediction_project/UCI HAR Dataset/UCI HAR Dataset/test/y_test.csv"



import pandas as pd
import numpy as np
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
import glob
import os


def make_data(path):
    directory = path

    files = sorted(glob.glob(os.path.join(directory, "*.txt")))

    # Load each file: (Num_Samples, 128)
    data = [np.loadtxt(file) for file in files]

    # Stack along the last axis: (Num_Samples, 128, 9)
    X_train = np.stack(data, axis=-1)

    print("X_train shape:", X_train.shape)
    return X_train



X_train = make_data("/home/huzaifa/Code/AI_ML/DL/human_motion_prediction_project/UCI HAR Dataset/UCI HAR Dataset/train/Inertial Signals")
X_test = make_data("/home/huzaifa/Code/AI_ML/DL/human_motion_prediction_project/UCI HAR Dataset/UCI HAR Dataset/test/Inertial Signals")
Y_train = pd.read_csv(lable_train)
Y_test = pd.read_csv(lable_test)

def preprocess(data,Y):
    data = data.reshape(-1,128*9)
    Y -= 1
    return data,Y

def postprocess(data,Y):
    Y += 1
    return data,Y

X_train,Y_train = preprocess(X_train,Y_train)


X_train,X_val,Y_train,Y_val = train_test_split(X_train,Y_train,test_size=0.35)

print(X_train.shape)

#print(np.unique_counts(Y))



model = XGBClassifier(
    max_depth=3,
    tree_method="hist",
    n_estimators=250,
    early_stopping_rounds=5,
    random_state=42,learning_rate = 1,
)
model.fit(X_train,Y_train,
    eval_set=[(X_train, Y_train), (X_val, Y_val)],
    verbose=3)
pred = model.predict(X_val)
from sklearn.metrics import accuracy_score
print(accuracy_score(Y_val,pred))

X_test,Y_test = preprocess(X_test,Y_test)
pred = model.predict(X_test)
print(accuracy_score(Y_test,pred))








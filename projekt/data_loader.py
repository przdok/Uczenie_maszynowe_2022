import os
from random import sample
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from PIL import Image
from sklearn.utils import shuffle
import tensorflow as tf
from imblearn.under_sampling import RandomUnderSampler
import imblearn

def load_and_preprocess_data(data_dir):
    labels = pd.read_csv(os.path.join(data_dir, 'HAM10000_metadata.csv'))
    labels = labels.sort_values(by='image_id')
    X = []
    y = []
    image_names = os.listdir(os.path.join(data_dir, 'images'))
    for image_name in image_names:
        try:
            image = Image.open(os.path.join(data_dir, 'images', image_name))
            print(image_name)
            image_label = labels[labels['image_id'] + '.jpg'  == image_name]['dx'].values[0]
            print('image labels: \n{0}'.format(image_label))
            
            image = image.resize((150, 150))
            
            image = np.array(image) / 255.0
            X.append(np.array(image))
            y.append(image_label)
        except:
            pass 

    X = np.array(X)
    y = np.array(y) 
    
    if len(X) != len(y):
        print("Some images are missing or corrupted")
    
    for i in range(len(X)):
        if X[i].shape[:2] != (150, 150):
            print(f"Image {i} has invalid shape {X[i].shape[:2]}")
    print(X.shape, y.shape)

    unique_classes, class_counts = np.unique(y, return_counts=True)
    print("Unique classes and their count in y:", (unique_classes, class_counts))
    print(X.shape, y.shape)
  
    undersampler = RandomUnderSampler(sampling_strategy='auto')
    X, y = undersampler.fit_resample(X.reshape(X.shape[0], -1), y)

    unique_classes, class_counts = np.unique(y, return_counts=True)
    print("Unique classes and their count in y 2:", (unique_classes, class_counts))

    print("Shape of X:", X.shape)
    print("Shape of y:", y.shape)
    X, y = shuffle(X, y)
    le = LabelEncoder()
    y = le.fit_transform(y)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify = y)
    print("Class distribution in y_train:", np.unique(y_train, return_counts=True)[1])

    print("Class distribution in y_test:", np.unique(y_test, return_counts=True)[1])

    print((len(X_train), len(X_test), len(y_train), len(y_test)))
    return (X_train, y_train), (X_test, y_test)

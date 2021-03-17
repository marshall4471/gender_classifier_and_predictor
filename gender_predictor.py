# -*- coding: utf-8 -*-
"""gender_predictor.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TWmfAhFBS54-VzU-xU5l99samG-Q6p6e
"""

import zipfile
from google.colab import drive

drive.mount('/content/gdrive/')

zip_ref = zipfile.ZipFile("/content/gdrive/MyDrive/gender_pics.zip", 'r')
zip_ref.extractall("gender_pics.zip")
zip_ref.close()

from keras import models

file1 = ("/content/gender_pics.zip/Training")

file2 = ("/content/gender_pics.zip/Validation")

from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

train_set = train_datagen.flow_from_directory(file1,
                                                 target_size = (64, 64),
                                                 batch_size = 32,
                                                 class_mode = 'binary')

import tensorflow as tf

test_datagen = ImageDataGenerator(rescale = 1./255)

test_set = test_datagen.flow_from_directory(file2,
                                            target_size = (64, 64),
                                            batch_size = 32,
                                            class_mode = 'binary')

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Conv2D(filters=32, kernel_size=3, activation='relu', input_shape=[64, 64, 3]))
model.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))
model.add(tf.keras.layers.Conv2D(filters=32, kernel_size=3, activation='relu'))
model.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(units=128, activation='relu'))
model.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))
model.compile(optimizer = 'adam', loss='binary_crossentropy', metrics=['accuracy'])
model.summary()

history = model.fit(train_set, validation_data =test_set, epochs=30, verbose=2)

model.save("gender_pred2.h5")

import matplotlib.pyplot as plt

from google.colab import files
uploaded = files.upload()

x = plt.imread('adam_sandler.jpg')
plt.imshow(x)


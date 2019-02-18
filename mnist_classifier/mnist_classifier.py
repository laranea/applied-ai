# -*- coding: utf-8 -*-
"""Copy of MNIST Classification, Feedforward NN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1b4KASEuLDo9HS-5mkUJgVq8DIbKMLN-h

## Importing Modules
"""

from keras.datasets import mnist
import matplotlib.pyplot as plt
import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.utils import np_utils

seed = 7
numpy.random.seed(seed)

"""### Bring in Data, check the data"""

(X_train, Y_train), (X_test, Y_test) = mnist.load_data()

plt.imshow(X_train[20000], cmap=plt.get_cmap('gray'))
plt.show()
print(Y_train[20000])

"""## Perform required preprocessing, and make it ready for machine learning algorithim."""

num_of_pixels = X_train.shape[1] * X_train.shape[2]
X_train = X_train.reshape(X_train.shape[0], num_of_pixels).astype('float32')
X_test = X_test.reshape(X_test.shape[0], num_of_pixels).astype('float32')
X_train = X_train / 255
X_test = X_test / 255

Y_train = np_utils.to_categorical(Y_train)
Y_test = np_utils.to_categorical(Y_test)
num_classes = Y_test.shape[1]

"""## Create the network"""

my_model = Sequential()
my_model.add(Dense(10, input_dim=num_of_pixels, activation='relu'))
my_model.add(Dense(num_classes, activation='softmax'))

"""## Configure and compile the network"""

my_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

"""## Train the network"""

my_model.fit(X_train, Y_train, epochs=10, batch_size=100, verbose=2)

"""## Evaluate the performance (test your hypothesis)"""

scores = my_model.evaluate(X_test, Y_test, verbose=0)
print("Error: %.2f%%" % (100-scores[1]*100))
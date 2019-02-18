# -*- coding: utf-8 -*-
"""MNIST_RNN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10iJHaTHiQEDaOqpsdl0DY_zNHjfyXGDs
"""

import keras
from keras.datasets import mnist
from keras import models, Sequential
from keras.layers import Input, Dense, Dropout
from keras.layers import LSTM, SimpleRNN, GRU

# Training parameters.
batch_size = 32
classes = 10
epochs = 10

# Embedding dimensions.
row_hidden = 128
col_hidden = 128

# The data, split between train and test sets.
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape(-1, 28, 28)
x_test = x_test.reshape(-1, 28, 28)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255
print(x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# Converts class vectors to binary class matrices.
y_train = keras.utils.to_categorical(y_train, classes)
y_test = keras.utils.to_categorical(y_test, classes)
model=Sequential()

#RNN Model
model.add(SimpleRNN(128,input_shape=(28,28)))
model.add(Dense(classes, activation='softmax'))
model.compile(loss='categorical_crossentropy',
            optimizer='rmsprop',
            metrics=['accuracy'])

# Training.
model.fit(x_train, y_train,
        batch_size=batch_size,
        epochs=epochs,
        verbose=1,
        validation_data=(x_test, y_test))

# Evaluation.
scores = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', scores[0])
print('Test accuracy:', scores[1])

#LSTM MODEL
epochs=5
model.add(LSTM(125,input_shape=(28,28)))
model.add(Dropout(0.4))
model.add(Dense(classes, activation='softmax'))
model.compile(loss='categorical_crossentropy',
            optimizer='rmsprop',
            metrics=['accuracy'])

# Training.
model.fit(x_train, y_train,
        batch_size=batch_size,
        epochs=epochs,
        verbose=1,
        validation_data=(x_test, y_test))

# Evaluation.
scores = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', scores[0])
print('Test accuracy:', scores[1])

#GRU MODEL
epochs=5
model.add(GRU(128,input_shape=(28,28)))
model.add(Dense(classes, activation='softmax'))
model.compile(loss='categorical_crossentropy',
            optimizer='rmsprop',
            metrics=['accuracy'])

# Training.
model.fit(x_train, y_train,
        batch_size=batch_size,
        epochs=epochs,
        verbose=1,
        validation_data=(x_test, y_test))

# Evaluation.
scores = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', scores[0])
print('Test accuracy:', scores[1])
import numpy as np
import keras
import matplotlib.pyplot as plt
from keras.datasets import mnist
from keras.models import Sequential
from keras.optimizers import SGD
from keras.layers import Dense
from ann_visualizer.visualize import ann_viz

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

x_train /= 255  
x_test /= 255

num_classes = 10

y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

model = Sequential()

model.add(Dense(10, activation='relu', input_shape=(784,)))
# model.add(Dense(10, activation= 'relu'))

model.compile(loss = "msle", optimizer = SGD(lr = 0.1),
metrics=['categorical_accuracy'])

batch_size = 32
epochs = 50

history = model.fit(x_train, y_train,
                batch_size=batch_size,
                epochs=epochs,
                verbose=1,
                validation_data=(x_test, y_test))
score = model.evaluate(x_test, y_test, verbose=0)

# ann_viz(model)
# keras.utils.plot_model(model, to_file='model.png')


print('Test loss:', score[0])
print('Test accuracy:', score[1])

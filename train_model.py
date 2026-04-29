import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np

mnist = keras.datasets.mnist

n_classes = 10
img_shape = (28, 28, 1)

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.astype("float32") / 255
x_test = x_test.astype("float32") / 255
x_train = np.expand_dims(x_train, -1)
x_test = np.expand_dims(x_test, -1)

model = keras.Sequential(
    [
        keras.Input(shape=img_shape),
        layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Flatten(),
        layers.Dense(n_classes, activation="softmax"),
    ]
)

batch_size = 64
epochs = 4

model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1)

model.save('model.h5')

score = model.evaluate(x_test, y_test, verbose=0)
print("Acurácia:", score[1])
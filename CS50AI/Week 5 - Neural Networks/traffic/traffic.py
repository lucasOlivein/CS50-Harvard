import cv2 as cv
import numpy as np
import sys

import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import tensorflow as tf
from tensorflow.keras import Sequential, Input
from tensorflow.keras.layers import Conv2D, Flatten, Dense

from sklearn.model_selection import train_test_split

EPOCHS = 10
IMG_WIDTH = 30
IMG_HEIGHT = 30
NUM_CATEGORIES = 43
TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) not in [2, 3]:
        sys.exit("Usage: python traffic.py data_directory [model.h5]")

    # Get image arrays and labels for all image files
    images, labels = load_data(sys.argv[1])

    # Split data into training and testing sets
    labels = tf.keras.utils.to_categorical(labels)
    x_train, x_test, y_train, y_test = train_test_split(
        np.array(images), np.array(labels), test_size=TEST_SIZE
    )

    # Get a compiled neural network
    model = get_model()

    # Fit model on training data
    model.fit(x_train, y_train, epochs=EPOCHS)

    # Evaluate neural network performance
    model.evaluate(x_test,  y_test, verbose=2)

    # Save model to file
    if len(sys.argv) == 3:
        filename = sys.argv[2]
        model.save(filename)
        print(f"Model saved to {filename}.")


def load_data(data_dir):
    """
    Load image data from directory `data_dir`.

    Assume `data_dir` has one directory named after each category, numbered
    0 through NUM_CATEGORIES - 1. Inside each category directory will be some
    number of image files.

    Return tuple `(images, labels)`. `images` should be a list of all
    of the images in the data directory, where each image is formatted as a
    numpy ndarray with dimensions IMG_WIDTH x IMG_HEIGHT x 3. `labels` should
    be a list of integer labels, representing the categories for each of the
    corresponding `images`.
    """
    # Check if data_dir is a valid directory
    if not os.path.isdir(data_dir):
        sys.exit("Invaled data directory")
    
    images = []
    labels = []

    # Iterate over each directory in data_dir
    for directory in os.listdir(data_dir):
        path = os.path.join(data_dir, directory)

        # Check for valid directories in data_dir
        if os.path.isdir(path):

            # Iterate over each file in a specific directory in data_dir
            for file in os.listdir(path):

                # Reading and resizing the image
                img = cv.resize(src=cv.imread(os.path.join(path, file)),
                                dsize=(IMG_WIDTH, IMG_HEIGHT),
                                fx=0, fy=0, 
                                interpolation=cv.INTER_AREA)
                
                images.append(img)
                labels.append(directory)

    return (images, labels)

def get_model():
    """
    Returns a compiled convolutional neural network model. Assume that the
    `input_shape` of the first layer is `(IMG_WIDTH, IMG_HEIGHT, 3)`.
    The output layer should have `NUM_CATEGORIES` units, one for each category.
    """

    model = Sequential([
        Input(shape=(30, 30, 3)),
        Conv2D(filters=8, kernel_size=3, strides=1, padding="same", use_bias=False),
        Flatten(),
        Dense(NUM_CATEGORIES, activation="softmax")
    ])

    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
        loss="categorical_crossentropy",
        metrics=['accuracy'])
    
    return model




if __name__ == "__main__":
    main()

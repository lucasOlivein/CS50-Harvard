import cv2 as cv
import numpy as np
import sys
import math

import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import tensorflow as tf
from tensorflow.keras import Sequential, Input, Model
from tensorflow.keras.layers import ( Conv2D, DepthwiseConv2D, Flatten, Dense, BatchNormalization, 
                                     ReLU, Add, AveragePooling2D, GlobalAveragePooling2D, MaxPooling2D, 
                                     Concatenate, Reshape, Multiply, Activation, Lambda, Dropout,
                                     LayerNormalization, DepthwiseConv2D)

from sklearn.model_selection import train_test_split

EPOCHS = 50
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

    # DropPath (Stochastic Depth)
    class DropPath(tf.keras.Layer):
        def __init__(self, drop_prob=0.0, **kwargs):
            super().__init__(**kwargs)
            self.drop_prob = float(drop_prob)

        def call(self, x, training=False):
            if (not training) or (self.drop_prob == 0.0):
                return x

            keep_prob = 1.0 - self.drop_prob
            batch = tf.shape(x)[0]
            # broadcast mask shape: (batch, 1, 1, 1) for channels-last
            shape = (batch,) + (1,) * (len(x.shape) - 1)
            random_tensor = keep_prob + tf.random.uniform(shape, dtype=x.dtype)
            binary_mask = tf.floor(random_tensor)

            return (x / keep_prob) * binary_mask
    
    # Layer Scale
    class LayerScale(tf.keras.Layer):
        def __init__(self, dim, init_value=1e-6, **kwargs):
            super().__init__(**kwargs)
            self.dim = int(dim)
            self.init_value = float(init_value)

        def build(self, input_shape):
            self.gamma = self.add_weight(
                name="gamma",
                shape=(self.dim,),
                initializer=tf.keras.initializers.Constant(self.init_value),
                trainable=True,
                dtype=self.dtype,
            )

        def call(self, x):
            return x * self.gamma


    # ConvNeXt block
    class ConvNeXtBlock(tf.keras.Layer):
        def __init__(self, dim, drop_prob=0.0, layer_scale_init=1e-6, **kwargs):
            super().__init__(**kwargs)
            self.dim = int(dim)
            self.drop_prob = float(drop_prob)
            self.layer_scale_init = float(layer_scale_init)

            self.dw = DepthwiseConv2D(kernel_size=7, padding="same")
            self.norm = LayerNormalization(epsilon=1e-6)
            self.pw1 = Conv2D(4 * self.dim, kernel_size=1)
            self.pw2 = Conv2D(self.dim, kernel_size=1)
            self.ls = LayerScale(self.dim, self.layer_scale_init)
            self.dp = DropPath(self.drop_prob)

        def call(self, x, training=False):
            shortcut = x
            x = self.dw(x)
            x = self.norm(x)
            x = self.pw1(x)
            x = tf.nn.gelu(x)
            x = self.pw2(x)
            x = self.ls(x)
            x = self.dp(x, training=training)
            return shortcut + x

    input = Input((IMG_WIDTH, IMG_HEIGHT, 3))

    drop_path_rate = 0.0
    layer_scale_init_value = 1e-6
    
    # Custom values
    depths = (2, 2, 4, 2)
    dims = (35, 70, 140, 280)


    # Stem
    layer = Conv2D(dims[0], kernel_size=4, strides=4, padding="same")(input)
    layer = LayerNormalization(epsilon=1e-6)(layer)

    # DropPath rates lineares
    total_blocks = sum(depths)
    dp_rates = [float(r) for r in tf.linspace(0.0, drop_path_rate, total_blocks).numpy()]
    dp_index = 0

    # Stage 0
    for _ in range(depths[0]):
        layer = ConvNeXtBlock(dims[0], drop_prob=dp_rates[dp_index], layer_scale_init=layer_scale_init_value)(layer)
        dp_index += 1

    # Stages 1, 2, 3
    for stage in range(1, 4):
        layer = Conv2D(dims[stage], kernel_size=2, strides=2, padding="valid")(layer)
        layer = LayerNormalization(epsilon=1e-6)(layer)
        for _ in range(depths[stage]):
            layer = ConvNeXtBlock(dims[stage], drop_prob=dp_rates[dp_index], layer_scale_init=layer_scale_init_value)(layer)
            dp_index += 1
    
    layer = GlobalAveragePooling2D()(layer)
    layer = LayerNormalization(epsilon=1e-6)(layer)
    output = Dense(NUM_CATEGORIES, activation="softmax")(layer)

    model = Model(input, output)
    
    model.compile(
        optimizer=tf.keras.optimizers.AdamW(learning_rate=0.001),
        loss="categorical_crossentropy",
        metrics=['accuracy'])
    
    return model

if __name__ == "__main__":
    main()
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
                                     Concatenate, Reshape, Multiply, Activation, Lambda, Dropout)

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
    # Round filters based on width coefficient
    def round_filters(filters, width_coefficient, depth_divisor=8):
        if not width_coefficient:
            return filters
        
        filters *= width_coefficient
        new_filters = int(filters + depth_divisor / 2) // depth_divisor * depth_divisor
        new_filters = max(depth_divisor, new_filters)
        
        if new_filters < 0.9 * filters:
            new_filters += depth_divisor
        
        return int(new_filters)

    def round_repeats(repeats, depth_coefficient):
        if not depth_coefficient:
            return repeats
        return int(math.ceil(depth_coefficient * repeats))

    # Squeeze-and-Excitation
    def sq_ex_block(tensor, sq_ex_ratio):
        filters = tensor.shape[-1]
        reduced = max(1, int(filters * sq_ex_ratio))

        layer = GlobalAveragePooling2D()(tensor)
        layer = Reshape((1, 1, filters))(layer)
        layer = Conv2D(reduced, 1, activation="swish")(layer)
        layer = Conv2D(filters, 1, activation="sigmoid")(layer)

        return Multiply()([tensor, layer])

    # Stochastic depth (DropConnect)
    class DropConnect(tf.keras.Layer):
        def __init__(self, rate=0.0, **kwargs):
            super().__init__(**kwargs)
            self.rate = rate

        def call(self, x, training=False):
            if not training or self.rate == 0:
                return x
            keep_prob = 1 - self.rate
            batch = tf.shape(x)[0]
            random_tensor = keep_prob + tf.random.uniform([batch,1,1,1])
            binary = tf.floor(random_tensor)
            return (x / keep_prob) * binary

    

    # MBConv (mobile inverted bottleneck)
    def mbconv_block(tensor, in_filters, out_filters, kernel_size, strides,
                    expand_ratio, se_ratio, drop_connect_rate):

        layer = tensor
        expanded_filters = in_filters * expand_ratio

        # Expand
        if expand_ratio != 1:
            layer = Conv2D(expanded_filters, 1, padding="same", use_bias=False)(layer)
            layer = BatchNormalization()(layer)
            layer = Activation("swish")(layer)

        # Depthwise
        layer = DepthwiseConv2D(kernel_size, strides=strides,
                                padding="same", use_bias=False)(layer)
        layer = BatchNormalization()(layer)
        layer = Activation("swish")(layer)

        # Squeeze and excitation
        if se_ratio and 0 < se_ratio <= 1:
            layer = sq_ex_block(layer, se_ratio)

        # Project
        layer = Conv2D(out_filters, 1, padding="same", use_bias=False)(layer)
        layer = BatchNormalization()(layer)

        # Skip connection
        if strides == 1 and in_filters == out_filters:
            if drop_connect_rate:
                layer = DropConnect(drop_connect_rate)(layer)
            layer = Add()([layer, tensor])

        return layer
    
    # (kernel, repeats, in_filters, out_filters, expand, stride, squ_exci)
    blocks_args = [
        (3, 1, 32, 16, 1, 1, 0.25),
        (3, 2, 16, 24, 6, 2, 0.25),
        (5, 2, 24, 40, 6, 2, 0.25),
        (3, 3, 40, 80, 6, 2, 0.25),
        (5, 3, 80, 112, 6, 1, 0.25),
        (5, 4, 112, 192, 6, 2, 0.25),
        (3, 1, 192, 320, 6, 1, 0.25),
    ]

    # Custom values
    width_coefficient = 0.35
    depth_coefficient = 0.35
    dropout_rate = 0.2
    drop_connect_rate = 0.2

    input = Input((IMG_WIDTH, IMG_HEIGHT, 3))

    # Stem
    out_channels = round_filters(32, width_coefficient)
    layer = Conv2D(out_channels, 3, strides=2, padding="same", use_bias=False)(input)
    layer = BatchNormalization()(layer)
    layer = Activation("swish")(layer)

    # Blocks
    total_blocks = sum(round_repeats(r, depth_coefficient) for (_, r, _, _, _, _, _) in blocks_args)
    block_i = 0

    for (k, r, in_f, out_f, exp, s, se) in blocks_args:

        repeats = round_repeats(r, depth_coefficient)
        in_filters  = round_filters(in_f, width_coefficient)
        out_filters = round_filters(out_f, width_coefficient)

        for j in range(repeats):
            stride = s if j == 0 else 1
            layer = mbconv_block(
                layer,
                in_filters=in_filters if j == 0 else out_filters,
                out_filters=out_filters,
                kernel_size=k,
                strides=stride,
                expand_ratio=exp,
                se_ratio=se,
                drop_connect_rate=drop_connect_rate * block_i / total_blocks
            )
            block_i += 1

    # Head
    head_filters = round_filters(1280, width_coefficient)
    layer = Conv2D(head_filters, 1, padding="same", use_bias=False)(layer)
    layer = BatchNormalization()(layer)
    layer = Activation("swish")(layer)

    # Classification
    layer = GlobalAveragePooling2D()(layer)
    if dropout_rate:
        layer = Dropout(dropout_rate)(layer)

    output = Dense(NUM_CATEGORIES, activation="softmax")(layer)

    model = Model(input, output)
    
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
        loss="categorical_crossentropy",
        metrics=['accuracy'])
    
    return model




if __name__ == "__main__":
    main()
